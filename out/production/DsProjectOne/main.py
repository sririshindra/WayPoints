from flask import Flask, render_template, url_for, flash, redirect, request
from forms import ReusableForm
import jsonGoogleMaps
from flask_googlemaps import
from flask_googlemaps import Map
app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

@app.route('/')
def my_form():

    food = {"testStrigification" : "buffaloNY"}

    return render_template("testpolylinewithhtml.html", source="Buffalo", destination="newyork",food=food)

@app.route('/', methods= ['POST'])
def my_form_post():

    source = request.form['source']
    destination = request.form['destination']
    processed_text = source.upper() + destination.upper()
    print(processed_text)
    food = {"testStrigification": "buffaloNY"}
    return render_template("testpolylinewithhtml.html", source=source, destination=destination,food=food)


if __name__ == "__main__":
    app.run(debug=True)