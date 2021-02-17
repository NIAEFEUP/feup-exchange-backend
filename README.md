# feup-exchange-backend

## Requirements
You should have:
- docker
- docker-compose

## How to run the server
The command docker-compose up in the same level as the yaml file should do it.
If you made changes to the dockerfiles or this is the first time running, you need
to build. This can be achieved with docker-compose build or docker-compose up --build.
After docker-compose up, voilá, you can start hitting the server with requests.
You can check the server address and port in terminal where you started the server.

## Insight on the structure
The source code is in the feup_exchange_backend folder.
As a regular developer who will not fiddle around with DevOps, you only need to know the
following: 
- urls.py file: Specifies exposed urls and calls view resources.
- views: These resources exist in the views folder. Each function created under a view class corresponds to a single url. A view's responsibility is to communicate with the controllers and return a response.
- controllers: The controllers handle all internal logic, that might be common to different
requests e.g., let's say there's an endpoint asking information about a user and another one asking about several. We can have a function that validates the user id is an integer as it should be. A controller does not communicate directly with the database, it communicates with models.
- models: These fellows interface the database tables and already have a predefined set of functions that make db querying a breeze.


