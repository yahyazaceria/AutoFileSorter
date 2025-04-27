import os
import shutil

# Set your paths here
DOCUMENTS_PATH = r'/Users/Yahya/Documents'   # Change to your Documents path
DEV_PATH = r'/Users/Yahya/dev'               # Change to your dev folder path
SOURCE_PATH = r'/Users/Yahya/Downloads'      # Folder to watch/move files from

# File type categories and their extensions
file_types = {
    'pdfs': ['.pdf'],
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'screenshots': ['.png'],  # We'll refine this below
    'dev': ['.py', '.js', '.html', '.css', '.java', '.c', '.cpp']
}

def is_screenshot(filename):
    # Adjust this function for your OS/language/filename pattern
    # Common screenshot patterns: "Screenshot", "スクリーンショット", "屏幕截图", etc.
    return filename.lower().startswith('screenshot') or 'screenshot' in filename.lower()

def organize_folder(source_folder, documents_folder, dev_folder):
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            # Check for dev files
            if ext in file_types['dev']:
                dest_folder = dev_folder
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, filename))
            # Check for screenshots (by extension and filename)
            elif ext in file_types['screenshots'] and is_screenshot(filename):
                dest_folder = os.path.join(documents_folder, 'screenshots')
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, filename))
            # Check for images (excluding screenshots)
            elif ext in file_types['images']:
                dest_folder = os.path.join(documents_folder, 'images')
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, filename))
            # Check for pdfs
            elif ext in file_types['pdfs']:
                dest_folder = os.path.join(documents_folder, 'pdfs')
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, filename))
            else:
                # Optionally handle other files
                pass

# Usage
organize_folder(SOURCE_PATH, DOCUMENTS_PATH, DEV_PATH)
