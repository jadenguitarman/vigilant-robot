from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
	return "<p>Hi there! I'm the vigilant robot that runs this site. At the moment, I can't do much. But my creator is working with the Beryl programming language, Diffgram, and Zeit Now to give me more power. Soon, I'll be able to take over the...</p> <br> <h1>Connection Interrupted</h1> <br> <h2>Try again later.</h2>";
	
@app.route("/api/guess")
def guess():
	return "hi";