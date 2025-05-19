# Universal Speech Translator 🌍🎙️

A cutting-edge AI-powered web application that breaks language barriers by translating spoken audio into 40+ languages with natural-sounding speech synthesis.

![Speech Translator Demo](https://img.shields.io/badge/Status-Live-success)
![Languages](https://img.shields.io/badge/Languages-40+-blue)
![AI Powered](https://img.shields.io/badge/AI-Whisper%20%2B%20Transformers-orange)

## 🚀 Features

### 🎯 Core Functionality
- **Speech-to-Text**: Advanced Whisper AI for accurate transcription
- **Multi-Language Translation**: Support for 40+ world languages
- **Text-to-Speech**: Natural-sounding voice synthesis
- **Real-time Processing**: Lightning-fast translation pipeline

### 🎨 User Experience
- **Modern UI**: Beautiful gradient design with animated particles
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Dual Input Methods**: Upload audio files or record directly in browser
- **Progress Tracking**: Real-time progress indicators
- **Audio Playback**: Built-in player for translated speech

### 🛡️ Security & Privacy
- **Privacy First**: No permanent file storage
- **Secure Processing**: Files processed and immediately discarded
- **CORS Enabled**: Safe cross-origin requests
- **Client-side Validation**: Input validation before processing

## 🌐 Supported Languages

| Region | Languages |
|--------|-----------|
| **European** | Spanish, French, German, Italian, Dutch, Portuguese, Russian, Polish, Swedish, Danish, Norwegian, Finnish, Czech, Hungarian, Romanian, Bulgarian, Croatian, Slovak, Greek, Turkish |
| **Asian** | Chinese, Japanese, Korean, Hindi, Bengali, Tamil, Telugu, Thai, Vietnamese, Indonesian, Malay, Filipino |
| **Middle Eastern** | Arabic, Hebrew, Persian, Urdu |
| **African** | Swahili, Afrikaans, Amharic |
| **Others** | Welsh, Irish, Icelandic, Basque, Catalan, Galician |

## 🏗️ Architecture

### Frontend Stack
```
├── HTML5 (Semantic Structure)
├── CSS3 (Modern Styling)
│   ├── CSS Grid & Flexbox
│   ├── Custom Animations
│   ├── Responsive Design
│   └── Glass-morphism Effects
├── Vanilla JavaScript
│   ├── File Upload Handling
│   ├── Audio Recording API
│   ├── Progress Management
│   └── Dynamic UI Updates
└── Font Awesome Icons
```

### Backend Stack (Python)
```
├── Whisper (Speech Recognition)
├── Transformers (Language Translation)
├── gTTS (Text-to-Speech)
├── PyTorch (ML Framework)
└── Flask/FastAPI (Web Framework)
```

## 📁 Project Structure

```
speech-translator/
├── 📄 index.html              # Main website file
├── 🐍 backend/
│   ├── app.py                 # Flask/FastAPI server
│   ├── translator.py          # Translation logic
│   ├── requirements.txt       # Python dependencies
│   └── models/               # Pre-trained models
├── 📋 netlify.toml            # Netlify configuration
├── 📖 README.md               # This file
├── 📄 LICENSE                 # MIT License
└── 🖼️ assets/
    ├── images/               # Screenshots, logos
    └── demos/               # Demo files
```

## 🚀 Quick Start

### Option 1: Frontend Only (Demo)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/speech-translator.git
   cd speech-translator
   ```

2. **Open locally:**
   ```bash
   # Simply open index.html in your browser
   open index.html
   # OR serve with Python
   python -m http.server 8000
   ```

3. **Deploy to Netlify:**
   - Drag the project folder to [netlify.com](https://netlify.com)
   - Site goes live instantly!

### Option 2: Full-Stack Application

1. **Setup Backend:**
   ```bash
   cd backend
   pip install -r requirements.txt
   python app.py
   ```

2. **Environment Variables:**
   ```bash
   export FLASK_ENV=development
   export MODEL_PATH=/path/to/models
   export UPLOAD_FOLDER=/tmp/uploads
   ```

3. **Frontend Configuration:**
   ```javascript
   // Update API_BASE_URL in index.html
   const API_BASE_URL = 'http://localhost:5000';
   ```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- Node.js 14+ (for development)
- 4GB+ RAM (for ML models)
- Modern web browser

### Backend Dependencies
```bash
pip install -r requirements.txt
```

**requirements.txt:**
```
openai-whisper==20231117
transformers==4.35.0
torch==2.1.0
gtts==2.4.0
flask==3.0.0
flask-cors==4.0.0
python-multipart==0.0.6
uvicorn==0.24.0
fastapi==0.104.0
```

### System Requirements
- **Development**: 8GB RAM, 2GB storage
- **Production**: 16GB RAM, 10GB storage (for all models)

## 🔧 Configuration

### Environment Variables
```bash
# .env file
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
MODEL_CACHE_DIR=/models
MAX_FILE_SIZE=50MB
ALLOWED_EXTENSIONS=mp3,wav,m4a,flac
CORS_ORIGINS=https://yourdomain.com
```

### Model Configuration
```python
# config.py
WHISPER_MODEL_SIZE = "base"  # tiny, base, small, medium, large
TRANSLATION_BATCH_SIZE = 32
TTS_SPEED = "normal"  # slow, normal, fast
CACHE_TRANSLATIONS = True
```

## 🚀 Deployment

### 1. Netlify (Frontend)
```bash
# netlify.toml
[build]
  publish = "."
  command = "echo 'Static site ready'"

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    Content-Security-Policy = "default-src 'self' 'unsafe-inline' cdnjs.cloudflare.com"
```

### 2. Heroku (Full-Stack)
```bash
# Procfile
web: python backend/app.py
release: python -c "import nltk; nltk.download('punkt')"

# runtime.txt
python-3.11.5

# Deploy
heroku create your-app-name
git push heroku main
```

### 3. Docker (Containerized)
```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["python", "backend/app.py"]
```

### 4. Cloud Functions (Serverless)
```bash
# Deploy to Vercel
vercel --prod

# Deploy to AWS Lambda
sam deploy --guided

# Deploy to Google Cloud Functions
gcloud functions deploy translate-speech
```

## 📊 Performance Optimization

### Frontend Optimizations
- **Lazy Loading**: Models loaded on-demand
- **Compression**: Gzip compression for assets
- **Caching**: Aggressive browser caching
- **CDN**: Static assets served from CDN

### Backend Optimizations
```python
# Model caching
@lru_cache(maxsize=1)
def get_whisper_model():
    return whisper.load_model("base")

# Async processing
async def process_audio(file):
    # Use asyncio for concurrent processing
    pass

# Response compression
app.config['COMPRESS_MIMETYPES'] = [
    'application/json',
    'text/html',
    'text/css',
    'application/javascript'
]
```

## 🔒 Security

### Input Validation
```python
ALLOWED_EXTENSIONS = {'mp3', 'wav', 'm4a', 'flac'}
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB

def validate_audio_file(file):
    if file.size > MAX_FILE_SIZE:
        raise ValueError("File too large")
    
    if not file.filename.split('.')[-1].lower() in ALLOWED_EXTENSIONS:
        raise ValueError("Invalid file type")
```

### Rate Limiting
```python
from flask_limiter import Limiter

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["100 per hour"]
)

@app.route('/api/translate')
@limiter.limit("5 per minute")
def translate():
    pass
```

## 📈 Monitoring & Analytics

### Health Checks
```python
@app.route('/health')
def health_check():
    return {
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'version': '1.0.0',
        'models_loaded': bool(whisper_model)
    }
```

### Logging
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
```

## 🧪 Testing

### Unit Tests
```bash
# Run tests
python -m pytest tests/

# Coverage report
pytest --cov=backend --cov-report=html
```

### Integration Tests
```python
# test_api.py
def test_translation_endpoint(client):
    with open('test_audio.wav', 'rb') as f:
        response = client.post('/api/translate', 
                             data={'audio': f, 'target_lang': 'es'})
    
    assert response.status_code == 200
    assert 'translated_text' in response.json()
```

### Load Testing
```bash
# Using Artillery
artillery run load-test.yml

# Using Apache Bench
ab -n 100 -c 10 http://localhost:5000/api/translate
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Workflow
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Standards
- **Python**: Follow PEP 8, use Black formatter
- **JavaScript**: Use ESLint with Airbnb config
- **CSS**: Follow BEM methodology
- **Commits**: Use Conventional Commits format

## 📚 API Documentation

### Translation Endpoint
```
POST /api/translate
Content-Type: multipart/form-data

Parameters:
- audio: Audio file (required)
- target_lang: Target language code (required)
- model_size: Whisper model size (optional, default: "base")

Response:
{
    "original_text": "Hello world",
    "translated_text": "Hola mundo",
    "audio_url": "/api/audio/abc123.mp3",
    "processing_time": 2.5,
    "confidence": 0.95
}
```

### Health Check
```
GET /health

Response:
{
    "status": "healthy",
    "timestamp": "2024-01-01T00:00:00Z",
    "version": "1.0.0",
    "models_loaded": true
}
```

## 🐛 Troubleshooting

### Common Issues

**Issue**: "ModuleNotFoundError: No module named 'whisper'"
```bash
# Solution
pip install openai-whisper
```

**Issue**: "CUDA out of memory"
```python
# Solution: Use CPU or smaller model
device = "cpu"  # Force CPU usage
model = whisper.load_model("tiny")  # Smaller model
```

**Issue**: "Audio file not supported"
```bash
# Solution: Install ffmpeg
# Mac
brew install ffmpeg
# Ubuntu
sudo apt install ffmpeg
# Windows
# Download from https://ffmpeg.org/
```

### Performance Issues
- Use smaller Whisper models for faster processing
- Implement audio preprocessing to reduce file sizes
- Cache frequently translated phrases
- Use GPU acceleration when available

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenAI** for the Whisper speech recognition model
- **Hugging Face** for the Transformers library
- **Google** for the Text-to-Speech API
- **Community** for contributions and feedback

## 📞 Support

- **Documentation**: [Wiki](https://github.com/yourusername/speech-translator/wiki)
- **Issues**: [GitHub Issues](https://github.com/yourusername/speech-translator/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/speech-translator/discussions)
- **Email**: support@speechtranslator.com

## 🗺️ Roadmap

### Version 1.1 (Next Release)
- [ ] Real-time speech translation
- [ ] Voice cloning for consistent speaker identity
- [ ] Batch processing for multiple files
- [ ] Advanced language detection

### Version 1.2 (Future)
- [ ] Mobile app (React Native)
- [ ] Desktop app (Electron)
- [ ] API rate limiting and premium tiers
- [ ] Integration with popular video platforms

### Version 2.0 (Long-term)
- [ ] Neural voice synthesis
- [ ] Emotion preservation in translation
- [ ] Multi-speaker support
- [ ] Real-time video dubbing

---

<div align="center">

**Made with ❤️ by the Speech Translator Team**

[🌐 Live Demo](https://your-app.netlify.app) • [📖 Documentation](https://docs.speechtranslator.com) • [🐛 Report Bug](https://github.com/yourusername/speech-translator/issues) • [💡 Request Feature](https://github.com/yourusername/speech-translator/issues)

</div>