import os
from datetime import datetime
import shutil

source = input("Enter source path: ")
archive_dir = "archive_dir"
backup_path = os.path.join(source, archive_dir)

num_days = int(input("Enter limit age for archive decision?"))

# Create archive folder if missing
if not os.path.exists(backup_path):
    os.makedirs(backup_path)

def get_unique_name(dest_folder, filename):
    """Rename file if it already exists in destination"""
    base, ext = os.path.splitext(filename)
    counter = 1
    new_name = filename

    while os.path.exists(os.path.join(dest_folder, new_name)):
        new_name = f"{base}_{counter}{ext}"
        counter += 1

    return new_name

# Process files
for file_name in os.listdir(source):
    source_path = os.path.join(source, file_name)

    if os.path.isfile(source_path):
        # File metadata
        mod_time = os.path.getmtime(source_path)
        human_time = datetime.fromtimestamp(mod_time)
        now = datetime.now()
        difference_in_time = (now - human_time).days

        if difference_in_time > num_days:
            # Handle duplicates
            unique_name = get_unique_name(backup_path, file_name)
            dest_path = os.path.join(backup_path, unique_name)

            shutil.move(source_path, dest_path)
            print(f"Moved: {file_name} → {dest_path}")