from flask import Flask, request, jsonify, render_template
import requests
import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


client = Groq(
    api_key =os.environ.get("GROQ_API_KEY"),
)

def generate_lyrics_from_groq(prompt):
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are an music assistant to create a lyrics based on the user description and language  and music gener",
        },
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content





@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_lyrics', methods=['POST'])
def generate_lyrics():
    data = request.json
    song_description = data.get('description', '')
    language = data.get('language', 'English')
    genre = data.get('genre', 'Pop')

    if not song_description:
        return jsonify({'error': 'Please provide a song description'}), 400


    prompt = f"Generate song lyrics in {language}, genre: {genre}, description: {song_description}"

    generated_lyrics = generate_lyrics_from_groq(prompt)

    return jsonify({'lyrics': generated_lyrics})

if __name__ == '__main__':
    app.run(debug=True)
