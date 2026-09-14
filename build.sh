#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input || true
python manage.py migrate

# Rregullon fjalëkalimin e adminit
python fix_user.py