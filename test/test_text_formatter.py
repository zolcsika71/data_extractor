import pytest
from utils.text_formatter import format_text

def test_format_text():
    result = format_text('Sample Text')
    assert result == 'Formatted Sample Text'
