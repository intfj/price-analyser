from flask import Flask, request, jsonify
from scraper import scrape_all_marketplaces
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/scrape", methods=["POST"])
def scrape():
    data = request.get_json()
    product = data.get("product")
    url = data.get("url")
    condition = data.get("condition")
    margin = data.get("margin")
    marketplaces = data.get("marketplaces", [])

    result = scrape_all_marketplaces(product, url, condition, margin, marketplaces)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
