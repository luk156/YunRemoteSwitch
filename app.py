from flask import Flask, render_template
import requests
from auth import requires_auth
app = Flask(__name__)


@app.route('/')
@requires_auth
def index():
    return render_template('index.html')


@app.route('/digital/read/<pin>')
@requires_auth
def digital_read(pin):
    # show the user profile for that user
    r = requests.get('http://root:arduino03@localhost/arduino/digital/' + str(int(pin)+3))
    return r.text


@app.route('/digital/write/<pin>/<status>')
@requires_auth
def digital_write(pin, status):
    # show the user profile for that user
    r = requests.get('http://root:arduino03@localhost/arduino/digital/' + str(int(pin)+3) + '/' + status)
    return r.text