import os
import shutil
import logging

logging.basicConfig(
    filename='file_organizer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

FILE_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xls", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css", ".java", ".cpp"]
}

def get_category(file_name):
    _, ext = os.path.splitext(file_name)
    for category, extensions in FILE_CATEGORIES.items():
        if ext.lower() in extensions:
            return category
    return "Others"

def organize_files(target_dir):
    result = []
    if not os.path.exists(target_dir):
        return ["❌ Directory does not exist."]
    
    for item in os.listdir(target_dir):
        item_path = os.path.join(target_dir, item)
        if os.path.isfile(item_path):
            category = get_category(item)
            category_path = os.path.join(target_dir, category)
            os.makedirs(category_path, exist_ok=True)
            shutil.move(item_path, os.path.join(category_path, item))
            result.append(f"Moved: {item} → {category}")
            logging.info(f"Moved: {item} → {category}")
    
    result.append("✅ Files organized successfully!")
    return result
