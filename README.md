# Speech-to-Speech Translator

A powerful Flask-based web application that provides real-time speech-to-speech translation. Upload English audio and get instant transcription, translation to 40+ languages, and audio output in your target language.

## 🚀 Features

- **Audio Transcription**: Converts English audio to text using OpenAI's Whisper (base model)
- **Multi-Language Translation**: Translates to 40+ languages using Facebook's M2M100 (facebook/m2m100_418M)
- **Text-to-Speech**: Generates audio for translated text using Google Text-to-Speech (gTTS)
- **Web Interface**: Simple and intuitive HTML frontend for easy file uploads and results
- **Error Handling**: Robust logging and post-processing with language-specific corrections
- **Complete Pipeline**: End-to-end speech-to-speech translation in one seamless workflow

## 📋 Prerequisites

Before installing, ensure you have:

- **Python**: Version 3.10 or higher (recommended over Windows Store Python 3.11)
- **FFmpeg**: Required for Whisper's audio processing
- **Git**: For cloning and managing the repository
- **Virtual Environment**: To isolate project dependencies

## 🛠 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/KuhanM/Speech-to-Speech.git
cd Speech-to-Speech
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg

**Windows:**
1. Download from [ffmpeg.org](https://ffmpeg.org)
2. Extract and add the `bin` folder to your system PATH (e.g., `C:\path\to\ffmpeg\bin`)
3. Verify installation: `ffmpeg -version`

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install ffmpeg
```

### 5. Environment Setup (Optional)

To suppress warnings:
```bash
# Windows
set HF_HUB_DISABLE_SYMLINKS_WARNING=1
set TF_ENABLE_ONEDNN_OPTS=0

# macOS/Linux
export HF_HUB_DISABLE_SYMLINKS_WARNING=1
export TF_ENABLE_ONEDNN_OPTS=0
```

## 🚀 Usage

### 1. Start the Application

```bash
python app.py
```

The server will start at `http://localhost:5000`

### 2. Using the Web Interface

1. Open `http://localhost:5000` in your browser
2. Upload an audio file (WAV, MP3, etc.) containing English speech
3. Select your target language from the dropdown
4. Click **"Translate Speech"**
5. Get your results:
   - Original transcription (English)
   - Translated text (target language)
   - Audio file of the translation

### 3. Example Translation

**Input Audio**: *"I like cats I have two cats at home and I probably see them in two days"*

**Hindi Output**: *"मैं बिल्लियों को पसंद करता हूँ मेरे घर पर दो बिल्लियाँ हैं और मैं शायद उन्हें दो दिन में देखूंगा"*

**Spanish Output**: *"Me gustan los gatos, tengo dos gatos en casa y probablemente los vea en dos días"*

## 📁 Project Structure

```
Speech-to-Speech/
├── .gitignore              # Ignores venv, cache, and temporary files
├── Dockerfile              # For containerized deployment
├── app.py                  # Flask backend with transcription and translation
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Frontend HTML interface
└── README.md              # Project documentation
```

## 🌍 Supported Languages

The application supports translation to 40+ languages, including:

| Language | Code | Language | Code |
|----------|------|----------|------|
| Hindi | `hi` | Arabic | `ar` |
| Spanish | `es` | Chinese | `zh` |
| Tamil | `ta` | Japanese | `ja` |
| French | `fr` | German | `de` |
| Portuguese | `pt` | Italian | `it` |
| Russian | `ru` | Korean | `ko` |

*See `app.py` (`lang_map`) for the complete list of supported languages.*

## 🔧 Troubleshooting

### Authentication Errors
- Use a GitHub Personal Access Token for git operations
- Go to: Settings → Developer settings → Personal access tokens

### FFmpeg Issues
- Ensure FFmpeg is in your system PATH
- Verify with: `ffmpeg -version`
- Restart your terminal after PATH changes

### Translation Errors
- Check console logs for detailed error messages
- Ensure audio contains clear English speech
- Verify audio file format is supported

### Port Conflicts
If `localhost:5000` is already in use:

**Windows:**
```bash
netstat -aon | findstr :5000
taskkill /PID <process_id> /F
```

**Alternative:** Change the port in `app.py`:
```python
app.run(host='0.0.0.0', port=8080, debug=True)
```

## 🤝 Contributing

Contributions are welcome! Here's how to contribute:

1. **Fork** the repository
2. **Create** a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit** your changes:
   ```bash
   git commit -m "Add your feature description"
   ```
4. **Push** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open** a Pull Request on GitHub

Please ensure your contributions include:
- Clear documentation
- Test cases for new features
- Adherence to the existing code style

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper) for audio transcription
- [Hugging Face Transformers](https://huggingface.co/transformers/) for M2M100 translation model
- [gTTS](https://gtts.readthedocs.io/) for text-to-speech synthesis
- [Flask](https://flask.palletsprojects.com/) for the web framework

## 📞 Contact

For questions, suggestions, or feedback:
- **GitHub Issues**: [Open an issue](https://github.com/KuhanM/Speech-to-Speech/issues)
- **Maintainer**: [KuhanM](https://github.com/KuhanM)

---

⭐ **Like this project?** Give it a star on GitHub and share it with others!