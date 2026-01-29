import supercodex

def test_window_input_prompt(mock_nvim):
    plugin = supercodex.SuperCodex(mock_nvim)

    plugin.window_input_prompt()

    buffer = 1  # mocked return value

    # Buffer created
    mock_nvim.api.create_buf.assert_called_once_with(False, True)

    # Buffer options
    expected_options = [
        ("buftype", "prompt"),
        ("bufhidden", "wipe"),
        ("swapfile", False),
        ("modifiable", True),
        ("modified", False),
    ]

    for opt, val in expected_options:
        mock_nvim.api.buf_set_option.assert_any_call(buffer, opt, val)

    # Keymaps
    close_cmd = "<Cmd>setlocal nomodified<CR><Cmd>bwipeout!<CR>"
    keymap_opts = {"silent": True, "nowait": True}
    mock_nvim.api.buf_set_keymap.assert_any_call(buffer, "i", "<Esc>", close_cmd, keymap_opts)
    mock_nvim.api.buf_set_keymap.assert_any_call(buffer, "n", "q", close_cmd, keymap_opts)

    # Prompt
    mock_nvim.funcs.prompt_setprompt.assert_called_once_with(buffer, "> ")

    # Window opened with correct config
    mock_nvim.api.open_win.assert_called_once_with(
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

    # Insert mode started
    mock_nvim.command.assert_called_once_with("startinsert")

