import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'the_cellar.settings')
django.setup()

from products.models import Wine

wines = Wine.objects.filter(image__isnull=False).exclude(image='')

for wine in wines:
    old_path = str(wine.image)
    
    if old_path.startswith('media/'):
        new_path = old_path.replace('media/', '', 1)
        wine.image = new_path
        wine.save()
        print(f'✓ Fixed {wine.name}: {old_path} → {new_path}')
    else:
        print(f'- {wine.name} already correct: {old_path}')

print(f'\n✓ Done!')