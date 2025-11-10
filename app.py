import os
from flask import Flask, render_template, request, jsonify
import joblib
import torch
import numpy as np
from transformers import BertTokenizer, BertModel

# Inisialisasi Aplikasi Flask
app = Flask(__name__)

MODEL_FILE = 'rf_bert_model_PosNeg.joblib'
print("Memuat model Random Forest...")
if not os.path.exists(MODEL_FILE):
    print(f"Error: File model '{MODEL_FILE}' tidak ditemukan.")
    print("Pastikan file tersebut berada di folder yang sama dengan app.py")
    rf_model = None
else:
    try:
        rf_model = joblib.load(MODEL_FILE)
        print("Model Random Forest berhasil dimuat.")
    except Exception as e:
        print(f"Error saat memuat model: {e}")
        rf_model = None

print("Memuat model IndoBERT (mungkin perlu beberapa saat)...")
try:
    tokenizer = BertTokenizer.from_pretrained('indobenchmark/indobert-base-p1')
    bert_model = BertModel.from_pretrained('indobenchmark/indobert-base-p1')
    bert_model.eval()  
    print("Model IndoBERT berhasil dimuat.")
except Exception as e:
    print(f"Error saat mengunduh/memuat IndoBERT: {e}")
    print("Pastikan Anda memiliki koneksi internet saat pertama kali menjalankan.")
    tokenizer = None
    bert_model = None

def get_bert_embedding(text):
    """Mengubah teks mentah menjadi vektor embedding BERT [CLS]."""
    if not tokenizer or not bert_model:
        return None
        
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = bert_model(**inputs)
    cls_embedding = outputs.last_hidden_state[:, 0, :].numpy()
    return cls_embedding


@app.route('/')
def home():
    """Menampilkan halaman utama (index.html)."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Menerima data komentar dan mengembalikan prediksi sentimen."""
    if rf_model is None or bert_model is None:
        return jsonify({'error': 'Model tidak berhasil dimuat. Periksa konsol server.'}), 500

    try:
        data = request.get_json()
        comment_text = data.get('comment', '')

        if not comment_text:
            return jsonify({'error': 'Tidak ada teks komentar yang diberikan.'}), 400

        embedding = get_bert_embedding(comment_text)
        if embedding is None:
             return jsonify({'error': 'Gagal membuat embedding BERT.'}), 500

        prediction = rf_model.predict(embedding)
        probability = rf_model.predict_proba(embedding)
        sentiment_code = int(prediction[0])
        sentiment = "Positif" if sentiment_code == 1 else "Negatif"
        
        confidence = float(np.max(probability))
        
        return jsonify({
            'sentiment': sentiment,
            'confidence': f"{confidence * 100:.2f}%"
        })

    except Exception as e:
        print(f"Error pada saat prediksi: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    if rf_model is not None and bert_model is not None:
        print("\nServer Flask siap dijalankan.")
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        print("\nServer TIDAK dapat dijalankan karena model gagal dimuat.")