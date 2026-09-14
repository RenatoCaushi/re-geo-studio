#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input || true
python manage.py migrate

# Krijimi i superuser-it në një rresht të vetëm
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); u, _ = User.objects.get_or_create(username='Geologyrenni'); u.set_password('otanerstudio'); u.is_superuser = True; u.is_staff = True; u.is_active = True; u.save(); print('Superuser ok')"