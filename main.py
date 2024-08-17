# Import the necessary modules from extractor and utils
from extractor.pdf_extractor import extract_classes_from_pdf
from extractor.notebook_extractor import extract_classes_from_notebook
from utils.file_utils import save_to_file
from utils.text_formatter import format_classes

# Main function to orchestrate the extraction process
def main():
    # Define input files (PDFs and Jupyter Notebooks)
    pdf_files = ["data/pdf/PortfolioPython.pdf", "data/pdf/AdvPortfolioPython.pdf"]
    notebook_files = ["data/notebook/PortfolioPython.ipynb", "data/notebook/AdvPortfolioPython.ipynb"]

    # Extract classes from PDF files
    pdf_classes = []
    for pdf_file in pdf_files:
        pdf_classes.extend(extract_classes_from_pdf(pdf_file))

    # Extract classes from Jupyter Notebook files
    notebook_classes = []
    for notebook_file in notebook_files:
        notebook_classes.extend(extract_classes_from_notebook(notebook_file))

    # Combine extracted classes from all sources
    all_classes = pdf_classes + notebook_classes

    # Optionally format the extracted classes before saving
    formatted_classes = format_classes(all_classes)

    # Save the formatted classes to a text file
    save_to_file(formatted_classes, "output/extracted_classes.txt")

# Run the main function
if __name__ == "__main__":
    main()

