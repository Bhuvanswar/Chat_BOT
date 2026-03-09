from flask import Flask, render_template, request
from LLm import chat_with_groq

app = Flask(__name__)
chat_history = []
@app.route("/", methods=["GET","POST"])
def index():
    global chat_history
    message = None
    response = None
<<<<<<< HEAD
    if request.method == "GET":
        chat_history = [] 
=======
>>>>>>> 396b8ac0dec5b263f6a0c32267ca80300778047c

    if request.method == "POST":
        message = request.form["message"]
        response = chat_with_groq(message)

        chat_history.append({"role": "user", "content": message})
        chat_history.append({"role": "bot", "content": response})
    return render_template("home.html", chat_history=chat_history)

if __name__ == "__main__":
    app.run(debug=True)