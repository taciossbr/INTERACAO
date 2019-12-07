from flask import Flask, jsonify, request
from firstbot import chatbot

app = Flask(__name__)

@app.route('/', methods=['POST'])
def post():
    data = request.get_json()
    text = data['text']
    resp = chatbot.get_response(text)
    # print(type(resp))
    return jsonify(dict(text=str(resp))), 200


app.run(host='0.0.0.0', port=8080, debug=True)