from flask import Flask, render_template
app = Flask(__name__)
app.config['DEBUG'] = True
app.DEBUG = True

@app.route('/')
def hello(name=None):
    return render_template('index.html', name=name)

@app.route('/f')
def hellof(name="Filipe"):
    return ok()

@app.route('/led')
def ledchange():
	return render_template('led.html')

def ok():
    return render_template('hello.html')

