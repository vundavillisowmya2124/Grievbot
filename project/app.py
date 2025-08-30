from flask import Flask, render_template, request, jsonify
import wikipedia   # pip install wikipedia

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.json.get("msg", "").strip()
    
    if not user_input:
        return jsonify({"response": "Please type a question."})
    
    try:
        # Get a short Wikipedia summary (2 sentences)
        summary = wikipedia.summary(user_input, sentences=2)
        response = summary
    except wikipedia.exceptions.DisambiguationError as e:
        response = f"Your query is too broad. Did you mean: {', '.join(e.options[:5])}?"
    except wikipedia.exceptions.PageError:
        response = "Sorry, I couldn't find an answer for that."
    except Exception as e:
        response = "Sorry, I ran into a problem while searching. Please try again."
    
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
