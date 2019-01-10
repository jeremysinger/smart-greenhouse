The web application is a Python3 Flask app. 
It binds to localhost:80 (default http port) when it runs.

The main landing page is an overview dashboard of the system, with 
latest sensor readings and other information.

There is also a set of http endpoints for web queries to get
JSON data values for sensor readings:

/temperature
/humidity
/light

all return JSON data.

Finally /download will download a CSV file of historic sensor data.


