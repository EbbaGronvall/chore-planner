release: python backend/manage.py makemigrations && python backend/manage.py migrate
web: gunicorn backend.chore_api.wsgi:application 