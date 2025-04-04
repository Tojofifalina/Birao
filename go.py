import os
import django
import sys

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Birao.settings')
django.setup()

# Étape 1 : makemigrations + migrate
print("🔄 Migration de la base de données...")
os.system('python manage.py makemigrations')
os.system('python manage.py migrate')

# Étape 2 : Création d'un superutilisateur automatique
from django.contrib.auth import get_user_model

User = get_user_model()

# Variables par défaut (à modifier ou injecter par variables d'env)
username = os.getenv("DJANGO_SUPERUSER_USERNAME", "admin")
email = os.getenv("DJANGO_SUPERUSER_EMAIL", "")
password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "adminpass")

if not User.objects.filter(username=username).exists():
    print("👤 Création du superutilisateur...")
    User.objects.create_superuser(username=username, email=email, password=password)
else:
    print("✅ Superutilisateur déjà existant.")

# Étape 3 : Lancer le serveur
print("🚀 Lancement du serveur Django...")
os.system('python manage.py runserver 0.0.0.0:10000')
