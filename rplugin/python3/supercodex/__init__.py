import pynvim
import requests
import json

__version__ = "0.0.0-draft"

@pynvim.plugin
class SuperCodex:
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.function("SubmitPrompt", sync=True)
    def prompt_submit(self, args):
        user_input = args[0]

        api_key = self.nvim.vars.get("supercodex_api_key", "")
        url = self.nvim.vars.get("supercodex_url", "")
        model = self.nvim.vars.get("supercodex_model", "")

        payload = {
            "model": model,
            "messages": [{"role": "user", "content": user_input}],
        }

        response = requests.post(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}",
            },
            data=json.dumps(payload),
        )

        output = response.json()["choices"][0]["message"]["content"]

        self.nvim.command("""
        function! SuperCodexPrintMsg(timer) abort
          echomsg g:supercodex_msg
        endfunction
        """)

        self.nvim.vars["supercodex_msg"] = output

        self.nvim.command("stopinsert")
        self.nvim.command("bwipeout!")
        self.nvim.command("call timer_start(0, function('SuperCodexPrintMsg'))")

    @pynvim.command("WindowInputPrompt", nargs=0, sync=True)
    def window_input_prompt(self):
        buffer = self.nvim.api.create_buf(False, True)

        # These options and keymaps fix the buffer to allow closing the window, discarding text, and exitting the file.
        # Without these fixes NeoVim's default buffer configuration prevents closing the buffer and raises errors.
        self.nvim.api.buf_set_option(buffer, "buftype", "prompt")
        self.nvim.api.buf_set_option(buffer, "bufhidden", "wipe")
        self.nvim.api.buf_set_option(buffer, "swapfile", False)
        self.nvim.api.buf_set_option(buffer, "modifiable", True)
        self.nvim.api.buf_set_option(buffer, "modified", False)
        close_cmd = "<Cmd>setlocal nomodified<CR><Cmd>bwipeout!<CR>"
        self.nvim.api.buf_set_keymap(buffer, "i", "<Esc>", close_cmd, {"silent": True, "nowait": True})
        self.nvim.api.buf_set_keymap(buffer, "n", "q", close_cmd, {"silent": True, "nowait": True})

        self.nvim.funcs.prompt_setprompt(buffer, "> ")
        self.nvim.funcs.prompt_setcallback(buffer, "SubmitPrompt")

        self.nvim.api.open_win(
            buffer,
            True,
            {
                "relative": "editor",
                "row": 10,
                "col": 10,
                "width": 40,
                "height": 1,
                "style": "minimal",
            },
        )

        self.nvim.command("startinsert")
