from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")
	
@app.route("/more", methods = ["POST"])
def more():
	name = request.form.get("name")
	return render_template("more.html", name=name)
		
@app.route("/list")
def list():
	list=["one", "two", "three", "four", "five"]
	return render_template("list.html", list=list)
	
