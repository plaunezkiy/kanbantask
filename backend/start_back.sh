python app/manage.py migrate

gunicorn kanban.wsgi:application --bind 0.0.0.0:8000 
