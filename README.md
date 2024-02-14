# Flask-Drinks-RestApi
The aim of this project is to implement REST API endpoints using Flask framework.<br/>
The project uses drinks and its company as example entities for demonstration.<br/>
Users can access the relevant endpoints to retrieve/modify the data.<br/>

Implementing with Flask-RESTX module will auto generate the Swagger file. <br/>
Project is dockerized to allow fast & easy deployment. 

## Features
* CRUD operations
* Swagger documentation
* Dockerization
  
## Technologies used
* Flask 
* Flask-RESTX
* Postgres
* Docker

## Setting up (only required for the first time - create the database tables)
#### Ensure docker engine is running before proceeding ####

1. **CD** to the folder containing the docker-compose.yaml file.
    - **docker-compose up -d**

![image](https://github.com/dude76vvv/flask-drinks-restApi/assets/131178280/119d2928-a735-47e2-91b0-20da4e008f80)

2. Enter into the running flask app container via interactive mode
    - **docker exec -it restdrinkspostgresdocker-flask_app-1 sh**

![image](https://github.com/dude76vvv/flask-drinks-restApi/assets/131178280/d5249891-800b-4ae0-a790-f171a10d6fbc)

3. Open flask shell using:
    - **flask shell**
  
4. Create the tables in the postgres using:
     - **db.create_all()**

![image](https://github.com/dude76vvv/flask-drinks-restApi/assets/131178280/fb0cb0f9-2b26-4f87-ae3d-084fd0e709dd)

5. Run **quit()** to leave flask shell
6. Run **exit** to leave the container shell

## Running
1. **CD** to the folder containing the docker-compose.yaml file.
    - **docker-compose up -d**

![image](https://github.com/dude76vvv/flask-drinks-restApi/assets/131178280/81601278-a556-45d0-a372-497206526b47)
  
## Screenshots

![image](https://github.com/dude76vvv/flask-drinks-restApi/assets/131178280/3bac9246-e518-4aee-b35b-4f8fdefaa299)

![image](https://github.com/dude76vvv/flask-drinks-restApi/assets/131178280/a3453a09-fc7f-4ea7-832f-ef0e2d3158a6)

![image](https://github.com/dude76vvv/flask-drinks-restApi/assets/131178280/183c0028-d213-4219-93eb-316aedb3a060)

![image](https://github.com/dude76vvv/flask-drinks-restApi/assets/131178280/861a36dd-ce96-44d6-bd63-94f3aa7848f2)

![image](https://github.com/dude76vvv/flask-drinks-restApi/assets/131178280/d1fd7d79-1b43-4b0e-9075-f05e8e2bbb52)

![image](https://github.com/dude76vvv/flask-drinks-restApi/assets/131178280/105ca0ce-c071-4fb5-af7c-d832db49dee2)









  
