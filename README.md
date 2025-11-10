# 💬 Dashboard Sentimen Opini Publik: Kasus Kematian Affan Kurniawan

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Akses%20Aplikasi-Live%20Demo-blue)](https://huggingface.co/spaces/randy990/Dashboard_Sentimen_Opini_Publik_Terhadap_Affan_Kurniawan)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Model Used](https://img.shields.io/badge/Model-Custom%20RF%2BBERT-orange)](https://huggingface.co/indobenchmark/indobert-base-p1)

## 👋 Apa Ini?

Aplikasi ini adalah sebuah alat (tool) berbasis web sederhana yang berfungsi untuk **mendeteksi dan mengklasifikasikan sentimen** (perasaan atau opini) dari komentar publik.

**Tujuan utamanya** adalah membantu memilah-milah respons warganet terkait isu sensitif, yaitu kematian Affan Kurniawan, menjadi dua kategori besar:

1.  **🟢 Positif:** Komentar yang mengandung pujian, simpati, dukungan, atau ungkapan duka cita yang tulus.
2.  **🔴 Negatif:** Komentar yang bersifat buruk, menghina, kritikan tajam, atau ujaran kebencian.

Aplikasi ini dirancang agar kita bisa lebih cepat memahami *mood* dan fokus utama dari percakapan digital yang terjadi.

## 🧠 Bagaimana Cara Kerjanya? (Penjelasan Bahasa Manusia)

Dapur pacu aplikasi ini menggunakan gabungan dua teknologi *Artificial Intelligence* (AI) yang bekerja dalam tim:

1.  **IndoBERT (Sang Penerjemah Cerdas):** Setiap kali Anda memasukkan komentar, model BERT bertugas memahami konteks dan nuansa bahasa Indonesia yang kompleks (termasuk bahasa non-formal di media sosial). Ia mengubah setiap komentar menjadi deretan angka-angka (disebut *embedding*) yang mewakili makna komentar tersebut.

2.  **Random Forest Classifier (Sang Pengambil Keputusan):** Deretan angka hasil terjemahan dari BERT kemudian diberikan ke model Random Forest. Model ini dilatih menggunakan data yang sudah kami labeli (Positif/Negatif) untuk mengambil keputusan final: apakah deretan angka tersebut lebih mirip dengan pola "Positif" atau "Negatif".

Hasil akhirnya adalah label sentimen (Positif atau Negatif) beserta tingkat keyakinannya.

## 🚀 Teknologi yang Digunakan

Proyek ini dibangun menggunakan *stack* teknologi yang andal:

* **Framework Web:** Python **Flask** (sebagai kerangka kerja utama backend).
* **Web Server:** **Gunicorn** (untuk menjalankan Flask di lingkungan produksi).
* **Model Dasar:** **IndoBERT Base P1** (untuk pemrosesan bahasa/tokenization/embedding).
* **Model Klasifikasi:** **Random Forest Classifier** (disimpan dalam `rf_bert_model_PosNeg.joblib`).

## ⚙️ Cara Menjalankan di Lingkungan Lokal (Local Setup)

Jika Anda ingin menjalankan proyek ini di komputer Anda sendiri:

1.  **Clone Repositori:**
    ```bash
    git clone [LINK_REPOSITORI_ANDA]
    cd Dashboard_Sentimen_Opini_Publik_Terhadap_Affan_Kurniawan
    ```
2.  **Buat Virtual Environment:** (Sangat disarankan)
    ```bash
    python -m venv venv
    source venv/bin/activate  # Untuk Linux
    # atau .\venv\Scripts\activate  # Untuk Windows
    ```
3.  **Instal Dependensi:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Jalankan Aplikasi:**
    ```bash
    gunicorn app:app -b 0.0.0.0:5000
    ```
5.  Akses aplikasi di browser : `http://127.0.0.1:5000`
