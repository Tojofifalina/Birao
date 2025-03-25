import os
import time

print("migrate")
#os.system('python manage.py makemigrations')
os.system('python manage.py migrate')

#python manage.py createsuperuser
#os.system('python manage.py createsuperuser')
