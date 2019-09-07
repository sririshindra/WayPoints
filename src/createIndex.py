from pymongo import MongoClient, ASCENDING
import Config

client = MongoClient(Config.mongo_ip, Config.mongo_port)
db = client['waypoints']
waypoints_collection = db['waypoints']
weather_collection = db['weather']

weather_collection.create_index([('coord.lat', ASCENDING), ('coord.lon', ASCENDING)])
waypoints_collection.create_index([('source', ASCENDING), ('destination', ASCENDING)])
