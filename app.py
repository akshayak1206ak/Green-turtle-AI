from flask import Flask, render_template, request
from chatbot import get_response

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template("index.html")


# Chatbot Response
@app.route('/get')
def chatbot_response():

    user_text = request.args.get('msg')

    response = get_response(user_text)

    return response


# Run Flask Server
# Run Flask Server
if __name__ == '__main__':

    app.run(host="0.0.0.0", port=5000, debug=False)

