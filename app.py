from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

ADS_B_API_URL = "https://opensky-network.org/api/states/all"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/adsb')
def adsb_feed():
    """Fetch ADS-B data from the OpenSky Network API.
    In a restricted environment this will fail, so consider
    replacing with a local data source."""
    try:
        resp = requests.get(ADS_B_API_URL, timeout=5)
        resp.raise_for_status()
        return jsonify(resp.json())
    except Exception as exc:
        return jsonify({'error': str(exc)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
