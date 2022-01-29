# Meetings API

This is an Internal API that handles booking of meeting rooms. 

# Installation
Firstly, create your own virtual environment to encapsulate Python and it's dependanciens from global system.
```
python -m venv env
```

Afterwards activate environemnt
## Linux/Ubuntu
```
source env/bin/activate
```
## Windows

## Mac


Install all the necessary requirements for this project by typing:

```
pip install -r requirements.txt
```
Access the folder where the manage.py file located 

```
cd meetings
python manage.py makemigrations
python manage.py migrate
```

Create your own super user by typing:

```
python manage.py createsuperuser
```
And run the server
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
If you've would like to move your project to production don't forget to place you SECRET_KEY inside of separate file (ex. .env) and add it to .gitignore. For this project purpose i've left it out.
