from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import whisper
from transformers import pipeline
from gtts import gTTS
import os
import tempfile
import logging

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Language mappings
lang_map = {
    "af": {"name": "Afrikaans", "tts_code": "af"},
    "ar": {"name": "Arabic", "tts_code": "ar"},
    "bn": {"name": "Bengali", "tts_code": "bn"},
    "bg": {"name": "Bulgarian", "tts_code": "bg"},
    "ca": {"name": "Catalan", "tts_code": "ca"},
    "cs": {"name": "Czech", "tts_code": "cs"},
    "da": {"name": "Danish", "tts_code": "da"},
    "nl": {"name": "Dutch", "tts_code": "nl"},
    "fi": {"name": "Finnish", "tts_code": "fi"},
    "fr": {"name": "French", "tts_code": "fr"},
    "de": {"name": "German", "tts_code": "de"},
    "el": {"name": "Greek", "tts_code": "el"},
    "he": {"name": "Hebrew", "tts_code": "he"},
    "hi": {"name": "Hindi", "tts_code": "hi"},
    "hu": {"name": "Hungarian", "tts_code": "hu"},
    "is": {"name": "Icelandic", "tts_code": "is"},
    "id": {"name": "Indonesian", "tts_code": "id"},
    "it": {"name": "Italian", "tts_code": "it"},
    "ja": {"name": "Japanese", "tts_code": "ja"},
    "ko": {"name": "Korean", "tts_code": "ko"},
    "no": {"name": "Norwegian", "tts_code": "no"},
    "pl": {"name": "Polish", "tts_code": "pl"},
    "pt": {"name": "Portuguese", "tts_code": "pt-br"},
    "ro": {"name": "Romanian", "tts_code": "ro"},
    "ru": {"name": "Russian", "tts_code": "ru"},
    "sr": {"name": "Serbian", "tts_code": "sr"},
    "sk": {"name": "Slovak", "tts_code": "sk"},
    "es": {"name": "Spanish", "tts_code": "es"},
    "sw": {"name": "Swahili", "tts_code": "sw"},
    "sv": {"name": "Swedish", "tts_code": "sv"},
    "ta": {"name": "Tamil", "tts_code": "ta"},
    "te": {"name": "Telugu", "tts_code": "te"},
    "th": {"name": "Thai", "tts_code": "th"},
    "tr": {"name": "Turkish", "tts_code": "tr"},
    "uk": {"name": "Ukrainian", "tts_code": "uk"},
    "ur": {"name": "Urdu", "tts_code": "ur"},
    "vi": {"name": "Vietnamese", "tts_code": "vi"},
    "cy": {"name": "Welsh", "tts_code": "cy"}
}

def transcribe_audio(audio_path):
    """Transcribe audio file to text using Whisper."""
    try:
        result = whisper_model.transcribe(audio_path)
        return result["text"].strip()
    except Exception as e:
        logger.error(f"Error transcribing audio: {e}")
        raise

def load_translation_pipeline(source_lang, target_lang):
    """Load translation pipeline for specified language pair."""
    try:
        model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
        translator = pipeline("translation", model=model_name)
        return translator
    except Exception as e:
        logger.error(f"Error loading translation model: {e}")
        raise

def translate_text(translator, text):
    """Translate text to target language."""
    try:
        translated = translator(text)[0]["translation_text"]
        return translated
    except Exception as e:
        logger.error(f"Error translating text: {e}")
        raise

def text_to_speech(text, lang, output_file):
    """Convert text to speech and save as MP3."""
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save(output_file)
        return output_file
    except Exception as e:
        logger.error(f"Error generating speech: {e}")
        raise

# Load Whisper model once at startup
try:
    logger.info("Loading Whisper model...")
    whisper_model = whisper.load_model("base")
    logger.info("Whisper model loaded successfully")
except Exception as e:
    logger.error(f"Failed to load Whisper model: {e}")
    raise

# Pre-load translation model for en-hi
try:
    logger.info("Pre-loading translation model for en-hi...")
    global_translator = load_translation_pipeline("en", "hi")
    logger.info("Translation model loaded successfully")
except Exception as e:
    logger.error(f"Failed to pre-load translation model: {e}")
    raise

@app.route('/')
def index():
    """Serve the frontend HTML."""
    logger.info("Serving index.html")
    return send_file('templates/index.html')

@app.route('/translate', methods=['POST'])
def translate():
    """Handle audio file upload or recording and process translation."""
    try:
        target_lang = request.form.get('target_language')
        if not target_lang or target_lang not in lang_map:
            return jsonify({"error": f"Target language '{target_lang}' not supported. Choose from {list(lang_map.keys())}"}), 400

        # Handle file upload
        audio_file = request.files.get('audio_file')
        if not audio_file:
            return jsonify({"error": "No audio file provided"}), 400

        # Create temporary file for audio processing
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_audio:
            audio_path = temp_audio.name
            audio_file.save(audio_path)

        # Step 1: Transcribe audio
        logger.info("Transcribing audio...")
        transcribed_text = transcribe_audio(audio_path)

        # Step 2: Translate text
        logger.info("Loading translation model...")
        translator = global_translator if target_lang == "hi" else load_translation_pipeline("en", target_lang)
        logger.info("Translating text...")
        translated_text = translate_text(translator, transcribed_text)

        # Step 3: Generate speech
        logger.info("Generating speech...")
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_output:
            output_path = text_to_speech(translated_text, lang_map[target_lang]["tts_code"], temp_output.name)

        # Clean up temporary audio file
        os.unlink(audio_path)

        # Send results back
        return jsonify({
            "original_text": transcribed_text,
            "translated_text": translated_text,
            "audio_url": f"/get_audio/{os.path.basename(output_path)}"
        })

    except Exception as e:
        logger.error(f"Error in translation process: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/get_audio/<filename>')
def get_audio(filename):
    """Serve the generated audio file."""
    try:
        return send_file(os.path.join(tempfile.gettempdir(), filename), as_attachment=True)
    except Exception as e:
        logger.error(f"Error serving audio file: {e}")
        return jsonify({"error": "Audio file not found"}), 404

if __name__ == '__main__':
    logger.info("Starting Flask server...")
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)