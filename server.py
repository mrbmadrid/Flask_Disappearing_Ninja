from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/<color>')
def ninja(color):
	valid_ninjas = ['blue', 'red', 'orange', 'purple']
	valid = False
	for ninja in valid_ninjas:
		if color.lower() == ninja:
			valid = True
	ninja = "static/img/"
	if valid:
		ninja += color.lower()+".jpg"
	else:
		ninja += 'notapril.jpg'
	return render_template('ninja.html', ninja=ninja)

app.run(debug=True)