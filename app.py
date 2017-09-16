from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/digital/read/<pin>')
def digital_read(pin):
    # show the user profile for that user
    r = requests.get('http://localhost/arduino/digital/' + (pin+3))
    return r.text


@app.route('/digital/write/<pin>/<status>')
def digital_write(pin, status):
    # show the user profile for that user
    r = requests.get('http://localhost/arduino/digital/' + (pin+3) + '/' + status)
    return r.text