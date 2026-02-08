import supercodex

# The text print testing is skipped because it's only used for development/debugging purposes,
# tests for the text will be added when the LLM api calls are added.

def test_submit_prompt(mock_nvim):
    plugin = supercodex.SuperCodex(mock_nvim)

    plugin.window_input_prompt()

    buffer = 1  # mocked return value

    # Buffer created
    mock_nvim.api.create_buf.assert_called_once_with(False, True)

    # Callback
    mock_nvim.funcs.prompt_setcallback.assert_called_once_with(buffer, "SubmitPrompt")

