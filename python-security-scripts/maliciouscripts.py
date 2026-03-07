import os

extensions = [".exe", ".ps1", ".bat", ".vbs"]
search_dir = "C:\\Users"

for root, dirs, files in os.walk(search_dir):
    for file in files:
        if any(file.lower().endswith(ext) for ext in extensions):
            print(os.path.join(root, file))