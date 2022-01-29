# Meetings API

This is an Internal API that handles booking of meeting rooms. 

# Activating virtual environemnt 
Firstly, create your own virtual environment to encapsulate Python and it's dependanciens from global system:
```
python -m venv env
```

Afterwards activate environemnt:
## Linux/Ubuntu
```
source env/bin/activate
```
## Windows

## Mac


# Installation 

Install all the necessary requirements for this project by typing:

```
pip install -r requirements.txt
```
Access the folder where the manage.py file located: 

```
cd meetings
python manage.py makemigrations
python manage.py migrate
```

Create your own super user by typing:

```
python manage.py createsuperuser
```
And run the server:
```
python manage.py runserver
```
or
```
./manage.py runserver
```


# Database structure
![Database ER diagram](https://github.com/CypressG/cct/blob/master/Documentation/database.png?raw=true)


# Moving towards production
If you would like to move this project to production don't forget to place your SECRET_KEY inside of a separate file (ex. .env) and add it to .gitignore. For this project I intentionally left it out.

## Linters 
The following project used black and flake8 packages.
