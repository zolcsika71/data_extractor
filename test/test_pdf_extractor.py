from unittest import mock

from extractor.pdf_extractor import extract_classes_from_pdf

@mock.patch("builtins.open", new_callable=mock.mock_open, read_data=b"dummy data")
@mock.patch("PyPDF2.PdfReader")
def test_extract_classes_from_pdf(mock_pdf_reader, mock_open):
    mock_reader_instance = mock.Mock()
    mock_pdf_reader.return_value = mock_reader_instance

    mock_reader_instance.pages = [mock.Mock(extract_text=mock.Mock(return_value="class MyClass:\n    pass"))]

    result = extract_classes_from_pdf('/data/pdf/PortfolioPython.pdf')

    assert result is not None, "Result should not be None"
    assert isinstance(result, list), "Result should be a list"
    assert len(result) > 0, "Result list should contain extracted classes"
    assert "class MyClass:\n    pass" in result, "Extracted class should be in the result"






