import os
import shutil

def migrate_media(src_dir, dest_dir):
    """
    Migrates all files and folders from src_dir to dest_dir.
    """
    if not os.path.exists(src_dir):
        print(f"Source directory '{src_dir}' does not exist.")
        return

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        dest_path = os.path.join(dest_dir, item)
        if os.path.isdir(src_path):
            shutil.copytree(src_path, dest_path, dirs_exist_ok=True)
        else:
            shutil.copy2(src_path, dest_path)
        print(f"Migrated: {src_path} -> {dest_path}")

if __name__ == "__main__":
    # Example usage: update these paths as needed
    source_media_dir = "path/to/source/media"
    destination_media_dir = "path/to/destination/media"
    migrate_media(source_media_dir, destination_media_dir)