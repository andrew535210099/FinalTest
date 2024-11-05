# prediction.py

import streamlit as st

def app():
    st.markdown("""
    <style>
    .title {
        text-align: left;
        color: #1E90FF;  /* DodgerBlue */
        font-size: 2.3em;
        margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<h1 class="title">🌤️ Aplikasi Prediksi Cuaca di Nusa Tenggara</h1>', unsafe_allow_html=True)
    st.subheader("Selamat datang di Aplikasi Prediksi Cuaca")

    # Penjelasan Singkat
    st.markdown("""
    Aplikasi ini didesain untuk memprediksi perubahan cuaca di berbagai kota di Nusa Tenggara. 
    Menggunakan metode **Support Vector Regression (SVR)** dan **Long Short-Term Memory (LSTM)**, aplikasi ini mampu melakukan proyeksi meteorologi berdasarkan data cuaca selama 43 tahun yang telah dikumpulkan.
    """)

    # Manfaat Penelitian
    st.subheader("1. Manfaat Aplikasi")
    st.markdown("""
    Aplikasi ini bermanfaat dalam meningkatkan kesadaran masyarakat tentang pentingnya pemantauan dan prediksi data meteorologi serta dampaknya terhadap kehidupan sehari-hari. 
    Dengan hasil prediksi ini, diharapkan masyarakat di Kota Nusa Tenggara dapat lebih siap menghadapi potensi cuaca ekstrem di masa depan, sehingga dapat meminimalkan risiko dan kerugian yang mungkin timbul.
    """)

    # Fitur Utama
    st.subheader("2. Fitur Utama")
    st.markdown("""
    - **Prediksi Cuaca dengan SVR dan LSTM**: Prediksi cuaca dilakukan berdasarkan parameter-parameter penting seperti temperatur, kelembapan, curah hujan, kecepatan angin, dan lainnya.
    - **Perbandingan Metode**: Aplikasi ini juga menampilkan perbandingan hasil prediksi dari dua metode, yaitu SVR dan LSTM, untuk memberikan gambaran lebih mendalam tentang akurasi model.
    - **Visualisasi**: Hasil prediksi disajikan dalam bentuk grafik untuk memudahkan interpretasi.
    """)

    # Data Cuaca yang Digunakan
    st.subheader("3. Dataset yang Digunakan")
    st.markdown("""
    Dataset cuaca yang digunakan mencakup data historis dari tahun 1980 hingga 2023 dengan berbagai parameter, termasuk:
    - Temperatur minimum, maksimum, dan rata-rata
    - Kelembapan rata-rata
    - Curah hujan
    - Lamanya penyinaran matahari
    - Kecepatan angin maksimum, rata-rata, dan arah angin
    """)

    # Teknologi yang Digunakan
    st.subheader("4. Teknologi yang Digunakan")
    st.markdown("""
    - **Support Vector Regression (SVR)**: Model regresi berbasis vektor pendukung yang digunakan untuk prediksi cuaca dengan tingkat akurasi tinggi, terutama pada data yang kompleks.
    - **Long Short-Term Memory (LSTM)**: Model jaringan saraf tiruan berbasis memori jangka panjang yang dioptimalkan untuk memproyeksikan data cuaca yang memiliki ketergantungan temporal.
    - **Streamlit**: Framework Python yang digunakan untuk membangun aplikasi web ini.
    """)

    # Penutup
    st.subheader("5. Siapa yang akan menggunakan aplikasi ini?")
    st.markdown("""
    Aplikasi ini dapat digunakan oleh masyarakat umum, terutama yang tinggal di Nusa Tenggara, untuk mendapatkan informasi tentang prediksi cuaca di masa depan. 
    Dengan menggunakan data historis, aplikasi ini membantu memberikan informasi yang lebih akurat tentang potensi cuaca ekstrem, yang berguna untuk persiapan dan mitigasi risiko.
    """)
    
    # Footer
    st.markdown(
    """
    <style>
    body {
        background-color: #121212;  /* Warna latar belakang gelap */
        color: #ffffff;  /* Warna teks putih */
    }

    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: rgba(18, 18, 18, 0.9);  /* Warna latar belakang footer dengan transparansi */
        text-align: center;
        padding: 10px;
        font-size: 12px;
        color: #ffffff;  /* Warna teks footer putih */
    }

    .custom-background {
        background-color: #1e1e1e;  /* Warna latar belakang untuk elemen tertentu */
        border-radius: 5px;  /* Sudut melengkung */
        padding: 10px;  /* Padding */
        box-shadow: 0 2px 5px rgba(255, 255, 255, 0.2);  /* Bayangan */
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    # Contoh penggunaan custom background
    # st.markdown('<div class="custom-background">Your content here</div>', unsafe_allow_html=True)

    # Footer
    st.markdown("<div class='footer'>© 2024 Weather Prediction. All rights reserved.</div>", unsafe_allow_html=True)
