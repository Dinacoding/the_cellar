import os
import django
from pathlib import Path

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'the_cellar.settings')
django.setup()

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def migrate_images_to_cloudinary():
    """Upload all images from media/ folder to Cloudinary"""
    
    media_root = Path('media')
    
    if not media_root.exists():
        print(" No media folder found")
        return
    
    count = 0
    errors = 0
    
    # Walk through all files in media folder
    for root, dirs, files in os.walk(media_root):
        for filename in files:
            local_path = os.path.join(root, filename)
            relative_path = os.path.relpath(local_path, media_root)
            
            try:
                with open(local_path, 'rb') as f:
                    file_content = ContentFile(f.read())
                    
                    # Upload to Cloudinary
                    new_path = default_storage.save(relative_path, file_content)
                    
                    count += 1
                    print(f'✓ Uploaded: {relative_path} -> {new_path}')
                    
            except Exception as e:
                print(f'✗ Error uploading {relative_path}: {str(e)}')
                errors += 1
    
    print(f'\n✓ Complete: {count} files uploaded, {errors} errors')

if __name__ == '__main__':
    migrate_images_to_cloudinary()