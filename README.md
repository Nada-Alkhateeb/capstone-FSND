# Capstone Project


# Introduction
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies.

# Motivation 
This project is the last and combines most of the topics we have learned during the Full-stack nano-degree.this project goes through databases with Postgres, API with Flask, Authorization using Auth0, and finally deploying our application live via Heroku .


# Heroku:
URL: https://flask-movies-deploy.herokuapp.com/


# Database Models:
- Movies with attributes title and release date as shown below: 
    class movie(db.Model):  
        __tablename__ = 'movies'

        id = Column(Integer, primary_key=True)
        title = Column(String, nullable=False)
        release_date = Column(String)

- Actors with attributes name, age and gender, as shown below: 
    class actor(db.Model):
        __tablename__ = "actors"

        id = Column(Integer, primary_key=True)
        name = Column(String)
        age = Column(String)
        gender = Column(String)


# Endpoints:

1) GET /movies
Can get all movies.
Sample response output:
```
    {
        "movies": [
            {
                "id": 2,
                "release date": "1-5-2012",
                "title": "Who I am"
                },
                {
                    "id": 3,
                    "release date": "4-6-2018",
                    "title": "Dark"
                },
                {
                    "id": 5,
                    "release date": "11-3-1017",
                    "title": "Up"
                }
                        ],                 
        "success": true,
        "total": 3
}
```

2) DELETE /movies/{id}
Delete movie by id.
Sample response output:
```
{
    "delete": 5,
    "success": true
}
```

3) POST /movies
Add one movie to the database.
Sample response output:
```
{
    "movies": [
        {
            "id": 7,
            "release date": "11-3-2020",
            "title": "Cadaver"
        }
    ],
    "success": true
}
```

4) PATCH /movies/{id}
Make changes to an exsting movie by id.
Sample response output:
```
{
    "movie": {
        "id": 7,
        "release date": "11-3-2020",
        "title": "The Ouutpost"
    },
    "success": true
}
```

5) GET /actors
Can get all actors.
Sample response output:
```
{
    "actors": [
        {
            "age": "33",
            "gender": "F",
            "id": 1,
            "name": "hana"
        },
        {
            "age": "40",
            "gender": "M",
            "id": 2,
            "name": "Ja"
        }
    ],
    "success": true,
    "total": 2
}
```

6) DELETE /actors/{id}
Delete actor by id.
Sample response output:
```

{
    "delete": 1,
    "success": true
}
```

7) POST /actors
Add one actor to the database.
Sample response output:
```
{
    "actor": [
        {
            "age": "26",
            "gender": "F",
            "id": 5,
            "name": "Sara"
        }
    ],
    "success": true
}
```

8) PATCH /actors/{id}
Make changes to an exsting actor by id.
Sample response output:
```
{
    "actor": {
        "age": "24",
        "gender": "F",
        "id": 5,
        "name": "Sara"
    },
    "success": true
}
```

9)GET /auth
Get the URl to log in.
Sample response output:
```
{
    "auth_url": "https://fsnd-dom.us.auth0.com/authorize?audience=capstone&response_type=token&client_id=NDBBw6BIfDQQkhpKvWx294tcPNXudn72&redirect_uri=http://flask-movies-deploy.herokuapp.com/"
}
```



# Roles:
- There are three different roles in the application as described below:
    # Casting assistant
        Can view actors and movies
        email: test-assistant-1234@movies.com
        password: test-assistant-1234

    # Casting producer
        All permissions a Casting Assistant has and…
        Add or delete an actor from the database
        Modify actors or movies
        email: test-producer-1234@movies.com
        password: test-producer-1234

    # Casting Director
        All permissions a Casting Director has and…
        Add or delete a movie from the database
        email: test-director-1234@movies.com
        password: test-director-1234


# Tests:
    One test for success behavior of each endpoint
    One test for error behavior of each endpoint

- Put the token in test_app.py
To start the tests cd into the project foluder then type this command in terminal:
python test_app.py


# Dependencies

- Python 3.9.1
Follow instructions to install the latest version of python for your platform in the [python docs](https://www.python.org/downloads/)

- Virtual Environment
Instructions for setting up a virual enviornment for your platform can be found
in the python docs.
python -m venv venv
venv/bin/activate

- pip dependencies:
Install dependencies by naviging to the root directory and running:

```bash
pip install -r requirements.txt
```

- Local Database Setup
Once you create the database, open your terminal, navigate to the root folder, and run:

flask db init
flask db migrate -m "Initial migration."
flask db upgrade
After running, don't forget modify 'SQLALCHEMY_DATABASE_URI' variable.


## Running the server

Within the root directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```






