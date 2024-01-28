Basic documentation:

Since this repository is just a basic demonstration of Python, Django and Docker, this documentation will be simple and will contain some notes.

Application Description:
The application is a downright simple task manager that allows you to create, modify and delete individual tasks.  Each task has two mandatory parameters: name and description. It is also possible to specify the status of the task when creating it - if no status is specified, the default status CREATED will be added. All these three attributes, i.e. name, description and status are editable parameters. There are also non-editable parameters, namely creation time and completion time. The non-editable parameters are added and changed automatically and the user can only see and control their value indirectly (the completion time is based on the value set in the status).

Description of each parameter of one REST API task:
name - arbitrary name of the task (must be unique within the whole database)
description - an arbitrary description of the task
status - can take only three parameters, CREATED, INPROGRESS and COMPLETED
creation_time - non-editable datetime, automatically set value when the task is created
completion_time - non-editable datetime, an automatically set value based on the value of the status parameter

How to work with the application:
The application is prepared only as a REST API server, so in order to create, read and change tasks, it is necessary to use some HTTP client - browser, curl, ... 
All endpoints communicate using JSON format.

However, it is also possible to use Django administration, through which it is also possible to control the application directly via the web interface. For this purpose, an admin account skip_pay with password skip was created.
