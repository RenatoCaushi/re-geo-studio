#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input || true
python manage.py migrate

# Krijimi i superuser-it përmes shell-it të vetë Django-s
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='Geologyrenni').exists():
    User.objects.create_superuser('Geologyrenni', 'admin@example.com', 'otanerstudio')
    print("Superuser u me sukses!")
else:
    u = User.objects.get(username='Geologyrenni')
    u.set_password('otanerstudio')
    u.is_superuser = True
    u.is_staff = True
    u.is_active = True
    u.save()
    print("Fjalëkalimi u përditësua me sukses!")
EOF