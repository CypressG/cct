# Meetings API

This is an Internal API that handles booking of meeting rooms. It uses Basic Authorisation and SQLite3 (if you're looking   

# Requirements
 Python 3.8+

## Activating virtual environemnt 
Firstly, create your own virtual environment to encapsulate Python and it's dependanciens from global system:
```
python -m venv env
```

Afterwards activate environemnt:
## Choose the one that fits your Operating system and shell
| Platform      | Shell          | Command                              |
| --------------| ---------------|--------------------------------------|
| POSIX         | bash/zsh       | $ source <venv>/bin/activate         |
|               | fish           | $ source <venv>/bin/activate.fish    |
|               | csh/tcsh       | $ source <venv>/bin/activate.csh     |
|               | PowerShell Core| $ <venv>/bin/Activate.ps1            |
| Windows       | cmd.exe        | C:\> <venv>\Scripts\activate.bat     |
|               | PowerShell     | PS C:\> <venv>\Scripts\Activate.ps1  |


# Installation 

Install all the necessary requirements for this project by typing:

```
pip install -r requirements.txt
```
Access the folder where the manage.py file located: 

```
cd meetings
python manage.py makemigrations api user_manager
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

 This project is divided into two apps for more control (user_manager and api). User registartion can be conducted via admin panel. Gradually it would be worth it to implement sufficient registration form where admin can confirm or deny registration applicants. This function is not yet implemented in this project.    

# Additional tips and ideas
If you would like to move this project to production don't forget to place your SECRET_KEY inside of a separate file (ex. .env) and add it to .gitignore. For this project I intentionally left it out. It is higly suggested to move to more secure authorisation methods such as  (OAuth3 or jwt). 
  
## You can move this project from sqlite to postgres database
  
  To do so you need:
  1) Backup your data 
  ``` python manage.py dumpdata > datadump.json```
  2) ```pip install psycopg2```
  3) change your settings.py file To
  ```
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'NAME_OF_DB',
        'USER': 'DB_USER_NAME',
        'PASSWORD': 'DB_PASSWORD',
        'HOST': 'localhost',
        'PORT': 'PORT_NUMBER',
    }
}
  ```
  4) Load the data 
  ```
  python manage.py loaddata datadump.json

  ```
  5) migrate database 
  ```
  python manage.py makemigrations
  python manage.py migrate
  ```

  
## Linters and Formatting
The following project used black and flake8 packages. There is a small difference between linters they can be adjusted in pyproject.toml

# Other
There is also general logging included it writes specified material into general.log file. 

There are some unit tests generally they only check if you can create objects for fake information python library "Faker" was used
