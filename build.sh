#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py collectstatic --no-input

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'yourpassword')" | python manage.py shell

