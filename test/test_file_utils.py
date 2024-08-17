import pytest
from utils.file_utils import read_file, write_file

def test_read_file(mocker):
    mock_open = mocker.patch("builtins.open", mocker.mock_open(read_data="file content"))
    content = read_file('sample.txt')
    mock_open.assert_called_once_with('sample.txt', 'r')
    assert content == "file content"

def test_write_file(mocker):
    mock_open = mocker.patch("builtins.open", mocker.mock_open())
    result = write_file('output.txt', 'Sample content')
    mock_open.assert_called_once_with('output.txt', 'w')
    mock_open().write.assert_called_once_with('Sample content')
    assert result is True
