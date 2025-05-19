Speech-to-Speech Translator

A Flask-based web application that transcribes English audio and translates it into multiple languages (e.g., Hindi, Spanish, Tamil, French) using OpenAI's Whisper for transcription and Facebook's M2M100 for translation. The translated text is converted to speech using gTTS, providing a complete speech-to-speech translation pipeline.
Features

Audio Transcription: Converts English audio to text using Whisper (base model).
Multi-Language Translation: Translates transcribed text to 40+ languages (e.g., hi, es, ta, fr) with M2M100 (facebook/m2m100_418M).
Text-to-Speech: Generates audio for translated text using gTTS.
Web Interface: Upload audio files via a simple HTML frontend and receive transcription, translation, and audio output.
Error Handling: Robust logging and post-processing to correct translation errors (e.g., Hindi-specific fixes).

Prerequisites

Python: Version 3.10 (recommended over Windows Store Python 3.11).
FFmpeg: Required for Whisper’s audio processing.
Git: For cloning and managing the repository.
Virtual Environment: To isolate dependencies.

Installation

Clone the Repository:
git clone https://github.com/KuhanM/Speech-to-Speech.git
cd Speech-to-Speech


Set Up a Virtual Environment:
python -m venv venv
.\venv\Scripts\activate  # Windows


Install Dependencies:
pip install -r requirements.txt


Install FFmpeg:

Download from ffmpeg.org.
Extract and add the bin folder to your system PATH (e.g., C:\path\to\ffmpeg\bin).
Verify:ffmpeg -version




Suppress Warnings (Optional):To avoid Hugging Face and TensorFlow warnings:
set HF_HUB_DISABLE_SYMLINKS_WARNING=1
set TF_ENABLE_ONEDNN_OPTS=0



Usage

Run the Application:
python app.py

The server will start at http://localhost:5000.

Access the Web Interface:

Open http://localhost:5000 in a browser.
Upload an audio file (e.g., WAV or MP3) containing English speech.
Select a target language (e.g., Hindi, Spanish, Tamil).
Click Translate Speech to get:
Transcribed text (English).
Translated text (target language).
Audio file of the translated text.




Example:

Input Audio: "I like cats I have two cats at home and I probably see them in two days"
Hindi Output: "मैं बिल्लियों को पसंद करता हूँ मेरे घर पर दो बिल्लियाँ हैं और मैं शायद उन्हें दो दिन में देखूंगा"
Spanish Output: "Me gustan los gatos, tengo dos gatos en casa y probablemente los vea en dos días"



Project Structure
Speech-to-Speech/
├── .gitignore              # Ignores venv, cache, and temporary files
├── Dockerfile              # For containerized deployment
├── app.py                  # Flask backend with transcription and translation
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Frontend HTML interface
├── README.md               # Project documentation

Supported Languages
The app supports translation to 40+ languages, including:

Hindi (hi)
Spanish (es)
Tamil (ta)
French (fr)
Arabic (ar)
See app.py (lang_map) for the full list.

Troubleshooting

Authentication Errors:
Use a GitHub Personal Access Token for git push (Settings > Developer settings > Personal access tokens).


FFmpeg Not Found:
Ensure FFmpeg is in your PATH and verify with ffmpeg -version.


Translation Errors:
Check logs in the console for transcription or translation issues.
Verify audio quality (clear English speech).


Port Conflicts:
If localhost:5000 is in use:netstat -aon | findstr :5000
taskkill /PID <pid> /F


Or change the port in app.py (e.g., port=8080).



Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a branch:git checkout -b feature/your-feature


Commit changes:git commit -m "Add your feature"


Push to your fork:git push origin feature/your-feature


Open a Pull Request on GitHub.

Please follow the Code of Conduct and include tests for new features.
License
This project is licensed under the MIT License. See LICENSE for details.
Acknowledgments

OpenAI Whisper for audio transcription.
Hugging Face Transformers for M2M100 translation.
gTTS for text-to-speech.
Built with Flask.

Contact
For questions or feedback, open an issue on GitHub or contact KuhanM.