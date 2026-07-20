-> In this repo, this all files are the projects which had been performed by me during the 15 days summer internship at Inlabz Technology.

-> In this projects, I had used Django and Python.

-> Required things are PyCharm, Python-Environment, Django(v-2026.1.2)

-> To install the Django in the PyCharm terminal use this command: ->
        pip install django

-> To install the PyCharm 
        https://www.jetbrains.com/pycharm/download/?section=windows

-> To set up the Django Project in your system, follow this steps: 
  1. Show the welcome Home Page after completing the full Set-up of the Pycharm; click on the New Project, set the project path and keep as it for Python version.
  2. Open the New project terminal and type this command to install the Django, 
        pip install django
  3. Then after type this command to setup the project: -> django-admin startproject projectname .
  4. Then after type this command to setup the project app: -> django-admin startapp appName
  5. Then Go to the Project Folder and click on the setting.py file and then add the app name in the last INSTALLED_APP Section
  6. Then type this command in the terminal: -> python manage.py migrate
  7. Then type this command to open the Django_project: -> python manage.py runserver
  8. Then create the superuser using this command: -> python manage.py createsuperuser
  9. In this case, type User_name*, Email, Password*, Repeat-Password* and then type Y
  10. Then you can login into the django-admin panel using the link :-> http://127.0.0.1:8000/admin/
  11. After that make your project in the models.py and then type this command: -> python manage.py makemigrations
  12. After that Register the all models in the admin.py file and then type this command: -> python manage.py migrate
  12. And at last you have to type the again the python manage.py runserver
