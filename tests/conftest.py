import pytest
from unittest.mock import MagicMock
import os
import sys

# This snippet makes sure Python can import the Neovim plugin package
# by adding the project's rplugin/python3 directory to sys.path.
this_file = os.path.abspath(__file__)
# e.g. "/home/main/.config/nvim/lua/local_plugins/supercodex.nvim/tests/conftest.py"
project_root = os.path.dirname(os.path.dirname(this_file))
# e.g. "/home/main/.config/nvim/lua/local_plugins/supercodex.nvim"
rplugin_python_dir = os.path.join(project_root, "rplugin", "python3")
# e.g. "/home/main/.config/nvim/lua/local_plugins/supercodex.nvim/rplugin/python3"
sys.path.insert(0, rplugin_python_dir)
# sys.path[0] == "/home/main/.config/nvim/lua/local_plugins/supercodex.nvim/rplugin/python3"

# Mock NeoVim instance
@pytest.fixture
def mock_nvim():
    nvim = MagicMock()

    # Mock API and funcs namespaces
    nvim.api = MagicMock()
    nvim.funcs = MagicMock()

    # Return a fake buffer id
    nvim.api.create_buf.return_value = 1

    return nvim
