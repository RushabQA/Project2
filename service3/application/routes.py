from flask import request, render_template, Response
from application import app
import requests
import random


@app.route('/', methods=['GET'])
def playlist():
    playlists = ['chilled', 'upbeat', 'motivation', 'throwback', 'instrumental', 'zumba', 'rap', 'hiphop']
    playlist = playlists[random.randit(0,7)]
    return Response(playlist, mimetype='text/plain')