import os
import shutil

# Folder to organize (change this if needed)
folder = input("Enter folder path (default is current): ") or "."

# File type mappings
types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv"],
    "Code": [".py", ".js", ".html", ".css"],
    "Archives": [".zip", ".tar", ".gz"]
}

def organize(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            for category, extensions in types.items():
                if ext in extensions:
                    target_dir = os.path.join(folder_path, category)
                    os.makedirs(target_dir, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_dir, filename))
                    print(f"Moved {filename} to {category}/")
                    break

organize(folder)
