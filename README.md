# UserRegisterLoginApp
UserRegisterLoginApp using Django

Step-1: Create your app using 'django-admin startapp signupLoginApp' and register it in settings.py

Step-2: Create a model User with custom fields for a user to register.

Step-3: Register this model in admin panel to connect with sqlite3 database.
To save database details run below commands:
python migrate.py makemigrations
python migrate.py migrate

Step-4: Create Login.html,Signup.html,Home.html pages

Step-5: Create a superuser who acts as an Admin

Step-6: Create views and urls path as per your customization

Step-7: Now run the project using 'python manage.py runserver' command and check your results at specified urls and check data entries in sqlite database



