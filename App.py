from flask import Flask, render_template, request
from LLm import chat_with_groq

app = Flask(__name__)
chat_history = []
@app.route("/", methods=["GET","POST"])
def index():
    global chat_history
    message = None
    response = None

    if request.method == "POST":
        message = request.form["message"]
        response = chat_with_groq(message)

        chat_history.append({"role": "user", "content": message})
        chat_history.append({"role": "bot", "content": response})
    return render_template("home.html", chat_history=chat_history)

if __name__ == "__main__":
    app.run(debug=True)