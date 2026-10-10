import os
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

TRENDING_TOPICS = {
    "Tech": [
        "Future of Artificial Intelligence in 2026", 
        "Top 5 Gadgets You Must Buy", 
        "How Python is Changing the World"
    ],
    "Finance": [
        "Smart Ways to Save Money", 
        "Crypto Market Trends", 
        "How to Start Investing with Low Income"
    ],
    "Motivation": [
        "Daily Habits of Successful People", 
        "How to Overcome Lazy Behaviour", 
        "The Power of Discipline"
    ]
}

@app.route('/')
def home():
    # Yeh code bina templates folder ke direct index.html ko padh lega
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            return render_template_string(f.read())
    else:
        return "index.html file nahi mili! Kripya check karein."

@app.route('/get_topics', methods=['POST'])
def get_topics():
    data = request.json
    niche = data.get('niche', 'Tech')
    topics = TRENDING_TOPICS.get(niche, ["General Tech Trend 1", "General Tech Trend 2"])
    return jsonify({"topics": topics})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
  
