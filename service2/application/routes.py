from flask import request, render_template, Response
from application import app
import requests
import random


@app.route('/', methods=['GET'])
def workout():
    workouts = ['walk', 'run', 'swim', 'cycle', 'yoga', 'hiit', 'boxing', 'weights']
    workout = workouts[random.randit(0,7)]
    return Response(workout, mimetype='text/plain')
