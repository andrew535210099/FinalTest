import os
import streamlit as st
from PIL import Image

def app():
    st.title("🌊 Tinjauan Tren Cuaca di Nusa Tenggara")
    
    # Set the directory for images
    image_directory = os.path.join(os.getcwd(), 'trendpage')
    
    # Check if the directory exists and get the list of image files
    if os.path.exists(image_directory):
        images = [f for f in os.listdir(image_directory) if f.endswith(('jpg', 'jpeg', 'png', 'gif'))]
        
        # Create two columns for displaying images
        cols = st.columns(2)

        # Loop through the images and display them in the columns
        for i, image_file in enumerate(images):
            image_path = os.path.join(image_directory, image_file)
            img = Image.open(image_path)
            
            # Remove "_trend.png" or similar suffix from the caption
            caption = image_file.replace('_trend.png', '').replace('_trend.jpg', '').replace('_trend.jpeg', '').replace('_trend.gif', '')

            # Display images in the appropriate column
            cols[i % 2].image(img, caption=caption, use_column_width=True)
    else:
        st.warning("Folder 'trendpage' tidak ditemukan. Silakan tambahkan gambar di dalam folder ini.")

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
