import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
u, created = User.objects.get_or_create(username='Geologyrenni')
u.set_password('otanerstudio')
u.is_superuser = True
u.is_staff = True
u.is_active = True
u.save()

print("ADMIN_PASSWORD_RESET_SUCCESSFUL")