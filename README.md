# Chatbot UI

## Overview
This project is a simple chatbot interface built using HTML, CSS (Bootstrap), and JavaScript (jQuery). It allows users to send messages and receive responses dynamically via AJAX requests.

## Features
- Clean and modern UI with Bootstrap styling
- Smooth chat experience with auto-scrolling
- User-friendly input with "Enter" key support
- AJAX-based interaction with a backend
- Responsive layout for different screen sizes

## Setup and Usage
1. Clone this repository or download the files.
2. Ensure you have a backend server running with an endpoint `/get_response` to handle requests.
3. Open `index.html` in a browser to start using the chatbot.

## Dependencies
- [Bootstrap 4.5.2](https://getbootstrap.com/)
- [jQuery 3.6.0](https://jquery.com/)

## Backend Integration
The chatbot expects a backend service that accepts a `POST` request at `/get_response` with a parameter `user_input` and returns a JSON response:
```json
{
  "response": "Hello, how can I help you?"
}
```
Ensure your backend is configured to handle CORS if hosted separately.

## Flask Backend Setup
If you are using Flask as the backend, follow these steps:

### Install Flask
```bash
pip install flask
```

### Create `app.py`
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form.get('user_input')
    response_text = f"You said: {user_input}"
    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(debug=True)
```

### Run the Flask App
```bash
python app.py
```
Your Flask server will be running on `http://127.0.0.1:5000`.

## Contributing
Feel free to fork and modify this project to enhance its features. Pull requests are welcome!

## License
This project is open-source and available under the MIT License.

