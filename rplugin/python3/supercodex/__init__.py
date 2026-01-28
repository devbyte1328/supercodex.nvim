import pynvim

@pynvim.plugin
class Hello:
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.autocmd("VimEnter", pattern="*", sync=False)
    def on_start(self):
        self.nvim.out_write("Hello World! SuperCodex! Python!\n")

    @pynvim.command("HelloWindow", nargs=0, sync=True)
    def hello_window(self):
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
