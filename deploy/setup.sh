#!/usr/bin/env bash

set -e

# TODO: Set to URL of git repo.
PROJECT_GIT_URL='https://github.com/pawel-zielinski/profiles-rest-api.git'      # This is because the script is going to clone the content of our project to the server when we run it.

PROJECT_BASE_PATH='/usr/local/apps/profiles-rest-api'                           # This is path which is the directory we are going to store our project on the server.

echo "Installing dependencies..."
apt-get update
apt-get install -y python3-dev python3-venv sqlite python-pip supervisor nginx git  # Next we instal some dependencies which we need to run our application on a server.
                                                                                # Git - is going to be used to clone the project,
                                                                                # NGINX - is the webserver that is going to serve the static files and act as a proxy to our uWSGI service,
                                                                                # uWSGI - is the service that is going to run in supervisor,
                                                                                # SQLITE - is going to be used for the database.
# Create project directory
mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH                                   # To clone the project from GitHub to the server.

# Create virtual environment
mkdir -p $PROJECT_BASE_PATH/env
python3 -m venv $PROJECT_BASE_PATH/env

# Install python packages
$PROJECT_BASE_PATH/env/bin/pip install -r $PROJECT_BASE_PATH/requirements.txt   # Instalation based on application added to the requirements.txt.
$PROJECT_BASE_PATH/env/bin/pip install uwsgi==2.0.18                            # uWSGI is a Python deamon for running Python code as a webserver.

# Run migrations and collectstatic
cd $PROJECT_BASE_PATH
$PROJECT_BASE_PATH/env/bin/python manage.py migrate
$PROJECT_BASE_PATH/env/bin/python manage.py collectstatic --noinput             # collectstatic will gather all of the static files for all of the apps in our project into one dir.
                                                                                # Django does this automatically but since we are not using it on production we need to create
                                                                                # a location with all of the stitc files that we can use to serve the CSS and JavaScript for the
                                                                                # Django admin and the Django REST Framework browsable API.
# Configure supervisor - supervisor is a application on Linux that allows you to manage processes. This is what is going to manage our Python process or our uWSGI server.
cp $PROJECT_BASE_PATH/deploy/supervisor_profiles_api.conf /etc/supervisor/conf.d/profiles_api.conf  # Copy the supervisor profiles API config. into the location on the server
                                                                                                    # where supervisor is kept.
supervisorctl reread                                                            # To update these supervisor configuration files.
supervisorctl update                                                            # To update all the processes.
supervisorctl restart profiles_api                                              # Restart profiles API to make sure that our service is started.

# Configure nginx - this is the webserver that's going to be used to serve the static files.
cp $PROJECT_BASE_PATH/deploy/nginx_profiles_api.conf /etc/nginx/sites-available/profiles_api.conf   # Create a location for the configuration file and copy the configuration
                                                                                                    # file that we have added here to the sites available directory in NGINX.
rm /etc/nginx/sites-enabled/default                                             # Remove the default configuration.
ln -s /etc/nginx/sites-available/profiles_api.conf /etc/nginx/sites-enabled/profiles_api.conf       # Add a symbolic link from our sites available to our sitesenabled to enable our site.
systemctl restart nginx.service                                                 # Restart the NGINX service.

echo "DONE! :)"
