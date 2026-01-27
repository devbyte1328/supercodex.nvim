import pynvim

@pynvim.plugin
class Hello:
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.autocmd("VimEnter", pattern="*", sync=False)
    def on_start(self):
        self.nvim.out_write("Hello World! SuperCodex! Python!\n")
