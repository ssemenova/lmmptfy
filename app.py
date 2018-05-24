from flask import Flask, redirect, render_template
app = Flask(__name__)

@app.route("/")
def home():
	return render_template('main.html')

@app.route("/<command>")
def query(command):
	return render_template('main.html', command=command)
