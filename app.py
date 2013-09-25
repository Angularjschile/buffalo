from flask import Flask, request, Response, render_template, \
	session, g, redirect, url_for, abort
from functools import wraps

"""
DO NOT MESS WITH THIS STUFF
"""
# some basic http auth for now, use the @protected decorator on all public views
def check_auth(username, password):
    return username == 'admin' and password == 'juicy'

def authenticate():
    return Response(
    'Could not verify your access level for that URL.\n'
    'I needs them proper credentials amigo.', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def protect(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

"""
FEEL FREE TO MESS WITH THIS STUFF
"""
app = Flask(__name__)

@app.route('/')
@protect
def index():
    return render_template('index.html')

# boot this thing
if __name__ == '__main__':
	app.debug = True
	app.run()