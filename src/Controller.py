"""
This file contains the necessary methods required to control the flow of information between google maps api,
weather api and the database.
"""
import googlemaps
import polyline
from pymongo import MongoClient
from datetime import datetime
import random
import requests
import math
import Config
import time

gmaps = googlemaps.Client(key=Config.google_api_key)
weather_api_key = Config.weather_api_key
client = MongoClient(Config.mongo_ip, Config.mongo_port)
db = client['waypoints']
waypoints_collection = db['waypoints']
weather_collection = db['weather']


def get_directions_and_weather(source="Buffalo, NY", destination="Fremont, CA"):
    """
    This method gets the directions from  a given source and destination from the google maps api.
    It then decodes the polyline to get the list of latitudes and longitudes of the waypoints between source and
    destination.
    It then selects about five waypoints from the list of all waypoints using a custom algorithm.
    The latitudes and longitudes of  selected waypoints are used to call the weather api.
    The response from the weather api is then aggregated.
    Center of the map to be displayed is computed.
    Both directions and the weather api calls are cached in the mongodb database.  Before any api call is made
    Cache is checked and if the required data is not available in the cache then the api is directly used.

    :param source: Source city entered by the user. If Source is not provided default location is used
    :param destination: destination city entered by the user. If destination is not provided default location is used
    :return: returns a list of tuples where each tuple contains the latitudes, longitudes, weather of the waypoints
    between source and destination.
    """

    now = datetime.now()
    directions_result = None
    time_for_waypoints_db = 0
    cost_for_directions_api =0
    if Config.cache_directions:
        start = time.clock()
        directions_result = waypoints_collection.find_one({"source": source.lower(),
                                                           "destination": destination.lower()})
        time_for_waypoints_db = time_for_waypoints_db + time.clock() - start

    # checking the cache for directions
    if directions_result is None:
        start = time.clock()
        directions_result = gmaps.directions(source, destination, mode="driving", departure_time=now)
        cost_for_directions_api = cost_for_directions_api + time.clock() - start
        # directions api call will be done internally by the gmaps.directions method.

        if Config.cache_directions:
            start = time.clock()
            waypoints_collection.insert({"source": source.lower(), "destination": destination.lower(),
                                         "directions": directions_result})
            time_for_waypoints_db = time_for_waypoints_db + time.clock() - start
    else:
        directions_result = directions_result['directions']

    print("time_for_waypoints_db is " + str(time_for_waypoints_db))
    print("cost_for_directions_api is " + str(cost_for_directions_api))
    points = polyline.decode(directions_result[0]['overview_polyline']['points'])

    center_lat = (max((x[0] for x in points)) + min((x[0] for x in points))) / 2  # latitude of map's center
    center_lng = (max((x[1] for x in points)) + min((x[1] for x in points))) / 2  # longitude of map's center
    center = (center_lat, center_lng, "random dummy content " + str(random.randint(1, 500)))
    _points = []

    time_for_weather_db = 0.0
    cost_for_weather_api = 0.0

    def add_points(point, time_for_weather_db, cost_for_weather_api):

        lat = round(point[0], 2)
        lon = round(point[1], 2)
        data = None
        if Config.cache_weather:
            start = time.clock()
            data = weather_collection.find_one({"coord.lat": lat, "coord.lon": lon})  # checking the cache for weather
            time_for_weather_db = time_for_weather_db + time.clock() - start

        if data is None:
            url = "http://api.openweathermap.org/data/2.5/weather?lat="+str(point[0])+"&lon=" \
                  + str(point[1]) + "&appid=" + Config.weather_api_key + "&units=imperial"
            start = time.clock()
            r = requests.get(url)  # weather api call.
            data = r.json()
            cost_for_weather_api = time_for_weather_db + time.clock() - start
            if Config.cache_weather:
                start = time.clock()
                weather_collection.insert_one(data)
                time_for_weather_db = time_for_weather_db + time.clock() - start
        else:
            pass

        _points.append((point[0], point[1],  str(data['name']) + " has current temperature of " +
                        str(data['main']['temp'])
                        + "\u00b0" + " F and a maximum " + str(data['main']['temp_max']) + "\u00b0" +
                        " F and a minimum of " + str(data['main']['temp_min']) +
                        " and the weather is predicted to have " + str(data['weather'][0]['description'] ) ))
        return time_for_weather_db, cost_for_weather_api

    a, b = add_points(points[0], time_for_weather_db, cost_for_weather_api)  # adding the source as a default
    time_for_weather_db = time_for_weather_db + a
    cost_for_weather_api = cost_for_weather_api + b

    i = 1
    modulo_number = math.floor((len(points) - 2)/6)  # custom logic to select waypoints
    for point in points[1:-1]:
        if i % modulo_number == 0:
            a ,b = add_points(point, time_for_weather_db, cost_for_weather_api)
            time_for_weather_db = time_for_weather_db + a
            cost_for_weather_api = cost_for_weather_api + b
        i = i + 1

    a ,b = add_points(points[len(points) - 1], time_for_weather_db, cost_for_weather_api)
    # adding the destination by default
    time_for_weather_db = time_for_weather_db + a
    cost_for_weather_api = cost_for_weather_api + b
    print("time_for_weather_db is " + str(time_for_weather_db))
    print("cost_for_weather_api is " + str(cost_for_weather_api))

    return _points, center, points
