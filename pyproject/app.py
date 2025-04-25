from flask import Flask, render_template, request
import google.generativeai as genai

# Configure Gemini API
API_KEY = "AIzaSyAp8qzIlZp1LLAXPB7VKlRgR3e5fBuMPxU"  # Make sure to use your actual API key
genai.configure(api_key=API_KEY)

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

# Create Flask app
app = Flask(__name__)

# Store conversation history
conversation_history = []

# Route to show the chat page
@app.route("/")
def index():
    return render_template("index.html", conversation=conversation_history)

# Route to handle form submission and generate Gemini response
@app.route("/chat", methods=["POST"])
def chat_route():
    user_input = request.form["user_input"]
    # Store user input in the conversation history
    conversation_history.append(f"You: {user_input}")
    
    # Get response from Gemini model
    response = chat.send_message(user_input)
    
    # Store Gemini's response in the conversation history
    conversation_history.append(f"AI: {response.text}")
    
    # Render the updated conversation
    return render_template("index.html", conversation=conversation_history)

# Run the web server
if __name__ == "__main__":
    app.run(debug=True)
