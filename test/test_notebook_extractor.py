import pytest
from unittest import mock
from extractor.notebook_extractor import extract_classes_from_notebook


@mock.patch("builtins.open", new_callable=mock.mock_open,
            read_data='{"cells":[{"cell_type":"code","source":"class MyClass:\\n    pass"}]}')
def test_extract_classes_from_notebook(mock_open):
    result = extract_classes_from_notebook('sample.ipynb')

    assert result is not None, "Result should not be None"
    assert isinstance(result, list), "Result should be a list"
    assert len(result) > 0, "Result list should contain extracted classes"
    assert "class MyClass:\\n    pass" in result, "Extracted class should be in the result"
