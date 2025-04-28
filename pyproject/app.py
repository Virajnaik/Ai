from flask import Flask, render_template, request
import google.generativeai as genai

API_KEY = "AIzaSyAp8qzIlZp1LLAXPB7VKlRgR3e5fBuMPxU" 
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

app = Flask(__name__)

conversation_history = []

@app.route("/")
def index():
    return render_template("index.html", conversation=conversation_history)

@app.route("/chat", methods=["POST"])
def chat_route():
    user_input = request.form["user_input"]

    conversation_history.append(f"You: {user_input}")
    
    response = chat.send_message(user_input)
    
    conversation_history.append(f"AI: {response.text}")
    
    return render_template("index.html", conversation=conversation_history)

if __name__ == "__main__":
    app.run(debug=True)
