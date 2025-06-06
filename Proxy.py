from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/api')
def proxy():
    try:
        url = "https://api.nobitex.ir/market/stats"
        headers = {'Content-Type': 'application/json'}
        payload = {
            "symbols": "usdt-irt,btc-irt,btc-usdt,eth-irt,eth-usdt,ada-irt,ada-usdt,xrp-irt,xrp-usdt,shib-irt,shib-usdt"
        }

        response = requests.post(url, headers=headers, json=payload)

        # بررسی پاسخ
        if response.status_code != 200:
            return jsonify({"error": f"Request failed with status {response.status_code}"}), 500

        data = response.json()

        if "stats" not in data:
            return jsonify({"error": "Missing 'stats' in response"}), 500

        return jsonify({"stats": data["stats"]})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
