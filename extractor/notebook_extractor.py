import json
import re

# Function to extract Python classes from a Jupyter Notebook file
def extract_classes_from_notebook(notebook_file):
    # Initialize a list to store the extracted classes
    extracted_classes = []

    # Open and read the notebook file
    with open(notebook_file, "r", encoding="utf-8") as file:
        notebook_data = json.load(file)

    # Loop through each cell in the notebook
    for cell in notebook_data['cells']:
        # Process only code cells
        if cell['cell_type'] == 'code':
            # Join the lines of code in the cell
            cell_code = "".join(cell['source'])

            # Regular expression pattern to match Python class definitions
            class_pattern = r'\bclass\s+\w+\s*(\(.*\))?:\s*\n(    .*\n)*'

            # Find all matches in the cell code
            matches = re.findall(class_pattern, cell_code, re.MULTILINE)

            # Clean up and store each match
            for match in matches:
                extracted_classes.append(match.strip())

    return extracted_classes

