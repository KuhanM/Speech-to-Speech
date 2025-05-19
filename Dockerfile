FROM python:3.10-slim 
WORKDIR /app 
COPY . . 
RUN pip install --no-cache-dir -r requirements.txt 
RUN python -c "import whisper; whisper.load_model('base')" 
RUN python -c "from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer; M2M100ForConditionalGeneration.from_pretrained('facebook/m2m100_418M'); M2M100Tokenizer.from_pretrained('facebook/m2m100_418M')" 
ENV HF_HUB_DISABLE_SYMLINKS_WARNING=1 
ENV TF_ENABLE_ONEDNN_OPTS=0 
EXPOSE 5000 
CMD ["python", "app.py"] 
