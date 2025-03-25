import os
from django.core.management import execute_from_command_line

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Birao.settings")  # Remplacez `myproject` par le nom de votre projet
    execute_from_command_line(["manage.py", "runserver", "192.168.43.1:8000"])
#pyinstaller --onefile --add-data "myproject/settings.py;myproject" run.py
#pyinstaller --onefile --hidden-import="django" run.py
