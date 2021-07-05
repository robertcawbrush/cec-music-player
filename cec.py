import os
from flask import Flask, render_template

from dotenv import load_dotenv, dotenv_values

app = Flask(__name__)

load_dotenv()

config = dotenv_values(".env")

SERVER_URL = config['SERVER_URL']
PORT = config['PORT']

@app.route('/')
def index():
    return 'We Runnin'

# listen for message from discord bot then grab the file from the stream or maybe just grab it off the file system of the discord bot

@app.route('/audio')
@app.route('/audio/<file_name>')
def audio(file_name=None):
    return render_template('music_player.html')

