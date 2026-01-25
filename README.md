# supercodex.nvim

# This project is a work in progress. this README is currently for development purposes:

SuperCodex is a Neovim plugin that integrates and streamlines the use of local and online LLMs for coding purposes.

## Setup
> [!NOTE]
> This documentation does not cover how to host a local language model or how to obtain credentials for a cloud‑based LLM service. Those steps are the responsibility of the user.  
> The plugin itself is built to use an OpenAI‑compatible API endpoint. It follows the standard OpenAI API specification for all request/response formatting and authentication, so any endpoint that implements that interface will work seamlessly with the plugin.

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
  dir = vim.fn.stdpath("config") .. "/lua/local_plugins/supercodex",
  name = "supercodex",
  opts={}
}
```
