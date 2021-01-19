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

# Create user database model

1. Create user profile model (Django by default can create user model but we
   will override it and create our custom profile model).
2. Best practice is to keep all of the models files (all of the database models)
   in a file called __models.py__ within our app.
3. In __models.py__ import *from django.contrib.auth.models import AbstractBaseUser*
and *from django.contrib.auth.models import PermissionsMixin* as they are standard
base classes that you need to use when overriding or customizing the default
Django user model.
4. Create new class for models (*__go to models.py for more informations__*)

# Profiles REST API

Profiles REST API course code.
