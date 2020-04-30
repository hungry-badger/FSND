# Introduction

This Capstone is the final project of the Udacity Full Stack Nano Degree (FSND) program. I enrolled in the program to get an introduction and practical experience in working with databases, API's, cyber securtiy and automated deployment & testing of systems. This is the start to refresh my technical skills and is a great foundational program that has put me on the right course.

The Capstone project requires a developer to utilise all the skills and experience they have acquired in a single program. The skills I have acquired include:
* SQL and Data Modelling for the Web
* API Development and Documentation
* Identity and Access Management
* Server Deployment, Containerization and Testing

I have enjoyed the program, as it was challenging enough to also be rewarding, but simultaneously none of the challenges were unsurmountable as their sufficient support to overcome them.

# Overview

This project consists of the foundations of any business and captures both Client and Product information. Different user profiles are allowed to create, read, update and delete required respective Client and Product records.

# Tech Stack

The tech stack consists of:

* **SQLAlchemy ORM** is the Object Relational Mapping (ORM) library of choice
* **PostgreSQL** is the database type
* **Python3** and **Flask** is the server language and server framework
* **Flask-Migrate** for creating and running schema migrations
* **FLASK CORS** is the extension to handle cross origin requests from a frontend server. 
* **UnitTest** is used for endpoint testing and error behaviour
* **Auth0** used to authenticate user and provide Role Base Access Access Control (RBAC)
* **Heroku**  the cloud platform where the application and database is hosted
* **gunicorn** is a pure-Python HTTP server for WSGI applications. The applications are deployed using the Gunicorn webserver.

# RBAC controls

There are 3 types of access relevant to the API Server. Where required, respective authentication tokens that are currently active is also provided:
* **Public** is accessable without any token

* **Client** is accessable with a token. This user type is able to:
    - "get:products" to view all products
    - "delete:clients" to delete their record
    - "patch:clients" to update their record
    - "post:clients" to create a client record

    A currently active **Client** Auth0 token ([**client_token**]) is: [```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkdaOGJ6anR4RVpyQ2gwY0V2OHJuVCJ9.eyJpc3MiOiJodHRwczovL25pY2guZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYTdhZDY1NmM4ZWIyMGMxNTM0OWUxZCIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNTg4MjM2NTgxLCJleHAiOjE1ODgzMjI5ODEsImF6cCI6IkdSaHRWSk9KZm5aQjZZMmRMUnhWdERzR05IOElMS3pIIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Y2xpZW50cyIsImdldDpwcm9kdWN0cyIsInBhdGNoOmNsaWVudHMiLCJwb3N0OmNsaWVudHMiXX0.oXY9NJL-2Qh4VYMN4r7jCvjqhzs9YVcQrVtfBj6wcPOOHgQmdMkEck4e_s96I9X2ACWNWdujfXEQTA6jB8YmFwJeV54KyfrMCEE8T-J6GLVxd_0wJ_PlFskP23Px3E0569lo-L6K8TKjVikY43m72W05yk6OKmq1c7tXjaCOU6adRvhH1CEuPGnrn4HJoxkC2byLcuqSLEIgEykQYsgJ-GyjrAPHh_wwEGKnFU8FBkm-xJaXSy8YZZlLPNSj_aI-MLj0bebwDSaDSYRBi96NFR7gzI7xgc-Nv0Rht8AOoO6LMf7BmuybAHhHEoSesOJxJaaCxs818z-kk8dfegK1UA```]

* **Administrator** is accessable with a token. The user type is able to:
    - **"delete:clients"** to remove client records
    - **"delete:products"** to remove products
    - **"get:clients"** to access all client records
    - **"get:products"** to view all products
    - **"patch:clients"** to update a client record
    - **"post:clients"** to create a client record
    - **"post:products"** to create a new product

    A currently active **Administrator** Auth0 token ([**admin_token**]) is: [```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkdaOGJ6anR4RVpyQ2gwY0V2OHJuVCJ9.eyJpc3MiOiJodHRwczovL25pY2guZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYTdhZWRkY2YxOTBmMGMwZjZlNDBkNCIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNTg4MjM2NDgxLCJleHAiOjE1ODgzMjI4ODEsImF6cCI6IkdSaHRWSk9KZm5aQjZZMmRMUnhWdERzR05IOElMS3pIIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Y2xpZW50cyIsImRlbGV0ZTpwcm9kdWN0cyIsImdldDpjbGllbnRzIiwiZ2V0OnByb2R1Y3RzIiwicGF0Y2g6Y2xpZW50cyIsInBhdGNoOnByb2R1Y3RzIiwicG9zdDpjbGllbnRzIiwicG9zdDpwcm9kdWN0cyJdfQ.CkNcmci1zBUfGepaHva-q8n1jEa7EOJmv4n4CArwEk1EKIk_tyZCBuC7380Id2vIvoGi05909L9UqCBk6RSybJNh4IxjxCt-M6ByPpHTaeKpGXX3qeWhtrm7c7RiK_35gF6RgdvFQh50nlWb2BtrvnZYzZr-qqcmoUvpN5keVHqWVecfocxjrNZqL7MQZbVDL6sqbIHa7_F-FEyQ2J7ufX0zOG4-QXJLFno92AI20TxWp69VeSPwhUk5kgsOgBuDS9X7OUvQWo07nrpq7ZlbsvNCaX9J24w9BLPim18edbOQvGGHS6Z7ctjOCYjCocNrsjsYQv57i8DuF-6NrGoneQ```]

# API 
The project API's can be accessed at the URL: ```https://nich-capstone-app.herokuapp.com/``` 

## API Parameters

### Client parameters
The following input parameters are required for a client record:
* ***first_name*** is a string that contains the first name of a client
* ***surname*** is a string that contains the surname of a client
* ***id_number*** is a unique string that contains the identity number of the client
* ***email*** is a string that contains the email address of the client
* ***phone*** is a string that contain the phone number of a client

### Product parameters
The following input parameters are required for a client record:
* ***name*** is a string that is the name of the product
* ***description*** is a string that describes the product
* ***price*** is a float of a single unit of the product

## Test Server API
Public endpoint to check whether the server is running.

From your Command Line Interface, run:
```curl --location --request GET 'https://nich-capstone-app.herokuapp.com/'```

Expect Response:
['Welcome to the JUNGLE!!!']

## View Clients API
GET endpoint to view all clients that is only accessable by an Administrator user.

### CURL
From your Command Line Interface, run:
```
curl --location --request GET 'https://nich-capstone-app.herokuapp.com/clients' \
--header 'Authorization: Bearer [**admin_token**]' 
```

### Expected Response:
[Welcome to the JUNGLE!!!]

## Create client API
POST endpoint to create a client record that is only accessable by an Administrator or Client user.

### CURL

From your Command Line Interface, run:
```
[url --location --request POST 'https://nich-capstone-app.herokuapp.com/clients' \
--header 'Authorization: Bearer [**admin_token** or **client_token**] \
--header 'Content-Type: application/json' \
--data-raw '{
    "first_name": "Sachin",
    "surname": "Tendulkar",
    "id_number": "7604170299087",
    "email": "sachin@tendulkar.com",
    "phone": "0823330902"
}'
```

### Expected Response:
{
  "client": {
    "email": "sachin@tendulkar.com",
    "first_name": "Sachin",
    "id": 114,
    "id_number": "7604170299087",
    "phone": "0823330902",
    "surname": "Tendulkar"
  },
  "status_code": 200,
  "success": true
}


## Update client record API
PATCH endpoint to update a client record that is only accessable by an Administrator or Client user. 

The ID of the specific client to be updated must be provided ('5' in the CURL instruction below). This is accesable\
by running a 'Client GET' request or when a Client user created their profile.

### CURL
From your Command Line Interface, run:
```
curl --location --request PATCH 'https://nich-capstone-app.herokuapp.com/clients/5' \
--header 'Authorization: Bearer [**admin_token** or **client_token**] \
--header 'Content-Type: application/json' \
--data-raw '{
    "id_number": "1104270179088"
}'
```

### Expected Response:
{
  "client": {
    "email": "sachin@tendulkar.com",
    "first_name": "Sachin",
    "id": 114,
    "id_number": "1104270179088",
    "phone": "0823330902",
    "surname": "Tendulkar"
  },
  "status_code": 200,
  "success": true
}


## Delete client record
DELETE endpoint to remove a client record that is only accessable by an Administrator or Client user. 

The ID of the specific client to be updated must be provided ('5' in the CURL instruction below). This is accesable\
by running a 'Client GET' request or when a Client user created their profile.

### CURL
From your Command Line Interface, run:
```
curl --location --request DELETE 'https://nich-capstone-app.herokuapp.com/clients/5' \
--header 'Authorization: Bearer [**admin_token** or **client_token**]'
```

### Expect Response:
{
  "delete": {
    "email": "sachin@tendulkar.com",
    "first_name": "Sachin",
    "id": 114,
    "id_number": "1104270179088",
    "phone": "0823330902",
    "surname": "Tendulkar"
  },
  "status_code": 200,
  "success": true
}


## Product API's
Product API's are the same as the Client API's, except for:
* ***View Products*** is only accesable by registered Client and Administrator users.
* ***All other APIs*** (i.e. create, update, delete) is only accessable by Administrator users.

The respective parameter information must be provided as per the parameter section above. 

For the Product DELETE API, the deleted object is not returned, only whether the status and success of the operation.

# Main Files: Project Structure

  ```sh
  ├── README.md
  ├── ```app.py``` the main driver of the app
  ├── ```auth.py``` enforces RBAC on users 
  ├── ```Auth0 Tokens.rtf``` is a folder with links to the Auth0 page to register and setup user tokens
  ├── ```manage.py``` runs respective database migrations on Heroku
  ├── ```models.py``` contains the setup of the SQL Alchemy models
  ├── ```Procfile``` contains a list of process to automatically execute within the app on Heroku
  ├── ```README.md``` is this file you are reading
  ├── ```requirements.txt``` contains the dependencies we need to install with ['$ pip3 install -r requirements.txt']
  ├── ```setup.sh``` contains respective configuration variables that is required by Heroku
  ├── ```test_flaskr.py``` contains tests for success and error behaviour. This can be run with the ['$ python3 test_flaskr.py'] command
 ```


# Development setup

1. Understand the Project Structure (explained above) and where important files are located.

2. Setup your Auth0 server to create tokens and RBAC. The require authorisations and access control is contained within the app.py file.

3. Build and run local development following the Development Setup steps below.
    3.1. Initialize and activate a virtualenv:
    ```
    - $ cd YOUR_PROJECT_DIRECTORY_PATH/
    - $ virtualenv --no-site-packages env
    - $ source env/bin/activate
    ```

    3.2. Install the dependencies:
    ```
    - $ pip3 install -r requirements.txt
    ```

    3.3. Inital setup on local server
        
    Create your database and migrations locally, before upgrading migrations to Heroku. Make sure your SQLALCHEMY_DATABASE_URI is set to a local database, e.g. postgres://localhostname@localhost:5432/herokutest and you've already created the database this local address points to.

    The models.py and test_flaskr.py files need to be updated where the SQLALCHEMY_DATABASE_URI and database_path need to be updated accordingly
        

    3.4. Setup the local database migration files by running manage.py 
    ```
    - $ python3 manage.py db init
    - $ python3 manage.py db migrate
    - $ ptyhon3 manage.py db upgrade
    ```
    
    3.5 Run the development server:
    ```
    - $ export FLASK_APP=app.py
    - $ export FLASK_ENV=development # enables debug mode
    - $ python3 -m flask run
    ```

    3.6. Navigate to Home page [**http://localhost:5000**] and test the functionaliy

4. Deploy Server to Heroku
    
    4.1 Assuming all is well and you can see you migration file in migrations/versions, run either ```$ python3 manage.py db upgrade``` or ```$ flask db upgrade```, again, depending on your setup

    4.2 Create your app in Heroku. Run ```$ heroku create name_of_your_app```. The output will include a git url for your Heroku application. Copy this as, we'll use it in a moment.

    4.2 You are now ready to migrate your database to Heroku. Change the SQLALCHEMY_DATABASE_URI to a variable that is in a Postgres database on Heroku, i.e. DATABASE_URL. You can check your environment variables in Heroku by going to Settings>Config Vars and then clicking "Reveal Config Vars."

    4.3 Add git remote for Heroku to local repository. Using the git url obtained from the last step, in terminal run: ```$ git remote add heroku heroku_git_url```.

    4.4 Add postgresql add on for our database
    Heroku has an addon for apps for a postgresql database instance. Run this code in order to create your database and connect it to your application: 
    ```$ heroku addons:create heroku-postgresql:hobby-dev --app name_of_your_application```

    4.5 Run ```$ heroku config --app name_of_your_application``` in order to check your configuration variables in Heroku. You will see DATABASE_URL and the URL of the database you just created. That's excellent, but there were a lot more environment variables our apps us

    4.3 Push your changes to your git repository.

    4.4 Push your changes to Heroku with the command ```$ git push heroku master```

    4.5 Run the command, ```$ heroku run python3 manage.py db upgrade --app name_of_your_app```
    
    If you receive no errors, after running the command above, you should be able to see your table schema by navigating, in the Heroku UI, to Resources, and clicking on Heroku Postgres. Navigate to Dataclips>Create Dataclips and your table schema from you migration will appear on the left hand side.

# Testing
[```test_flaskr.py```] contains tests for success and error behaviour. 

This can be run with the [```$ python3 test_flaskr.py```] command. 

# Author
The Hungry Honey Badger... 

# Acknowledgements
I enjoyed the Udacity Full Stack Development course. 

Credits to all the respective teachers, mentors and colleagues who assisted in the course.