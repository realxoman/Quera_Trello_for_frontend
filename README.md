# Quera_Trello_for_frontend

Add a .env file to your project:
```
SECRET_KEY=
DEBUG=
```

Install the requirements:
```bash
pip install -r requirements.txt
```

Makemigrations and migrate
```bash
python manage.py makemigrations
python manage.py migrate
```

If you need a superuser to access django admin you can run this:
```bash
python manage.py createsupseruser
```

Then run and access to project:

```bash
python manage.py runserver
```

Project Urls:
- Swagger: http://localhost:8000
- Admin: http://localhost:8000/admin

Best.
