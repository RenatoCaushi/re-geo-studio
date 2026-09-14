#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input || true
python manage.py migrate

# Ekzekuton script-in e fjalëkalimit
python fix_user.py