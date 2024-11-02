# prediction.py

import streamlit as st

def app():
    st.title("🌤️ Weather Preview Trend in Nusa Tenggara")
    st.subheader("Selamat datang di Aplikasi Prediksi Cuaca")
    
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
