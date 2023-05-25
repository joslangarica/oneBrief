import os

def save_to_file(filename, content, subdirectory=None):
    if subdirectory is None:
        subdirectory = "static/generated/preview/"

    if not os.path.exists(subdirectory):
        os.makedirs(subdirectory)
        
    file_path = os.path.join(subdirectory, filename)
    
    with open(file_path, 'w') as file:
        file.write(content)
