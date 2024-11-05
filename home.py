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
    Aplikasi ini bertujuan untuk membantu masyarakat dan peneliti dalam memahami pola dan tren perubahan cuaca di berbagai kota di Nusa Tenggara. 
    Memanfaatkan metode **Support Vector Regression (SVR)** dan **Long Short-Term Memory (LSTM)**, aplikasi ini menawarkan proyeksi kondisi meteorologi berdasarkan analisis data cuaca historis selama 43 tahun. 
    """)
    
    # Manfaat dan Tujuan Aplikasi
    st.subheader("1. Tujuan dan Manfaat Aplikasi")
    st.markdown("""
    Aplikasi ini memiliki beberapa tujuan utama:
    - **Memprediksi dan Mengantisipasi Cuaca Ekstrem**: Dengan memberikan informasi prediksi, aplikasi ini diharapkan membantu masyarakat dalam merencanakan aktivitas dan persiapan menghadapi potensi cuaca ekstrem.
    - **Pendukung Riset dan Kebijakan Iklim**: Data historis dan prediksi yang dihasilkan dapat digunakan sebagai dasar ilmiah dalam penelitian perubahan iklim dan membantu pembuat kebijakan untuk merancang langkah-langkah mitigasi dan adaptasi di daerah Nusa Tenggara.
    """)

    # Fitur Utama
    st.subheader("2. Fitur Utama")
    st.markdown("""
    - **Prediksi Cuaca Berdasarkan Parameter Meteorologi**: Menggunakan SVR dan LSTM untuk memberikan prediksi yang akurat berdasarkan parameter seperti temperatur, kelembapan, curah hujan, dan kecepatan angin.
    - **Perbandingan Metode Prediksi**: Menyediakan perbandingan antara SVR dan LSTM untuk memberikan wawasan lebih dalam mengenai akurasi prediksi.
    - **Visualisasi Data**: Menampilkan hasil prediksi dalam grafik untuk kemudahan interpretasi dan analisis.
    """)

    # Data Cuaca yang Digunakan
    st.subheader("3. Dataset yang Digunakan")
    st.markdown("""
    Dataset mencakup data cuaca historis dari tahun 1980 hingga 2023, yang terdiri dari:
    - Temperatur minimum, maksimum, dan rata-rata
    - Kelembapan rata-rata
    - Curah hujan
    - Lamanya penyinaran matahari
    - Kecepatan angin maksimum, rata-rata, dan arah angin
    """)

    # Teknologi yang Digunakan
    st.subheader("4. Teknologi yang Digunakan")
    st.markdown("""
    - **Support Vector Regression (SVR)**: Model regresi yang mampu memberikan prediksi presisi tinggi untuk data yang kompleks.
    - **Long Short-Term Memory (LSTM)**: Model jaringan saraf tiruan yang dioptimalkan untuk data sekuensial, cocok untuk proyeksi tren cuaca jangka panjang.
    - **Streamlit**: Framework yang digunakan untuk membangun antarmuka web aplikasi ini, membuatnya mudah diakses dan interaktif.
    """)

    # Pengguna Utama
    st.subheader("5. Siapa yang akan menggunakan aplikasi ini?")
    st.markdown("""
    Aplikasi ini dirancang untuk:
    - **Masyarakat umum** di Nusa Tenggara yang membutuhkan informasi cuaca untuk aktivitas sehari-hari.
    - **Peneliti dan Akademisi** yang memerlukan data prediksi cuaca sebagai bagian dari studi perubahan iklim atau riset lingkungan.
    - **Pembuat kebijakan dan pihak terkait** yang memerlukan data cuaca dalam menyusun strategi mitigasi dan adaptasi terhadap perubahan iklim.
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

    # Footer
    st.markdown("<div class='footer'>© 2024 Weather Prediction. All rights reserved.</div>", unsafe_allow_html=True)
