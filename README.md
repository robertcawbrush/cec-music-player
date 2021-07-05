# cec-music-player

Discord bot to interpret music files of .mp3 or wav (probably mp3 because of the 8mb file cap )

Bots in python extending discord python

The bot will listen for any audo file posted, then send the event and stream or just upload it to an http server that will host slugged urls such as http://DjRetard.mz/aef8k which will contain a web player  for that audio. 

CEC is the name of the server

## Dependencies
- discord py
- flask py
- sqlite
- file server hosted on Digital Ocean or something else AWS can be free 
- a web player in C (TBD @finlay)

## local development
you'll need each servr running on your own machine otherwise they wont be able to talk to one another

## virtual environment
most of the pain in python development comes from this

1. install python 3 at [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/), make sure the path to wherever you install python is in your path. nothing will work if you can't access
   python from powershell running `python --version`
1. on Windows, run `python -m venv ./venv/bin/activate`. On Linux/Darwin run `source ./venv/bin/activate`

when you are done developing either close the terminal or run `deactivate` the venv will provide this

## start the development server

we need to get flask running to serve the web side of the music player

1. python will have also installed `pip` which is pythons package manager, run `pip install -r requirements.txt`
1.in a command line such as cmd or powershell run `set FLASK_APP=hello.pyy` from the root of this folder, you should be able to see `cec.py` running `dir` this will tell flask what the entrypoint for the server is
1. run `flask run` should give you something like this `Running on http://127.0.0.1:5000/` don't close this terminal or you'll shutdown the server

## start the discord bot

we need the bot running in order to see the audio files and do something. make sure you run the dev server first because you need python to run it. 
you will also have the dependencies you need from running `pip install -r requirements.txt`

1. run 'python disco-cec.py'. should give you something like `discord bot is running on 127.0.0.1:3000`
1. don't close this terminal either as it will kill the bot

The bot will listen for any audo file posted, then send the event and stream or just upload it to an http server that will host slugged urls such as http://DjRetard.mz/aef8k which will contain a web player  for that audio. 
