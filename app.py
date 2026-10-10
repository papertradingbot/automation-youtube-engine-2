import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample Trending Topics
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
    return render_template('index.html')

@app.route('/get_topics', methods=['POST'])
def get_topics():
    data = request.json
    niche = data.get('niche', 'Tech')
    topics = TRENDING_TOPICS.get(niche, ["General Tech Trend 1", "General Tech Trend 2"])
    return jsonify({"topics": topics})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
  
