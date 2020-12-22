Steps

Install Django-allauth: pip3 install django-allauth

Migrate : python3 manage.py migrate

Create superuser : python3 manage.py createsuperuser

Creating site :
.\manage.py shell(for windows)
python3 manage.py shell(for linux)
from django.contrib.sites.models import Site
sites=Site()
sites.domain='http://127.0.0.1:8000/'
sites.name='htpp://127.0.0.1:8000/'
sites.save()
print(sites.id)


Go to http://127.0.0.1:8000/admin
login with superkey credentials

Go to social application
Click on add social application
Enter name : google api
Give client id :641814269707-eqs4ek38c90jf1ai9jhg8aeinhul38jl.apps.googleusercontent.com
Give secret key : bUBOVVdqETGzScKgLtR1M3EB
from available sites move http://127.0.0.1:8000/ to chosen sites

Then run these commands :
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
