#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input || true
python manage.py migrate

# Përditësimi i fjalëkalimit të adminit direkt gjatë build-it
python manage.py shell << 'EOF'
from django.contrib.auth import get_user_model
User = get_user_model()
u, created = User.objects.get_or_create(username='Geologyrenni')
u.set_password('otanerstudio')
u.is_superuser = True
u.is_staff = True
u.is_active = True
u.save()
print("Fjalekalimi u ndryshua me sukses!")
EOF