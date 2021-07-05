from flask import Flask
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

@app.route('/')
def app():
    return f'app running on {LOCALHOST}:{PORT}'

# listen for message from discord bot then grab the file from the stream or maybe just grab it off the file system of the discord bot

@app.route('/audio')
def audio():
    return 'we runnin'
