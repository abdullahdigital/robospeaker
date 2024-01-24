from flask import Flask, render_template, request, jsonify
from threading import Thread
import pyttsx3

app = Flask(__name__)

def generate_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def background_speak(text):
    thread = Thread(target=generate_speech, args=(text,))
    thread.start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speak', methods=['POST'])
def speak():
    data = request.get_json()
    text = data.get('text', '')
    background_speak(text)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
