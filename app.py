import os
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Gemini API Configuration (Railway ke Environment Variables se key uthayega)
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "YAHAN_APNI_API_KEY_DAALEIN")
genai.configure(api_key=GEMINI_API_KEY)

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
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            return render_template_string(f.read())
    else:
        return "index.html file nahi mili!"

@app.route('/get_topics', methods=['POST'])
def get_topics():
    data = request.json
    niche = data.get('niche', 'Tech')
    topics = TRENDING_TOPICS.get(niche, ["General Tech Trend 1", "General Tech Trend 2"])
    return jsonify({"topics": topics})

@app.route('/generate_script', methods=['POST'])
def generate_script():
    data = request.json
    topic = data.get('topic', 'Tech Trends')
    
    try:
        # Gemini Model initialize karein
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Create an engaging, viral YouTube video script for the topic: '{topic}'. Include a strong hook, main body points, and a call to action."
        
        response = model.generate_content(prompt)
        script_text = response.text
    except Exception as e:
        script_text = f"Script generate karne me error aayi: {str(e)}"
        
    return jsonify({"script": script_text})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
  
