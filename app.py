from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def gender():

    if request.method == "POST":

        gender = request.form["gender"]

        return f"Siz tanlagan jins: {gender}"

    return render_template("index.html")

app.run(debug=True)
