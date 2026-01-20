#!/usr/bin/env bash
set -euo pipefail

OS="$(uname -s)"
ARCH="$(uname -m)"

BACKEND="cpu"

# Allow manual override
if [[ -n "${LLAMA_BACKEND:-}" ]]; then
  echo "LLAMA_BACKEND override detected: $LLAMA_BACKEND"
  echo "selected_backend=$LLAMA_BACKEND"
  exit 0
fi

echo "Detected OS: $OS"
echo "Detected ARCH: $ARCH"

# ----------------------------
# macOS
# ----------------------------
if [[ "$OS" == "Darwin" ]]; then
  if [[ "$ARCH" == "arm64" ]]; then
    BACKEND="macos-arm64"
  else
    BACKEND="macos-x64"
  fi

  echo "selected_backend=$BACKEND"
  exit 0
fi

# ----------------------------
# Linux
# ----------------------------
if [[ "$OS" == "Linux" ]]; then
  # ---- CUDA (highest priority)
  if command -v nvidia-smi >/dev/null 2>&1; then
    if nvidia-smi >/dev/null 2>&1; then
      BACKEND="linux-cuda"
      echo "CUDA detected"
      echo "selected_backend=$BACKEND"
      exit 0
    fi
  fi

  # ---- ROCm / HIP (best-effort)
  if [[ -d "/opt/rocm" ]] || command -v rocminfo >/dev/null 2>&1; then
    BACKEND="linux-hip"
    echo "ROCm detected"
    echo "selected_backend=$BACKEND"
    exit 0
  fi

  # ---- Vulkan (portable GPU fallback)
  if command -v vulkaninfo >/dev/null 2>&1; then
    if vulkaninfo >/dev/null 2>&1; then
      BACKEND="linux-vulkan"
      echo "Vulkan detected"
      echo "selected_backend=$BACKEND"
      exit 0
    fi
  fi

  # ---- CPU fallback by architecture
  case "$ARCH" in
    x86_64|amd64)
      BACKEND="linux-x64"
      ;;
    aarch64|arm64)
      BACKEND="linux-arm64"
      ;;
    s390x)
      BACKEND="linux-s390x"
      ;;
    *)
      BACKEND="linux-cpu-unknown"
      ;;
  esac

  echo "No GPU backend detected"
  echo "selected_backend=$BACKEND"
  exit 0
fi

# ----------------------------
# Unknown OS
# ----------------------------
echo "Unsupported OS: $OS"
echo "selected_backend=cpu"
exit 0

