
from flask import Flask, request, jsonify, send_from_directory
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  # Use env variable for security

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    # ChatGPT response only
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_input}]
    )

    return jsonify({
        "response": response.choices[0].message['content']
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
