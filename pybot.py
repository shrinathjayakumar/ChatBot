from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

user_name = None
bot_name = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    global user_name
    global bot_name
    user_input = request.json['user_input']
    
    if user_name is None:
        user_name = request.form['user_name'].strip()  # Set the user's name
        bot_name = request.form['bot_name'].strip()  # Set the bot's name
        response = f"Welcome, {user_name}! How can I assist you today, {bot_name}?"
    else:
        response = chatbot_response(user_input)
    
    return jsonify(response=response)

def chatbot_response(user_input):
    # Implement your chatbot logic here based on user input
    # Example:
    if 'hello' in user_input.lower():
        return "How can I help?"
    elif 'help' in user_input.lower():
        return "Sure, I'm here to help. What do you need assistance with?"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask a different question?"

if __name__ == "__main__":
    app.run(debug=True)
