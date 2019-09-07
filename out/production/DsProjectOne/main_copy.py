from flask import Flask, render_template, url_for, flash, redirect, request
from forms import ReusableForm
import json
app = Flask(__name__)


app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

@app.route('/')
@app.route('/home')
def index():
    return 'This is the home page %s ' % request.method



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = ReusableForm(request.form)
    # name=request.form['name']
    if form.validate():
        # Save the comment here.
        flash('Hello ' + str(form.source) + "  " + str(form.destination) )
    else:
        flash('All the form fields are required. ')
    return render_template('hello.html', form=form)





@app.route('/abc')
def my_form():

    food = {"testStrigification" : "buffaloNY"}

    return render_template("testpolylinewithhtml.html", source="Buffalo", destination="newyork",food=food)

@app.route('/abc', methods=['POST'])
def my_form_post():
    source = request.form['source']
    destination = request.form['destination']
    processed_text = source.upper() + destination.upper()
    print(processed_text)
    food = {"testStrigification": "buffaloNY"}
    return render_template("testpolylinewithhtml.html", source=source, destination=destination,food=food)


@app.route('/bacon', methods=['GET', 'POST'])
def bacon():
    if request.method == "POST":
        return "you are using POST"
    else:
        return "you are using GET"



@app.route('/profile/<name>')
def profile(name):

    return render_template("profile.html", name=name)
    # return 'This is ' + name

@app.route('/test')
def test():

    return render_template("testpolylinewithhtml.html")
    # return 'This is ' + name

if __name__ == "__main__":
    app.run(debug=True)