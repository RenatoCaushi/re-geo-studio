import os
import sys
from pathlib import Path

# Shto dosjen kryesore në Python Path
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

# Krijon ose përditëson përdoruesin
user, created = User.objects.get_or_create(username='Geologyrenni')
user.set_password('otanerstudio')
user.is_superuser = True
user.is_staff = True
user.is_active = True
user.save()

if created:
    print("Përdoruesi u krijua me sukses!")
else:
    print("Fjalëkalimi u përditësua me sukses!")