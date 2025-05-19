# ADS-B Tracker Playground

This project provides a minimal Flask application that displays ADS-B data on a Leaflet map.

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the server:

```bash
python app.py
```

The application will attempt to fetch live data from the OpenSky Network API. In environments without internet access, the request will fail and return an error message.
