# Capstone Project


# Introduction
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies.


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

2) DELETE /movies/{id}
Delete movie by id.

3) POST /movies
Add one movie to the database.

4) PATCH /movies/{id}
Make changes to an exsting movie by id.

5) GET /actors
Can get all actors.

6) DELETE /actors/{id}
Delete actor by id.

7) POST /actors
Add one actor to the database.

8) PATCH /actors/{id}
Make changes to an exsting actor by id.

9)GET /auth
Get the URl to log in 



# Roles:
- There are three different roles in the application as described below:
    # Casting assistant
        View movies and actors
        email: test-assistant-1234@movies.com
        password: test-assistant-1234

    # Casting producer
        All permissions a Casting Assistant has and…
        Add or delete or modify an actor or movie from the database
        email: test-producer-1234@movies.com
        password: test-producer-1234


# Tests:
    One test for success behavior of each endpoint
    One test for error behavior of each endpoint

- Put the token in test_app.py *****


# Dependencies
You can install the dependencies using:

```bash
pip install -r requirements.txt
```



