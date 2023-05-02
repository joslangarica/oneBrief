def save_to_file(filename, content):
    if not content:
        print(f"Error: Unable to save '{filename}' as content is missing.")
        return
    try:
        with open(filename, "w") as file:
            file.write(content)
        print(f"File '{filename}' is successfully saved.")
    except Exception as e:
        print(f"Error while saving file '{filename}': {e}")