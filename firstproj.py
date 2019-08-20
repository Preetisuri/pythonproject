from flask import Flask
app=Flask(__name__)
#app.config["DEBUG"]=True
#@app.route('/',methods=['GET'])
@app.route('/')
def home():
	return "<h1>My first flask project....</h1><br><h4>Got it</h4>"

app.run()
