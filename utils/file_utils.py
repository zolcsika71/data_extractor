# Function to save extracted classes to a text file
def save_to_file(data, file_path):
    # Open file in write mode with UTF-8 encoding
    with open(file_path, "w", encoding="utf-8") as file:
        # Write each class to the file, separated by two newlines for readability
        for item in data:
            file.write(item + "\n\n")

