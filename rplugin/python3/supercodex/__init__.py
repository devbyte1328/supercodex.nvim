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

        self.nvim.api.buf_set_option(buffer, "buftype", "prompt")
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

        # ESC → close window
        self.nvim.api.buf_set_keymap(buffer, "i", "<Esc>", "<Cmd>close<CR>", {"silent": True, "nowait": True},)

        self.nvim.command("startinsert")
