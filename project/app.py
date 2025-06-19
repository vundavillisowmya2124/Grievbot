from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

faq = {
    "how to reset password": "Click 'Forgot Password' on the login page.",
    "how to contact support": "Email us at support@example.com.",
    "lab results delay": "Results take 48 hours to update.",
    "fee payment issue": "Check your payment ID and retry."
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.json.get("msg").lower()
    response = faq.get(user_input, "Sorry, I don't understand that. Please contact support.")
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
