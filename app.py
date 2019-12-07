from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
	return "<h1>Democracy Now! API</h1><p>This is a prototype API for the trusted news media company Democracy Now!</p>"

app.run()