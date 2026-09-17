#!/usr/bin/env bash
set -e

# Ekzekuto vetëm gunicorn pa prekur bazën e të dhënave
exec gunicorn config.wsgi:application