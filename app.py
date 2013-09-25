from flask import Flask, request, Response, render_template, \
	session, g, redirect, url_for, abort
from functools import wraps

"""
DO NOT MESS WITH THIS STUFF
"""
# some basic http auth for now, use the @protected decorator on all public views
def _check_creds(username, password):
	return username == 'admin' and password == 'purple'

def _bad_creds():
	return Response(
		'Could not verify your access level for that URL.\n'
		'You have to login with proper credentials dawg', 401,
		{'WWW-Authenticate': 'Basic realm="Login Required"'})

def protected(c):
	@wraps(c)
	def decorated(*args, **kwargs):
		auth = request.authorization
		if not auth and not _check_creds(auth.username, auth.password):
			return _bad_creds()
		return c(*args, **kwargs)
	return decorated

"""
FEEL FREE TO MESS WITH THIS STUFF
"""
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# boot this thing
if __name__ == '__main__':
	app.debug = True
	app.run()