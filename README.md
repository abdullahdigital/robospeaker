# RoboSpeaker

RoboSpeaker is a Flask web application that converts text to speech using the `pyttsx3` library. This application can handle text input from users and convert it into spoken words.

## Features

- Convert text input to speech.
- Increment and display the number of times the text-to-speech feature has been used.

## Requirements

- Python 3.x
- Flask
- pyttsx3

## How It Works

RoboSpeaker leverages the `pyttsx3` library to convert text into speech. Here’s a brief overview of how the application is structured:

1. **Flask Application**: The core of the application is built using Flask, a lightweight web framework for Python. It handles HTTP requests and serves the web pages.

2. **Text-to-Speech Conversion**: The `pyttsx3` library is used for converting text into speech. When text is submitted through the web interface, it is processed by `pyttsx3` to generate the corresponding speech.

3. **Threading for Performance**: The speech generation process runs in a separate thread, allowing the application to handle multiple requests efficiently without blocking the main thread.

4. **Speech Counter**: Each time a text-to-speech request is processed, a counter is incremented. This counter is used to track and display the number of times the text-to-speech functionality has been used.

## How to Use

1. **Access the Web Application**: Open your web browser and navigate to `http://127.0.0.1:5000`.

2. **Input Text**: Enter the text you want to convert to speech in the input field on the homepage.

3. **Submit**: Click the submit button to hear the speech. The application will also update and display the total number of speech conversions performed.

4. **View Count**: The speech count, which tracks how many times the text-to-speech feature has been used, will be displayed on the page.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and submit a pull request.

