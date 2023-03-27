## Address CRUD API

# steps to Setup the Project 

1. Setup virtual environment using `python3 -m venv env` in the base directory
2. install the requirements using command `pip install -r requirements.txt`
3. After successful installation you can start the fastapi server uvicorn `uvicorn main:app --reload`
4  Your API will be running at `http://127.0.0.1:8000` and forswagger UI navigate to `http://127.0.0.1:8000/docs`

Below are the API endpoints that are available to use 

1. `GET /address`
2. `GET /address/{id}`
3. `POST /address`
4. `PUT /address/{id}`
5. `DELETE /address/{id}`

Swagger UI

![image](https://user-images.githubusercontent.com/87128465/227924214-5dbb01d2-8acc-4103-bbcd-9d167934aa04.png)


Redoc

![image](https://user-images.githubusercontent.com/87128465/227924035-0653d2ad-47a8-4ad4-b833-cfb87dbf989e.png)
