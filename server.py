from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/<color>')
def ninja(color):
	valid_color=['red','blue','orange','purple']
	for ninja in valid_color:
		if color == ninja:
			return color
	return 'april'

app.run(debug=True)