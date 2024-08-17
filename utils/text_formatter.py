# Function to format the extracted classes for output (optional, based on needs)
def format_classes(classes):
    # For each class, you can add additional formatting, like headers or separators
    formatted_classes = []
    for cls in classes:
        # Example: adding a header before each class
        formatted_class = f"### Extracted Class:\n\n{cls}"
        formatted_classes.append(formatted_class)

    return formatted_classes

