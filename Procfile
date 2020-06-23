release: python manage.py migrate --pythonpath jobtracker.manage
web: gunicorn --pythonpath jobtracker jobtracker.wsgi