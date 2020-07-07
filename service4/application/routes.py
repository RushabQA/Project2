from flask import Flask, render_template
from application import app
import requests
import string


@app.route('/', methods=["GET","POST"])
def combine():
    workout = requests.data.decode('http://service2:5001')
    playlist = requests.data.decode('http://service3:5002')
    if workout == 'walk':
        playlist = "chilled"
    elif workout == 'run':
        playlist = "upbeat"
    elif workout == 'swim':
        playlist = "motivation"
    elif workout == 'cycle':
        playlist = "throwback"
    elif workout == 'yoga':
        playlist = "instrumental"
    elif workout == 'hiit':
        playlist = "zumba"
    elif workout == 'boxing':
        playlist = "rap"
    else:
        playlist = "hiphop"
    return "Your workout is" + workout + "and your playlist is " + playlist + "!"