from flask import Flask, request, jsonify
from model import CoronaTracker

app = Flask(__name__)
tracker = CoronaTracker()


# news endpoint : newsapi
@app.route("/news")
def get_corona_news():
    return jsonify({"articles" : tracker.articles})

if __name__ == "__main__":
    app.run(debug=True)
