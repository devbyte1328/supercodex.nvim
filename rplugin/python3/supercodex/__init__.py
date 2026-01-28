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
        input_buffer = self.nvim.api.create_buf(False, True)

        self.nvim.api.buf_set_option(input_buffer, "buftype", "prompt")
        self.nvim.funcs.prompt_setprompt(input_buffer, "> ")

        self.nvim.api.open_win(
            input_buffer,
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
