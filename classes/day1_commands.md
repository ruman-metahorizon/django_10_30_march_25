# Basic Commands
git clone repo_url
cd project_name

python --version  # check python version
pip --version     # check pip version

pip freeze    # to check already installed library 

pip install virtualenv

virtualenv venv  # virtualenv env_name

Ubuntu: source venv/bin/activate
Windows: source ./venv/Scripts/activate

deactivate

## Django Started

pip install django

django-admin startproject project_name # project_name = blogs

python manage.py runserver

django-admin startapp boards