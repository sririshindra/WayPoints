## WayPoints
The purpose of the project is to display route from a source location to a destination location while also displaying the 
various waypoints along the route. When the user clicks on one of thee waypoints the temperature in that particular city is displayed.

## Motivation
The motivation behind the project is to learn the following.
1) Get used to building client-server systems. <br />
2) Working with APIs to distributed services. <br />
3) Working with the database. <br />
4) Understand and choose the web application stack. <br />


## Code style
PEP 8 for python

[![js-standard-style](https://img.shields.io/badge/code%20style-standard-brightgreen.svg?style=flat)](https://github.com/feross/standard)

## Tech/framework used
<b>Technologies used</b>
- [python](http://python.org) <br />
- [flask](http://flask.pocoo.org) <br />
- [mongodb](https://www.mongodb.com) <br />
- [docker](https://www.docker.com) <br />

<b>Built with</b>
- [Intellij IDEA](https://www.jetbrains.com/idea/) <br />

## Installation and setup
Provide step by step series of examples and explanations about how to get a development env running.

Open terminal <br />

<b>Install the necessary python packages</b> <br />
pip install pymongo <br />
pip install googlemaps <br />
pip install googlemaps <br />
pip install flask <br />

<b>Install docker in your system </b> <br />
https://docs.docker.com/install/  <br />
docker run -it -p 27017:27017  -d mongo  <br />
cd ProjectFolder/src  <br />
python createIndex.py  <br />


## Tests

Open terminal <br />
<b>In one tab do the following.</b> <br />
cd ProjectFolder/src  <br />
python main.py & <br />

<b>In another tab do the following.</b> <br />
curl "localhost:5000" > test.html. <br />
The curl call will display the time taken for the code to execute and will also return the html.<br />
This can be used to test the code with cache and without cache and see the difference.

## How to use?
Start the flask server <br/>
cd ProjectFolder/src  <br />
python main.py & <br />

To use the waypoints application simply go to the localhost:5000/ url and enter the source and destination in the textboxes. 
A vedio demo is included in the resources folder. <br />
![picture](resources/images/demo.png)

## Credits
The google waypoints example provided in the official documentation.
w3 schools for great html tutorials and reference.

## License
MIT © [rishi]()