# let's say i wanted to create a note taking app for example
# So how i might create a note taking application where i want to be able to
# store different types of notes that people are typing in order to record notes
# and save notes on this website?

from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)

@app.route("/",methods=["GET", "POST"])
def index(): #default index route
	if session.get("notes") is None: #if i try and get the notes from the session and it doesnt exist, then i want session notes to be an empty list
		session["notes"] = [] #without the line above this, this line would overwrite my notes everytime i would try to add a new thing
	if request.method == "POST": #if the method is post
		note = request.form.get("note") #i want to access whatever note i wanted to add presumably
		session["notes"].append(note) #take this list of notes(line9) and add a new thing to the list, new note 
	return render_template("index.html", notes=session["notes"]) # otherwise if i didnt submit any data or even if i did, render index.html passing in my list of notes

# and so the advantage here is that now i have multiple different sessions going on
# such that this particular user is independent of the other particular users