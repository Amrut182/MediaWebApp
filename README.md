#### Type the following after command in the cloned git repo (make sure that you have latest version of git)
`` pip install -r requirements.txt ``

#### Command for enabling execution of SQL commands in the database file (sqlite3)
`` python manage.py migrate --run-syncdb ``

`` python manage.py makemigrations ``

`` python manage.py migrate ``

#### Run the server using the following command
`` python manage.py runserver ``

##### Side note: If you have latest Django (i.e. Django 3), or any other version please uninstall it by running the following command:
`` pip uninstall Django ``

We strongly recommend use of [python virtual environment](https://docs.python.org/3/tutorial/venv.html)
