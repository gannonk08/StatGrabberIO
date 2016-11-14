# StatGrabber

StatGrabber is a python based webscrapper API that only needs a URL to return JSON formatted statistics, currently scores are returned

## Setup

1. Fork/Clone
1. Create and activate a virtualenv
1. Install dependencies

## Run

```sh
$ python espn_app.py
```

Then send a POST request in a new terminal window:

```sh
$ http POST http://localhost:5000/data spider=espn_crawler url=http://www.espn.com/nfl/game\?gameId\=400874553
```
