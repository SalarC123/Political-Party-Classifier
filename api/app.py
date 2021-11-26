# AWS hosting
# mobile styling
# host website on pythonanywhere and netlify

from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

root = os.path.dirname(os.path.abspath(__file__))
pickle_file = os.path.join(root, "pipe.pkl")

with open(pickle_file, "rb") as f:
    pipe = pickle.load(f)

@app.route("/")
def home():
    return render_template("home.html", results={})

@app.route("/predict", methods=["GET", "POST"])
def make_prediction():
    text = request.form.get("text-input")
    if request.method == "POST":
        conservative_probability, liberal_probability = pipe.predict_proba([text])[0]
        if conservative_probability >= 0.6:
            party = "Republican"
        elif conservative_probability <= 0.4:
            party = "Democrat"
        else:
            party = "Neutral"

        # converts decimal probabilities to percents
        conservative_percent = str(round(conservative_probability*100, 2)) + "%"
        liberal_percent = str(round(liberal_probability*100, 2)) + "%"

        results = {
            "Political Party": party,
            "Conservative": conservative_percent,
            "Liberal": liberal_percent
        }

        return render_template("home.html", results = results)
    else:
        return

if __name__ == "__main__":
    app.run()