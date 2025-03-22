import google.generativeai as genai

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def chat(content):
    genai.configure(api_key="<YOUR_API_KEY_HERE>")
    model = genai.GenerativeModel(model_name='gemini-2.0-flash')
    response = model.generate_content(content)
    return response.text

# Sample response logic for chatbot
def get_bot_response(user_input):
    # This is a basic response logic. You can replace it with more complex processing.
    if 'hello' in user_input.lower():
        return "Hello! How can I help you today?"
    elif 'bye' in user_input.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    bot_response = chat(user_input)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
