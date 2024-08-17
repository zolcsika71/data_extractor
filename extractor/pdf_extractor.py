import PyPDF2
import re

# Function to extract Python classes from a PDF file
def extract_classes_from_pdf(pdf_file):
    # Initialize a list to store the extracted classes
    extracted_classes = []

    # Open and read the PDF file
    with open(pdf_file, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""

        # Extract text from each page
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()

    # Regular expression pattern to match Python class definitions
    class_pattern = r'\bclass\s+\w+\s*(\(.*\))?:\s*\n(    .*\n)*'

    # Find all matches in the text
    matches = re.findall(class_pattern, text, re.MULTILINE)

    # Clean up and store each match
    for match in matches:
        extracted_classes.append(match.strip())

    return extracted_classes


