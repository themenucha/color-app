import os
from flask import Flask
from flask import render_template
import socket
import random
import os
import requests
  

app = Flask(__name__)

color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "pink": "#be2edd",
    "yellow": "#ffff00",
    "white": "#ffffff",
    "purple": "#7d3c98"
}

color = os.environ.get('APP_COLOR') or random.choice(["red","green"])
#color = os.environ.get('APP_COLOR') or random.choice(["white"])
#color = os.environ.get('APP_COLOR') or random.choice(["pink","blue","yellow"])

@app.route("/")
def main():
    #return 'Hello'
    print(color)
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[color])
    # api-endpoint
    URL = "http://maps.googleapis.com/maps/api/geocode/json"
  
    # location given here
    location = "delhi technological university"

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'address':location}

    # sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)

    # extracting data in json format
    data = r.json()


    # extracting latitude, longitude and formatted address 
    # of the first matching location
    latitude = data['results'][0]['geometry']['location']['lat']
    longitude = data['results'][0]['geometry']['location']['lng']
    formatted_address = data['results'][0]['formatted_address']

    # printing the output
    print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
          %(latitude, longitude,formatted_address))


@app.route('/color/<new_color>')
def new_color(new_color):
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[new_color])

@app.route('/read_file')
def read_file():
    f = open("/data/testfile.txt")
    contents = f.read()
    return render_template('hello.html', name=socket.gethostname(), contents=contents, color=color_codes[color])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
