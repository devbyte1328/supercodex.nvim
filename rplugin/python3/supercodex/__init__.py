import pynvim

__version__ = "0.0.0-draft"

@pynvim.plugin
class SuperCodex:
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.function("SubmitPrompt", sync=True)
    def prompt_submit(self, args):
        text = args[0]

        # NeoVim makes it difficult to print the text input in a callback,
        # so Vimscript and a NeoVim global variable are used as a bridge.

        # Vimscript that is used to print the text
        self.nvim.command("""
        function! SuperCodexPrintMsg(timer) abort
          echomsg g:supercodex_msg
        endfunction
        """)

        # Store text in NeoVim's global variables
        self.nvim.vars["supercodex_msg"] = text

        # exit the window
        self.nvim.command("stopinsert")
        self.nvim.command("bwipeout!")

        # print AFTER callback returns using the Vimscript function
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
