import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Krijon një superuser të ri me të dhëna të reja
u, created = User.objects.get_or_create(username='admin_new')
u.set_password('pass123456')
u.is_superuser = True
u.is_staff = True
u.is_active = True
u.save()

print("NEW_SUPERUSER_CREATED")
