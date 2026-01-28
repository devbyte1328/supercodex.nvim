import pytest
from unittest.mock import MagicMock
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PYTHON_RPLUGIN = ROOT / "rplugin" / "python3"
sys.path.insert(0, str(PYTHON_RPLUGIN))

@pytest.fixture
def mock_nvim():
    nvim = MagicMock()

    # Mock API and funcs namespaces
    nvim.api = MagicMock()
    nvim.funcs = MagicMock()

    # Return a fake buffer id
    nvim.api.create_buf.return_value = 1

    return nvim
