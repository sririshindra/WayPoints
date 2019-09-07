from flask import Flask, render_template, request
from Controller import get_directions_and_weather
import Config

app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))


@app.route('/')
def my_form():
    """
    When the user loads the website the default page that will be loaded using this method.
    Gets the default directions and weather form buffalo to nyc.
    :return: html file that returns the default directions and weather information from Buffalo to nyc
    """
    points, center, points_polyline = get_directions_and_weather()
    waypoints_destination = {"waypoints": points, "center": center, "points_polyline": points_polyline,
                             "use_polyline": Config.use_polyline}
    return render_template("directions.html", source="buffalo", destination="nyc",
                           waypoints_destination=waypoints_destination)


@app.route('/', methods=['POST'])
def my_form_post():
    """
    when a user submits a waypoints request in the website a post call will be made which will be redirected to this
    method.
    Gets the directions and weather form source to destination submitted by the user.
    :return: html file that returns the directions and weather information from a given source to destination
    """
    source = request.form['source']
    destination = request.form['destination']
    points, center, points_polyline = get_directions_and_weather(source=source, destination=destination)
    waypoints_destination = {"waypoints": points, "center": center, "points_polyline": points_polyline,
                             "use_polyline": Config.use_polyline}
    return render_template("directions.html", source=source, destination=destination,
                           waypoints_destination=waypoints_destination)


if __name__ == "__main__":
    app.run(debug=False)
