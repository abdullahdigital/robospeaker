from flask import Flask, render_template, request, jsonify
from threading import Thread
import pyttsx3

app = Flask(__name__)

# Initialize a counter variable
speech_counter = 0

def generate_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def background_speak(text):
    global speech_counter
    # Increment the counter each time text is spoken
    speech_counter += 1
    thread = Thread(target=generate_speech, args=(text,))
    thread.start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main', methods=['POST'])
def speak():
    data = request.get_json()
    text = data.get('text', '')
    background_speak(text)
    # Return the current speech count in the response
    return jsonify({'status': 'success', 'speech_count': speech_counter})

if __name__ == '__main__':
    app.run(debug=True)
