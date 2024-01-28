# Basic documentation:

Since this repository is just a basic demonstration of Python, Django and Docker, this documentation will be simple and will contain some notes.

**Application Description:**

The application is a downright simple task manager that allows you to create, modify and delete individual tasks.  Each task has two mandatory parameters: name and description. It is also possible to specify the status of the task when creating it - if no status is specified, the default status CREATED will be added. All these three attributes, i.e. name, description and status are editable parameters. In addition to these parameters there are also non-editable parameters, namely creation time and completion time. The non-editable parameters are added and changed automatically and the user can only see and control their value indirectly (the completion time is based on the value set in the status).

**Description of each parameter of one REST API task:**

`name` - arbitrary name of the task (must be unique within the whole database)

`description` - an arbitrary description of the task
status - can take only three parameters, CREATED, INPROGRESS and COMPLETED

`creation_time` - non-editable datetime, automatically set value when the task is created

`completion_time` - non-editable datetime, an automatically set value based on the value of the status parameter

**Description of the methods used for the REST API:**
`GET` - used to retrieve all tasks or to retrieve one task (depending on the endpoint - root endpoint for all tasks and /task_id for one task [task_id must be an integer and must exist])

`POST` - used to create only one task

`PUT` - used only to change/update one task

`DELETE` - used only to delete one task

**How to work with the application:**
The application is prepared only as a REST API server, so in order to create, read and modify tasks it is necessary to use some HTTP client - browser, curl, Python requests lib, ... 
All endpoints communicate using JSON format.

However, it is also possible to use Django administration, through which it is also possible to control the application directly via the web interface. For this purpose, an admin account **skip_pay** with password **skip** was created.

**Tests:**
Basic tests are created for the application to test the functionality of the application.
If you want to run the tests, run the following command in the manage.py directory:

`python manage.py test`

**How to work with the application using curl:**
```
curl -X POST -H "Content-Type: application/json" \
    -d '{"name": "new name, "description": "some desc"}' \
    127.0.0.1:8000
```

This command creates a new task and saves it to the database. The best way to find out how to proceed for other http methods is to check the tests (api/tests.py), where all the possibilities of the API itself are tested.

**How to start an application server with REST API:**
There are many ways to run an application. The recommended way is using the Docker container technology and using the docker-compose tool with a command (the command assumes you are in the root directory, or wherever the docker-compose.yml file is):

`docker-compose up -d`

Nowadays it is more modern to drop containers using the podman tool, and there is also an equivalent podman-compose tool with the same parameters as the Docker version:

`podman-compose up -d`

Another way to run the server is directly from Python, ideally using a virtual environment (the following commands assume a Linux operating system, commands vary slightly on other systems):
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

**NOTE:**
This documentation is really only a sample and therefore not exhaustive (actually it is written in a quick "first time" ;-) ).
