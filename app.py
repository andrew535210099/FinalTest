import streamlit as st
from streamlit_option_menu import option_menu
import evaluation, preview, home, prediction

st.set_page_config(
    page_title="Prediksi Data Meteorologi di Nusa Tenggara",
    page_icon="🌦️"
)

class MultiApp:
    
    def __init__(self):
        self.apps = []
    
    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })
    
    def run(self):
        with st.sidebar:
            st.markdown(
                """
                <style>
                    .sidebar-title {
                        text-align: center;
                        font-size: 70px;
                        margin-bottom: -10px; /* Mengatur jarak antara judul dan menu */
                    }
                    hr {
                        border: 1px solid #333;
                        margin-top: 0px;
                        margin-bottom: 10px;
                    }
                </style>
                """, 
                unsafe_allow_html=True
            )
            
            st.markdown("<h2 class='sidebar-title'>🌦️ Prediksi Cuaca</h2>", unsafe_allow_html=True)
            st.markdown("<hr>", unsafe_allow_html=True)
            
            app = option_menu(
                menu_title=None,
                options=["Beranda", "Tinjauan Tren", "Prediksi", "Evaluasi"],
                icons=['house', 'bar-chart', 'cloud-sun', 'check-circle'],  # Ikon yang diperbarui
                default_index=0,
                styles={
                    "container": {"padding": "5!important"},
                    "nav-link-selected": {"background-color": "#1E3A8A"},
                }
            )
            
            # Menampilkan konten berdasarkan pilihan menu
            if app == "Beranda":
                st.markdown(
                    """
                    <div style="background-color: #333; padding: 15px; border-radius: 8px; border: 1px solid #444;">
                        <h2 style="text-align: center; color: #fff; font-size: 24px;">🌤️ Selamat Datang di Halaman Prediksi Cuaca</h2>
                        <p style="text-align: center; font-size: 16px; color: #ddd;">
                            Aplikasi ini memberikan wawasan mengenai tren dan prediksi data meteorologi di Nusa Tenggara. Temukan data historis, tren, dan prediksi cuaca yang relevan untuk Anda.
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            elif app == "Prediksi":
                st.markdown(
                    """
                    <div style="background-color: #333; padding: 15px; border-radius: 8px; border: 1px solid #444;">
                        <h2 style="text-align: center; color: #fff; font-size: 24px;">🌤️ Buat Prediksi Cuaca</h2>
                        <p style="text-align: center; font-size: 16px; color: #ddd;">
                            Gunakan model canggih kami untuk meramalkan kondisi cuaca di Nusa Tenggara. Masukkan parameter yang diperlukan untuk mendapatkan prediksi yang akurat dan terkini.
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            elif app == "Tinjauan Tren":
                st.markdown(
                    """
                    <div style="background-color: #333; padding: 15px; border-radius: 8px; border: 1px solid #444;">
                        <h2 style="text-align: center; color: #fff; font-size: 24px;">📈 Tinjauan Tren Cuaca</h2>
                        <p style="text-align: center; font-size: 16px; color: #ddd;">
                            Jelajahi pola dan tren cuaca historis di Nusa Tenggara. Visualisasi ini membantu Anda memahami perubahan iklim yang sedang terjadi dengan melihat data cuaca masa lalu.
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            elif app == "Evaluasi":
                st.markdown(
                    """
                    <div style="background-color: #333; padding: 15px; border-radius: 8px; border: 1px solid #444;">
                        <h2 style="text-align: center; color: #fff; font-size: 24px;">📝 Evaluasi Model</h2>
                        <p style="text-align: center; font-size: 16px; color: #ddd;">
                            Lihat hasil evaluasi akurasi dan performa model prediksi cuaca kami. Pelajari bagaimana model kami membandingkan hasil prediksi dengan data aktual.
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        # Panggil fungsi aplikasi yang sesuai
        if app == "Beranda":
            home.app()
        elif app == "Tinjauan Tren":
            preview.app()
        elif app == "Prediksi":
            prediction.app()   
        elif app == "Evaluasi":
            evaluation.app()    

# Membuat instance dari MultiApp dan menjalankannya
app = MultiApp()
app.run()
