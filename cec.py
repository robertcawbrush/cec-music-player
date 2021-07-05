import os
from flask import Flask
from dotenv import load_dotenv, dotenv_values

app = Flask(__name__)

load_dotenv()

config = dotenv_values(".env")

SERVER_URL = config['SERVER_URL']
PORT = config['PORT']

@app.route('/')
def index():
    return f'CEC music player is running'

# listen for message from discord bot then grab the file from the stream or maybe just grab it off the file system of the discord bot

@app.route('/audio')
@app.route('/audio/<file_name>')
def audio(file_name=None):
    if file_name:
        return f'the file you provided is {file_name}'
    return 'we runnin'

