import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, movies,actors
from auth import AuthError, requires_auth, AUTH0_DOMAIN, API_AUDIENCE,CALL_BACK_URL,CLIENT_ID

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  db = setup_db(app)
  CORS(app)

  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers'
    ,'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods'
    ,'GET,PATCH,POST,DELETE,OPTIONS')
    return response

  @app.route('/')
  def hello():
    return 'Hello, World!'
    
  @app.route("/auth")
  def generate_auth_url():
    url = f'https://{AUTH0_DOMAIN}/authorize' \
      f'?audience={API_AUDIENCE}' \
        f'&response_type=token&client_id=' \
          f'{CLIENT_ID}&redirect_uri=' \
            f'{CALL_BACK_URL}'
            
    return jsonify({
      'auth_url': url
      })
      
  @app.route("/actors")
  @requires_auth("get:actors")
  def get_actors(token):
    AllActors = actors.query.all()
    
    return jsonify({
      'success': True,
      'actors': [Actor.format() for Actor in AllActors],
      'total': len(AllActors)
      })

  @app.route("/movies")
  @requires_auth("get:movies")
  def get_movies(token):
    AllMovies = movies.query.all()
    
    return jsonify({
      'success': True,
      'movies': [movie.format() for movie in AllMovies],
      'total': len(AllMovies)
      })
      
  @app.route("/actors/<int:id>", methods=['DELETE'])
  @requires_auth("delete:actors")
  def delete_actors(token,id):
    try:
      actor = actors.query.filter_by(id=actors.id).first()
      if not actor:
        abort(404)
      actor.delete()
      
      return jsonify({
        'success': True, 
        'delete': id}
        ), 200
        
    except BaseException:
      return jsonify({
        'success': False}
        ), 400
        
  @app.route("/movies/<int:id>", methods=['DELETE'])
  @requires_auth("delete:movies")
  def delete_movies(token,id):
    try:
      movie = movies.query.filter_by(id=movies.id).first()
      if not movie:
        abort(404)
        
      movie.delete()
      return jsonify({
        'success': True, 
        'delete': id}
        ), 200
    except BaseException:
      return jsonify({
        'success': False}
        ), 400
        
  @app.route("/movies/<int:id>", methods=['PATCH'])
  @requires_auth("patch:movies")
  def patch_movies(token,id):
    movie = movies.query.get(id)
    try:
      if not movie:
        abort(404)
        
      body = request.get_json()
      title = body.get('title', None)
      date = body.get('release_date', None)

      if title:
        movie.title = title

      if date:
        movie.release_date = date

      movie.update()
    # Allmovies = movies.query.all()

    except BaseException:
      abort(400)
      
    return jsonify({
      'success': True,
      'movie': movie.format()
      })
  
  @app.route("/actors/<int:id>", methods=['PATCH'])
  @requires_auth("patch:actors")
  def patch_actors(token,id):
    actor = actors.query.get(id)
    try:
      if not actor:
        abort(404)
      
      body = request.get_json()
      name = body.get('name', None)
      age = body.get('age', None)
      gender = body.get('gender', None)

      if name:
        actor.name = name

      if age:
        actor.age = age

      if gender:
        actor.gender = gender

      actor.update()
    # Allmovies = movies.query.all()

    except BaseException:
      abort(400)

    return jsonify({
      'success': True,
      'actor': actor.format()
      })

  @app.route("/actors", methods=['POST'])
  @requires_auth("post:actors")
  def post_actors(token):
    body = request.get_json()

    if body is None:
      abort(400)
    if 'name' not in body:
      abort(400)
    if 'age' not in body:
      abort(400)
    if 'gender' not in body:
      abort(400)
    
    name = body.get('name', None)
    age = body.get('age', None)
    gender = body.get('gender', None)
             
    actor = actors(name=name, age=age,gender=gender)
    actor.insert()
    actor = actors.query.filter_by(id=actor.id).first()

    return jsonify({
      'success': True,
      'actor': [actor.format()]
      })


  @app.route("/movies", methods=['POST'])
  @requires_auth("post:movies")
  def post_movies(token):
    body = request.get_json()

    if body is None:
      abort(400)
    if 'title' not in body:
      abort(400)
    if 'release_date' not in body:
      abort(400)
    
    title = body.get('title', None)
    date = body.get('release_date', None)
             
    movie = movies(title=title, release_date=date)
    movie.insert()
    movie = movies.query.filter_by(id=movie.id).first()

    return jsonify({
      'success': True,
      'movies': [movie.format()]
      })

  @app.errorhandler(401)
  def unprocessable(error):
    return jsonify({
      "success": False,
      "error": 401,
      "message": "Unauthorized"
      }), 401

  @app.errorhandler(404)
  def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Resource not found"
    }), 404

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": 'Bad Request'
    }), 400

  @app.errorhandler(AuthError)
  def auth_error(error):
    return jsonify({
        "success": False,
        "error": error.status_code,
        "message": error.error['description']
    }), error.status_code

  return app

app = create_app()

if __name__ == '__main__':
    app.run()