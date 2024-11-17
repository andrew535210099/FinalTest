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
    
    st.markdown('<h1 class="title">❄️ Analisis Data Cuaca Nusa Tenggara</h1>', unsafe_allow_html=True)
    st.subheader("Selamat Datang di Aplikasi Analisis Data Cuaca")

    # Penjelasan Singkat
    st.markdown("""
    Aplikasi ini dirancang untuk menganalisis data cuaca historis di wilayah Nusa Tenggara. 
    Dengan menggabungkan teknik analisis data modern dan model prediktif, aplikasi ini membantu memahami tren cuaca selama lebih dari empat dekade (1980–2023).
    """)

    # Tujuan dan Manfaat
    # st.subheader("1. Tujuan dan Manfaat")
    # st.markdown("""
    # Aplikasi ini bertujuan untuk:
    # - **Memahami Tren Cuaca Jangka Panjang**: Menyediakan analisis data historis untuk mengenali pola cuaca di Nusa Tenggara.
    # - **Menyediakan Wawasan untuk
    # Keputusan Strategis**: Hasil analisis dapat dimanfaatkan oleh peneliti, pembuat kebijakan, dan masyarakat umum untuk berbagai kebutuhan, seperti penelitian perubahan iklim atau mitigasi bencana.
    # """)
    
    st.subheader("1. Tujuan dan Manfaat")
    st.markdown("""
    Aplikasi ini memiliki tujuan utama untuk:
    - **Menilai Kinerja Model Prediksi Cuaca di Berbagai Kota**: Menguji sejauh mana akurasi model dalam memprediksi cuaca berdasarkan data historis di masing-masing kota di Nusa Tenggara, guna menentukan seberapa efektif model ini dalam konteks lokal.
    - **Menyediakan Informasi yang Mendalam untuk Pengambilan Keputusan Strategis**: Hasil evaluasi model dapat digunakan oleh peneliti, pembuat kebijakan, dan masyarakat umum untuk merumuskan kebijakan berbasis cuaca, memahami dampak perubahan iklim, serta merencanakan langkah-langkah mitigasi bencana yang lebih tepat.
    - **Memfasilitasi Perbandingan Kinerja Model antar Kota**: Menyediakan analisis perbandingan yang berguna untuk menilai kelebihan dan kekurangan model prediksi cuaca di berbagai wilayah, sehingga memungkinkan peningkatan akurasi prediksi untuk setiap kota.
    """)


    # Fitur Utama
    st.subheader("2. Fitur Utama")
    st.markdown("""
    - **Analisis Data Cuaca Historis**: Memberikan wawasan berbasis data untuk parameter cuaca seperti temperatur, curah hujan, dan kelembapan.
    - **Prediksi Cuaca Jangka Pendek**: Menggunakan metode seperti Support Vector Regression (SVR) dan Long Short-Term Memory (LSTM) untuk mengestimasi nilai parameter tertentu.
    - **Visualisasi Interaktif**: Grafik dan tabel untuk mendukung interpretasi hasil analisis dengan lebih mudah.
    """)

    # Data Cuaca yang Digunakan
    st.subheader("3. Dataset yang Digunakan")
    st.markdown("""
    Dataset mencakup data cuaca historis dari tahun 1980 hingga 2023, meliputi:
    - Temperatur (minimum, maksimum, dan rata-rata)
    - Kelembapan rata-rata
    - Curah hujan
    - Durasi penyinaran matahari
    - Kecepatan angin (maksimum dan rata-rata)
    - Arah angin saat kecepatan maksimum
    """)

    # Teknologi yang Digunakan
    st.subheader("4. Teknologi yang Digunakan")
    st.markdown("""
    - **Support Vector Regression (SVR)**: Digunakan untuk memodelkan hubungan linear maupun non-linear antara variabel cuaca, memberikan hasil prediksi yang akurat.
    - **Long Short-Term Memory (LSTM)**: Model berbasis jaringan saraf untuk data sekuensial, seperti tren cuaca historis.
    - **Streamlit**: Framework untuk membangun antarmuka aplikasi yang interaktif dan ramah pengguna.
    """)

    # Pengguna Utama
    st.subheader("5. Siapa yang Akan Menggunakan Aplikasi Ini?")
    st.markdown("""
    Aplikasi ini dirancang untuk:
    - **Peneliti dan Akademisi**: Untuk studi perubahan iklim, tren cuaca, atau penelitian lingkungan lainnya.
    - **Pemerintah dan Pembuat Kebijakan**: Untuk perencanaan strategis terkait mitigasi risiko bencana atau pengelolaan sumber daya alam.
    - **Masyarakat Umum**: Untuk mendapatkan wawasan tentang pola cuaca di wilayah mereka.
    """)
    
    # Footer
    st.markdown(
    """
    <style>
    body {
        background-color: #121212;  /* Latar belakang gelap */
        color: #ffffff;  /* Warna teks putih */
    }

    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: rgba(18, 18, 18, 0.9);  /* Transparansi */
        text-align: center;
        padding: 10px;
        font-size: 12px;
        color: #ffffff;  /* Warna teks putih */
    }

    .custom-background {
        background-color: #1e1e1e;  /* Latar belakang elemen */
        border-radius: 5px;
        padding: 10px;
        box-shadow: 0 2px 5px rgba(255, 255, 255, 0.2);  /* Bayangan */
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    st.markdown("<div class='footer'>© 2024 Nusa Tenggara Weather Analysis. All rights reserved.</div>", unsafe_allow_html=True)
