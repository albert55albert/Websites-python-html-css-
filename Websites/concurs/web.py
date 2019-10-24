from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('home.html')

@app.route("/articles")
def articles():
	return render_template('articles.html')

@app.route("/informations")
def informations():
	return render_template('informations.html')

@app.route("/savetheworld")
def savetheworld():
	return render_template('savetheworld.html')

if __name__ == "__main__":
	app.run(debug = True)