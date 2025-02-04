from flask import Flask, render_template, request
import openai  # Pour utiliser GPT-3 ou un autre modèle de langage


app = Flask(__name__)

# Configuration pour l'API GPT-3 (clé d'accès)
openai.api_key = 'rVb0PrhF3E4CUGxARUkHT3BlbkFJPMGdbCJSMw5YYPzbipIo'  # Remplace par ta clé d'accès

# Page d'accueil du chatbot
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint pour obtenir la réponse du chatbot via l'API GPT-3
@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']
    
    # Fonction pour obtenir une réponse du modèle GPT-3
def get_gpt3_response(prompt_text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt_text,
        max_tokens=50
    )
    return response.choices[0].text.strip()

# Exemple d'utilisation de la fonction pour obtenir une réponse
user_input = "Bonjour, comment ça va ?"
bot_response = get_gpt3_response(user_input)
print(bot_response)

if __name__ == '__main__':
    app.run(debug=True)
