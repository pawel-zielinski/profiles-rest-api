# Creating a git local project

1. make wanted folder a project folder by adding it in Atom as project file,
2. using terminal go to your project folder and type *git init* to initialize
   local git project,
3. add readme.md file to the project,
4. add .gitignore file to tell your project to do not add files or directories
   written in it while doing *git commit*,
5. add license to the project,
6. type *git add .* to add newly created files to the local git project,
7. type *git commit -am "__note__"* to update local git project.

# Pushing project to GitHub

1. create public/private key; in terminal:
  * *ls ~/.ssh* - check if there is no ssh file in the project directory,
  * *ssh-keygen -t rsa -b 4096 -C "__email address__"* - determine parameters
    of the key,
  * input id for the key,
  * input pass phrase for the key.
2. type *cat ~/.ssh/id_rsa.pub* in terminal,
3. copy outputted key (everything),
4. add ssh key to account by naming it and pasting copied key to the GitHub account,
5. create new public repository with the new name,
6. in terminal run few lines of code suggested by GitHub to **push an existing repository**.

![Git Data Transport Commands](https://user-images.githubusercontent.com/69716167/104955042-ceeeff00-59c9-11eb-831a-04cf95420581.png)

# Creating Vagrant file
(to have local development server that we can use to run and test API)

1. type *vagrant init ubuntu/bionic64* to initialize the project with vagrant file
   and it bases it on ubuntu bionic64 base image.

# Set up Vagrant box

1. by editing Vagrant file customize development server,
2. set system, version, network, add Python to the machine.

# Run and contact to the server

1. run *vagrant up* in the terminal (VirtualBox needed) to start virtual machine,
2. run *vagrant ssh* to connect to the server by ssh protocol.


To access project files go to Vagrant directory on virtual machine by typing *cd /vagrant*
in terminal while connected to the server.
We can add Python program to the project and run it on vm by typing *python __file_name.py__*.

# Create Python Virtual Environment

1. to create Python environment type in terminal *python -m venv ~/env* while
   logged to vm,
2. activate Python virtual environment by typing *source ~/env/bin/activate*,
3. to switch off the environment just type *deactivate*.

# Install required Python packages

1. create new .txt file in your project where you will add packages' names and
   their versions,

Note: it is a good practice to set static version of the program to avoid unexpected
updates that can be incompatible for other packages.

2. While in */vagrant* file and Python Virtual Environment activated, type
   *pip install -r __file_with_previously_added_packages.txt__*.

# Create a new Django project & app

1. make sure that you are still in terminal with virtual environment activated and
   with directory set to */vagrant*,
2. to start a new project with a specific name in a specific location type
   *django-admin.py startproject __name_of_the_project__ .* while "." is the
   root location of the project,

Note: if "." will not be passed there will be created a sub folder with the name
passed in the __name_of_the_project__ argument.

3. to create Django app within our project for our Profiles API type
   *python manage.py startapp profiles_api*. This will create a new file with our app.

Note: Django can consist of one or more sub applications within a project that you can
use to separate different functionality within your project.

# Enable app in the Django

1. open __settings.py__ in Atom,
2. add *"rest_framework"*, *"rest_framework.authtoken"* and *"profiles_api"* to
   INSTALLED_APPS list.

Note: *"rest_framework"* - app for Django REST Framework,
*"rest_framework.authtoken"* - allows to use authentication token functionality.

# Test and commit changes

1. to start Django Web Development Server type in terminal (activate PVE and
   set to __/vagrant__ directory) *python manage.py runserver 0.0.0.0:8000*,

Note: *python manage.py runserver 0.0.0.0:8000* means that we run
Django Web Develpoment Server on every available network adapter (0.0.0.0)
on port 8000 (port must match with settings in __Vagrantfile__). Now the server
is running and we can check it by going to our browser and browsing
__127.0.0.1:8000__.

# Django models

In Django we use models to describe the data we need for our application. Django
then uses these models to set up and configure our database to store our data effectively

Each model in Django maps to a specific table within our database. Django handles
the relationship between our models and the database for us so we never need
to write any SQL statements or interact with the database directly.

# Create a user database model

1. Create user profile model (Django by default can create user model but we
   will override it and create our custom profile model).
2. Best practice is to keep all of the models files (all of the database models)
   in a file called __models.py__ within our app.
3. In __models.py__ import *from django.contrib.auth.models import AbstractBaseUser*
and *from django.contrib.auth.models import PermissionsMixin* as they are standard
base classes that you need to use when overriding or customizing the default
Django user model.
4. Create new class for models (*__go to models.py for more informations__*).

# Add a user model manager

Note: Because we have customized our user model we need to tell Django how to
interact with this user model in order to create users because by default when
it creates a user it expects a username field and a password field but we have
replaced the username field with a email field so we just need to create
a custom manager that can handle creating users with an email fields instead
of a username field.

1. Create custom user manager in __models.py__ (*__for details go to models.py__*).

Note: The way manager work is you specify some functions within the manager
that can be used to manipulate objects within the model that the manager is for.

# Set user custom model

Note: Now that we have set custom user model and custom user model manager we
can configure our project to use these as the default user model.

1. Go to __settings.py__ to the bottom of the file.
2. Type *AUTH_USER_MODEL = '__string that represents the model that we want to use as the Django user model__'*.

# Create Django migration file and sync DB

Note: Migration files are used for models that we have added to the project.
The way that Django manages the database is it creates what is called a migration
file that stores all of the steps required to make our database match our Django
models. Every time we change a model or add additional models to our project we
need to create a new migration file. The migration file will contain the steps
required to modify the database to match our updated models. So for example
if we add a new model to our project then we need to be able to create a new
table in the database and the way that Django does this is it uses what is called
migrations.

1. To create Django migrations use the Django command-line tool. Open up the
terminal and type:
  * *cd __location of Vagrant machine__* - to define which Vagrant machine will be used,
  * *vagrant up* - to start up machine,
  * *vagrant ssh* - to connect to the machine by ssh protocol,
  * *cd /Vagrant*,
  * *source ~/env/bin/activate* - to activate virtual environment,
  * *python manage.py makemigrations __name of the app we want to make migrations for - profiles_api__* -
    to create new migration file for user profiles model,
  * *python manage.py migrate* - run migrations (will make all the changes required
    to set up our database for our Django project).

# Create a superuser

1. To create superuser open up the terminal.
2. With virtual environment activated type *python manage.py createsuperuser*.
3. Follow the instructions given by terminal.

# Enable Django Admin

Note: To enable admin and look up for more informations go to __admin.py__.

# Test Django Admin

1. Start development server by typing *python manage.py runserver 0.0.0.0:8000*.
2. Open up browser and search *127.0.0.1:8000/admin* to launch development website
   with admin enabled.
3. Log in using previously created account of superuser.

Note: Three sections will appear (representing three different apps in our project):
  * __AUTH TOKEN__ - automatically added as part of Django REST framework
    when we enabled our tokens,
  * __AUTHENTICATION AND AUTHORIZATION__ - part of Django. This and __AUTH TOKEN__
    allows authentication system,
  * __PROFILES_API__ - created by us. we can see that the model we created is right
    below named *User profiles*. Notice that it is the name Django got from the name
    we have given to the user profile class in __models.py__ (Django separates camel
    casing [capital letters] and adds letter "s" at the end - this is because it is
    normalized to call classes singular with camel casing).

# APIViews

The Django REST framework offers a couple of helper classes we can use to create
our API endlpoints: the __APIView__ and the __ViewSet__. Both classes are
slightly different and offer their own benefits.

The __APIView__ is the most basic type of view we can use to build our API.
It enables us to describe the logic which makes our API endpoint. An __APIView__
allows us to define functions that match the standard HTTP methods:
  * *get* - return one or more items,
  * *post* - create an item,
  * *put* - update an item,
  * *patch* - partially update an item,
  * *delete* - delete an item.
__Every HTTP method must return response.__
By allowing us to customize the function for each HTTP method on our API URL,
__APIViews__ give us the most control over our application logic. This is perfect
in cases where you need to do something a little bit different from simply updating
objects in the database such as:
  * calling other APIs,
  * working with local files.
When to use __APIViews__:
  * need full control over your application logic (when you are running a very
    complicated algorithm or updating multiple data sources in one API call),
  * processing files and rendering a synchronous response (when you are validating
    a file and returning the result in the same call),
  * calling other APIs/services in the same request,
  * access local files or data.

# Create first APIView

Note: Open __viws.py__ for more informations.

# Configure view URL

Note: The way that Django URLs work is that we have the __urls.py__ (in __profiles_project__)
that is the entry point for all of the URLs in our app. We store every URL in
*urlpatterns* list.

1. We have to create a new __urls.py__ for __profiles_api__ app.
2. Import *include* from *django.urls* in __urls.py__ (__profiles_project__).
3. Add new URL to *urlpatterns* (*'api/'*), call *include* and pass in the name
   of the app and the module we want to include that contains our URLs (*'profiles_api.urls'*).
4. Next go to __urls.py__ in __profiles_api__ and import *path* from *django.urls*
   and *views* from *profiles_api*.
5. Create a new variable or a list variable called *urlpatterns* where we will store
   paths that map to views in our project (more informations - go to __urls.py__ in __profiles_api__).

# Create a serializer

1. Create a new file at __profiles_api__ and call it __serializers.py__
   (for more informations go to __serializers.py__ in __profiles_api__).

# Add POST method to APIView

1. Import *status* and *serializers* to __views.py__.
2. Add *post* class method and add logic to it (more informations in __views.py__).
3. Test the results on web page.

# Add PUT, PATCH and DELETE methods in APIView

1. Go to __views.py__ for more informations.

Note: The difference between PUT and PATCH is that the PUT method updates the whole
object while PATCH only does this partially. So for example if we change the name
and the id for our object and we will use PUT method we will be able to update
both name and id. But if we use PATCH method we will be able to update name or id.

2. Test the results on website. Remember that PATCH method is more complex but
   still quite similar to the PUT so you will find it in PUT area but in __Raw data__
   overlap.


# Profiles REST API

Profiles REST API course code.
