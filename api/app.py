# when you get model pribabilities, make 0.4-0.6 into NEUTRAL
# freeze requirements.txt
# use aws hosting for model if possible
# make model pipeline if needed
# finish readme
# remove old strategy from notebook

from flask import Flask, render_template
import pickle

app = Flask(__name__)

with open("clf.pkl", "rb") as f:
    clf = pickle.load(f)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run()