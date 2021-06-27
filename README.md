# cec-music-player

Discord bot to interpret music files of .mp3 or wav (probably mp3 because of the 8mb file cap )

Bots in python extending discord python

The bot will listen for any audo file posted, then send the event and stream or just upload it to an http server that will host slugged urls such as http://DjRetard.mz/aef8k which will contain a web player  for that audio. 

## Dependencies
- discord py
- flask py
- sqlite
- fileserver hosted on Digital Ocean or something else
- a web player in C (TBD @finlay)
