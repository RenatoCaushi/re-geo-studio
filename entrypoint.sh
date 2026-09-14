#!/usr/bin/env bash

# Ekzekutohet gjithmonë kur ndizet serveri
python manage.py migrate

python manage.py shell << 'EOF'
from django.contrib.auth import get_user_model
User = get_user_model()
u, created = User.objects.get_or_create(username='Geologyrenni')
u.set_password('otanerstudio')
u.is_superuser = True
u.is_staff = True
u.is_active = True
u.save()
print("ADMIN_CREATED_SUCCESSFULLY")
EOF

# Nis serverin gunicorn
exec gunicorn config.wsgi:application