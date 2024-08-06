from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Retrieve the API key from the environment variable
GOOGLE_API_KEY = ' '

# Configure the Generative AI client
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the GenerativeModel with 'gemini-pro'
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    feedback = request.form['feedback']
    
    
    prompt = f"""
    You are a sentiment classification model. Refer to the below example and classify feedback into 'p' or 'n' category. Return only the category in the output.
    feedback: what a lovely product
    sentiment: p
    feedback: it is a waste
    sentiment: n
    feedback: {feedback}
    sentiment:
    """
    
    
    response = model.generate_content(prompt)
    sentiment = response.text.strip()
    
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
