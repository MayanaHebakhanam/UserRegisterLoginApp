# UserRegisterLoginApp
UserRegisterLoginApp using Django

Create your app using 'django-admin startapp signupLoginApp' and register it in settings.py

Create a model User with custom fields for a user to register.

Register this model in admin panel to connect with sqlite3 database.
To save database details run below commands:
python migrate.py makemigrations
python migrate.py migrate

Create Login.html,Signup.html,Home.html pages

Create a superuser who acts as an Admin

Create views and urls path as per your customization

Now run the project using 'python manage.py runserver' command and check your results at specified urls and check data entries in sqlite database



