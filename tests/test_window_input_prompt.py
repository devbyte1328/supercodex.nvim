import supercodex

def test_window_input_prompt(mock_nvim):
    plugin = supercodex.SuperCodex(mock_nvim)

    plugin.window_input_prompt()

    # Buffer created
    mock_nvim.api.create_buf.assert_called_once_with(False, True)

    # Prompt set
    mock_nvim.funcs.prompt_setprompt.assert_called_once_with(1, "> ")

    # Window opened
    mock_nvim.api.open_win.assert_called_once()

    # Insert mode started
    mock_nvim.command.assert_called_with("startinsert")
