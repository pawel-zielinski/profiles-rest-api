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
our API endpoints: the __APIView__ and the __ViewSet__. Both classes are
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

# ViewSets

Just like __APIViews__, __ViewSets__ allow us to write the logic for our endpoints. However
instead of defining functions which map to HTTP methods, __ViewSets__ accept functions
that map to common API object actions such as:
  * *list* - for getting a list of objects,
  * *create* - for creating new objects,
  * *retrieve* - for getting a specific object,
  * *update* - for updating an object,
  * *partial_update* - for updating part of an object,
  * *destroy* - for deleting an object.
Additionally __ViewSets__ can take care a lot of the common logic for us.
They are perfect for writing APIs that perform standard database operations
and they are the fastest way to make an API which interfaces with a database back-end.
When to use __ViewSets__ rather than __APIViews__:
  * if you need to write an API that performs a simple create, read, update
    and delete operations (CRUD) on an existing database model,
  * if you need a quick and simple API,
  * if you need little or no customization on the logic,
  * if your API is working with standard database structure.

# Create a simple ViewSet

1. Head over to view.py.
2. Import *viewsets* from *rest_framework*.
3. Create a new *HelloViewSet* class and add functions to it.

Note: __ViewSet's__ methods are different from the __APIView's__. While __APIView's__ methods
concentrate for particular HTTP methods that you want to support on your endpoint,
__ViewSet's__ methods represent actions that you would perform on a typical API.

# Add URL Router

Note: Just like with our __APIView__ we need to register our new __ViewSet__ with
a URL to make it accessible through our API. The way that you register the __ViewSets__
with a URL is slightly different from how you register the __APIView__ with the URL.

To register __APIView__ with the *hello-view/* URL we used the *path* function in
__profiles_api/urls.py__.

To register __ViewSet__ you have to:
1. Use *Router* (class provided by the Django REST Framework) in order to generate
   the different routes that are available for our __ViewSet__:
   * in __profiles_api/urls.py__ import *include* from *django.urls* and
     *DefaultRouter* from *rest_framework.routers*,
   * to use *DefaultRouter* is you assign the router to a variable,
2. Use *__variable__.register* to register specific __ViewSets__ with our router
   (*"/"* is not needed in __ViewSets'__ URLs).
3. Add the URL to existing *urlpatterns*.

Note: So as you register new routes with our router, it generates a list of URLs
that are associated for our __ViewSet__. It figures out the URls that are required
for all of the functions that we add to our __ViewSet__ and then it generates this
URLs list which we can pass in to using the *path* function and the *include*
function to our *urlpatterns*.

More informations in __profiles_api/urls.py__.

# Add create, retrieve, update, partial_update and destroy functions

1. Go to __views.py__ and add serializer to *HelloViewSet* class in the same way
   that you added it to the __APIView__.

Note: We can use the same serializer that we created for our __APIView__.

2. Add functions in *HelloViewSet* class.

For more informations head over to __views.py__.

# Test ViewSet

Note: Unlike the API view we do not actually see the put, patch and delete
methods here on the */hello-viewset* API. That is because __ViewSets__ expect that you
will use this endpoint to retrieve a list of objects in the database and you
will specify a primary key ID in the URL when making changes to a specific object.
So if we want to see these additional functions that we added, we need to add
something to the end of the URL. Now in in this case because we are not actually
retrieving any real objects, it does not matter what you type, but if you just put
a number here, that would represent a primary key of an object, that you wanted to
change and hit enter, then it will change the page to the get request.

# Plan our profile API

Now that we know how to make a simple API we can move on to building our
profiles API. Before we get started let's explain the specification of
what we are going to build. Our profile API is going to be able to handle the
following:
  1. creating a profile to handle the registration of new users in the system -
     this will include validating the profile data to ensure that a user provided
     all the required fields,
  2. listing existing profiles so users can find other users in the system - this
     needs to include a way to search for users by email or name,
  3. viewing a specific profile by the profile ID,
  4. updating the profile of the logged in user - users in the system should be
     able to change their name, email address and password for their profile,
  5. provide a way for users to delete their own profile.

So what URLs and methods might our API have? Since our API manages profiles it
makes sense to give it the name *profile*.
  1. So the URL would be __/api/profile/__:
      * the route of the URL will list all profiles -> HTTP GET method is called,
      * create a new profile -> HTTP POST method is called.
  2. If the URL would be __/api/profile/<profile_id>/__    
      * view all the details of a specific profile object -> HTTP GET method is called,
      * update the object -> HTTP PUT or PATCH method is called,
      * remove object completely from the system -> HTTP DELETE method is called.

# Create user profile serializer

1. Import *models* from *profiles_api*.
2. Add a new serializer to the __serializers.py__ file (the serializer that we
   are going to add is model serializer - similar to a regulat serializer except
   it has a bunch of extra functionality witch makes it really easy to work with
   existing Django database models).
3. Create meta class.

Note: The way that you work with model serializers is you use a meta class to
configure the serializer to point to a specific model in our project.

For more informations go to __profiles_api/serializers.py__.

# Create profiles ViewSet

Note: Now that we have our *UserProfileSerializer* we can go ahead and create a
ViewSet to access the serializer through an endpoint.

1. Head over to __profiles_api/views.py__.
2. Import *models* from *profiles_api*.

Note: What we're going to use for our user profile API is something called
a *Model ViewSet*. The Model ViewSet is very similar to a standard ViewSet
except it's specifically designed for managing models through our API.
So it has a lot of the functionality that we need for managing models built into it.

3. Create new Model ViewSet - a class called *UserProfileViewSet*.

For more informations head over to __profiles_api/views.py__.

# Register profile Viewset with the URL router - to access it from the browser

1. Open up __profiles_api/urls.py__.
2. If needed import *views* from *profiles_api*.
3. Register ViewSet (more in __profiles_api/urls.py__).

# Create permission class

Note: We want to be able to restrict the users so they can only make changes to their
own profile in the system. We do that using a Django permissions class.

1. Create a new __profiles_api/permissions.py__ file.
2. Import *permissions* from *rest_framework*.
3. Use this *permission* class as the base for our custom permission class.
4. Define new class method which will be checking if object is requesting
   a safe method or is requsesting method on it self.

Note: Safe method is the method that is not making changes on anything.

For more go to __profiles_api/permissions.py__.

# Add authentication and permissions to Viewset

1. Go to __profiles_api/views.py__.
2. Import *TokenAuthentication* from *rest_framework.authentication*. The token
   authentication is going to be the type of authentication we use for users to
   authenticate themselves with our API.

Note: Token authentication works by generating a random token string when the
user logs in and then every request we make to their API that we need to
authenticate we add this token string to the request and that is effectively
a password to check that every request made is authenticated correctly.

3. Import *permissions* from *profiles_api*.
4. Head over to *UserProfileViewSet* class and configure this to use the correct
   authentication and permissions classes.

For more go to __profiles_api/views.py__.

# Profiles REST API

Profiles REST API course code.
