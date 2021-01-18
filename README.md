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

![Git Data Transport Commands](https://i.stack.imgur.com/Mqs0a.png)

# Creating Vagrant file
(to have local development server that we can use to run and test API)

1. type *vagrant init ubuntu/bionic64* to initialize the project with vagrant file
   and it bases it on ubuntu bionic64 base image.

# Set up Vagrant box

1. by editing Vagrant file customize development server,
2. set system, version, network, add Python to the machine.

# Run and contact to the server

1. run *vagrant up* in the terminal (VirtualBox needed) to create virtual machine,
2. run *vagrant ssh* to connect to the server by ssh protocol.


To access project files go to Vagrant directory on virtual machine by typing *cd /vagrant*
in terminal while connected to the server.
We can add Python program to the project and run it on vm by typing *python __file_name.py__*.



# Profiles REST API

Profiles REST API course code.
