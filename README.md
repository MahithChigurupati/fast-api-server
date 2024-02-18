# fast-api-server

This is a basic FastAPI server implemented using JWT OAuth2.0 and postgres SQL via `sqlalchemy` ORM.

## Instructions to run the project

- If you have docker installed, follow below steps for Running the application on Docker

```bash
docker-compose up --build
```

- If you want to run it locally, follow below steps

```bash
# clone the repository
git clone git@github.com:MahithChigurupati/fast-api-server.git

# move to fast-api-server directory
cd fast-api-server

# create environment
python -m venv env
source env/bin/activate

# install dependencies
pip install -r requirements.txt

# create DB
psql -U <your-username> -c "CREATE DATABASE fastApiServer;"

# start the server
uvicorn main:app --reload

# visit the link for API docs
http://127.0.0.1:8000/docs
```
