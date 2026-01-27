# supercodex.nvim

# This project is a work in progress. this README is currently for development purposes:

SuperCodex is a Neovim plugin that integrates, streamlines, and improves the use of local and cloud-based LLM's for coding purposes.

## Setup

> [!NOTE]
> This documentation does **not** cover how to host an LLM or how to obtain credentials for cloud-based LLM services. These steps are the responsibility of the user.
>
> The plugin is built to work with an **OpenAI-compatible API endpoint**. It follows the standard OpenAI API specification for request/response formatting and authentication. As a result, **any service that implements this interface should work seamlessly** with the plugin.
>
> In addition, users are responsible for selecting the LLM model. You should look for the **latest and best-performing LLM**, especially one that scores highly on **coding and programming benchmarks**, and that you can either run locally on your own hardware, or access through a cloud-based provider.
>
> Below are some useful resources to help you explore, host, or discover local LLM's:
>
> https://github.com/ggml-org/llama.cpp  
> https://github.com/open-webui/open-webui  
> https://huggingface.co/  
> https://huggingface.co/TheBloke

### 🌐 Live Version
lazy.nvim:

```
{
  "devbyte1328/supercodex.nvim",
  opts={}
}
```

### 💻 Local Version (for testing)

Create local plugins folder:

```
mkdir -p ~/.config/nvim/lua/local_plugins
```

Navigate to local plugins folder and Git clone this repository:

```
cd ~/.config/nvim/lua/local_plugins
```

```
git clone https://github.com/devbyte1328/supercodex.nvim.git
```

lazy.nvim:

```
{
  dir = vim.fn.stdpath("config") .. "/lua/local_plugins/supercodex.nvim",
  name = "supercodex",
  opts={}
}
```
