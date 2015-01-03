# Homestarkov

This is an in progress application to generate
[Homestar Runner](http://homestarrunner.com) character quotes using a
Markov Chain Generator trained on various characters' quotes.

## Installation

This program uses `flask`, `flask-cors`, `argparse`, and `PyMarkovChain`.

`pip install -r requirements.txt`

## Usage

Just run `python server.py`

## API

The server exposes a RESTful JSON API.

Endpoints are as follows:

### GET `/characters`

```json
[
  {
    "name": "Homsar",
    "path": "homsar",
    "tagline": "Legitimate Business!"
  },
  {
    "name": "Senor Cardgage",
    "path": "cardgage",
    "tagline": "Dump Tell No Mandy!"
  }
]
```

## Thanks

Special thanks to
[The Brothers Chaps](http://www.hrwiki.org/wiki/The_Brothers_Chaps)
for making such an amazing piece of internet history (and internet present!)

Special thanks, as well, to [hrwiki](http://hrwiki.org) user
[DorianGray](http://www.hrwiki.org/wiki/User:DorianGray) for his awesome
[compilation](http://www.hrwiki.org/wiki/User:DorianGray/Analysis_of_Senor_Cardgage%27s_Speech_Patterns)
of Senor Cardgage quotes.
