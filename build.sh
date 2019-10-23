python manage.py migrate
python manage.py  makemigrations
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@djangox.com', 'password123')" | python manage.py shell
