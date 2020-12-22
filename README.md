#### type the following after command in the cloned git repo (make sure that you have latest version of git)
`` pip install -r requirements.txt  ``

#### The following commands must be run to install the Django version needed for this mini project
`` pip install Django~=2.2.4``

#### You can check the version of Django in your system by running the following command:
``python -m django --version ``

#### Command for enabling execution of SQL commands in the database file (sqlite3)
``python manage.py migrate``

##### Side note: If you have latest Django (i.e. Django 3), or any other version please uninstall it by running the following command:
`` pip uninstall Django`` 

##### For Facebook Login you need to install social-auth-app-django:
`` pip install social-auth-app-django``