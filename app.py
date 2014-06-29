from flask import Flask, jsonify, abort, request, make_response, url_for, render_template
from flask.ext.httpauth import HTTPBasicAuth
#from mongo.connection import DB
import json

"""
------------=------------=------------=------------=------------
DO NOT MESS WITH THIS STUFF
------------=------------=------------=------------=------------
"""
# basic flask stuff
app = Flask(__name__, static_url_path = "")

# some globals for the information
API_VERSION = 1.1
API_NAME = "buffalo"
API_AUTHOR = "Barry Sagittarius"


# some wrappers around auth to redifne how it works. auth should be better, but for now \
#   it's going to be a simple implementation. Let's revist it when it's all good to go.
#
# when writing new routes, just decorete them with @auth.login_required and it will check \
#   for the basic username and password defined below.


auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'barry':
        return 'sagittarius'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify( { 'error': 'Unauthorized access' } ), 403)
    # doing a 403 instead of 401 to get rid of that ugly browser window infinite loop
    # because thats just annoying as shit and i presonally don't like that.
    
@app.errorhandler(400)
def not_found(error):
    # nothing too fancy here, just making the response a json error
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    # nothing too fancy here either, just making the response a json error
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

"""
------------=------------=------------=------------=------------
FEEL FREE TO MESS WITH THIS STUFF
------------=------------=------------=------------=------------
"""
# here is where we actually create the routes and the functions that do stuff. It is    \
#   separated into two parts. API calls and HTML calls. This is to keep it easy to read.\
#   try and create external files and include them later on for stuff that does heavy   \
#   lifting. This will keep the app.py size down for readability.

@app.route('/api/info', methods = ['GET'])
def api_info():
    return jsonify( {
        'name': API_NAME,
        'version': API_VERSION,
        'author': API_AUTHOR
        })

@app.route('/api/product/<game_id>/funnel', methods = ['GET'])
def game_funnel(game_id):
    return jsonify( {
        'status': 'ok',
        'game': game_id
        })

# boot this thing
if __name__ == '__main__':
    app.run(debug = True)