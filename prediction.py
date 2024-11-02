from datetime import datetime
from dateutil.relativedelta import relativedelta
import streamlit as st
import os
import pandas as pd
import plotly.graph_objects as go

def plot_predictions(data_historis, data_terpilih):
    """Plot data historis dan prediksi menggunakan Plotly untuk visualisasi yang lebih menarik."""
    
    # Kolom untuk prediksi LSTM dan SVR
    kolom_lstm = f'{data_terpilih} (LSTM)'
    kolom_svr = f'{data_terpilih} (SVR)'

    fig = go.Figure()

    # Menambahkan trace LSTM
    fig.add_trace(go.Scatter(
        x=data_historis['Tanggal'],
        y=data_historis[kolom_lstm],
        mode='lines+markers',
        name='LSTM',
        line=dict(color='orange', width=2),
        marker=dict(size=8, symbol='circle', color='orange', opacity=0.6),
        hovertemplate='LSTM: %{y:.2f} mm<br>Tanggal: %{x}<extra></extra>'
    ))

    # Menambahkan trace SVR
    fig.add_trace(go.Scatter(
        x=data_historis['Tanggal'],
        y=data_historis[kolom_svr],
        mode='lines+markers',
        name='SVR',
        line=dict(color='blue', width=2, dash='dash'),
        marker=dict(size=8, symbol='square', color='blue', opacity=0.6),
        hovertemplate='SVR: %{y:.2f} mm<br>Tanggal: %{x}<extra></extra>'
    ))

    # Update layout
    fig.update_layout(
        title=f'Prediksi {data_terpilih} dengan LSTM dan SVR',
        xaxis_title='Tanggal',
        yaxis_title=f'{data_terpilih} (mm)',
        legend_title='Model',
        hovermode='x unified',
        template='plotly_white',
        margin=dict(l=40, r=40, t=40, b=40),
        height=500
    )

    # Tampilkan grafik di Streamlit
    st.plotly_chart(fig, use_container_width=True)

def app():
    st.title("🌤️ Prediksi Cuaca")
    st.write("Aplikasi ini menampilkan prediksi cuaca menggunakan teknik SVR dan LSTM. Anda dapat membandingkan prediksi untuk berbagai kota dan rentang tanggal yang dipilih.")
    
    # Direktori Model
    model_directory = os.path.join(os.getcwd(), "data")

    # Daftar kota yang tersedia di direktori model
    cities = [d for d in os.listdir(model_directory) if os.path.isdir(os.path.join(model_directory, d))]
    
    # Dropdown untuk memilih kota
    selected_city = st.selectbox("Pilih Kota", cities)
    
    # Direktori model untuk kota yang dipilih
    city_model_directory = os.path.join(model_directory, selected_city)
    
    # Daftar file data yang tersedia
    model_files = ["Temperatur Minimum", "Temperatur Maksimum", "Temperatur Rata-rata", "Kelembapan Rata-rata", "Curah Hujan",
                    "Lamanya Penyinaran Matahari", "Kecepatan Angin Maksimum", "Arah Angin Saat Kecepatan Maksimum", "Kecepatan Angin Rata-rata"]
    
    if model_files:
        # Pilihan data yang akan diprediksi
        selected_data = st.multiselect("Pilih Data untuk Diprediksi", model_files)
        
        col1, col2 = st.columns(2)
        
        # Tanggal mulai default
        default_start_date = datetime(2024, 1, 1)
        
        with col1:
            start_date = st.date_input("Pilih Tanggal Mulai", value=default_start_date, min_value=default_start_date)

        # Tanggal akhir satu minggu setelah tanggal mulai
        end_date = start_date + relativedelta(days=7)

        # Input tanggal akhir dengan batasan minimum
        with col2:
            end_date = st.date_input("Pilih Tanggal Akhir", value=end_date, disabled=True)

        # Tombol untuk memulai prediksi
        with st.container():
            if st.button("Prediksi"):
                if not selected_data:
                    st.warning("Silakan pilih data yang ingin diprediksi.")
                    return  # Keluar dari fungsi jika tidak ada data yang dipilih
                
                # Periksa apakah kedua tanggal sudah dipilih
                if start_date and end_date:
                    # Buat rentang tanggal yang dibutuhkan untuk prediksi
                    date_range = pd.date_range(start=start_date, end=end_date)

                    # Periksa apakah rentang tanggal cukup panjang
                    if len(date_range) < 7:
                        st.warning("Silakan pilih rentang tanggal minimal 7 hari.")
                    else:
                        with st.spinner("Mengambil data historis..."):
                            data_historis = get_historical_data(selected_city, selected_data, start_date, end_date)  # Gunakan kota yang dipilih
                            
                            for data in selected_data:
                                plot_predictions(data_historis, data)
                else:
                    st.warning("Silakan pilih tanggal mulai dan tanggal akhir.")
    else:
        st.error("Tidak ada file model untuk kota yang dipilih.")
        
    # Footer
    st.markdown(
    """
    <style>
    body {
        background-color: #121212;
        color: #ffffff;
    }

    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: rgba(18, 18, 18, 0.9);
        text-align: center;
        padding: 10px;
        font-size: 12px;
        color: #ffffff;
    }

    .custom-background {
        background-color: #1e1e1e;
        border-radius: 5px;
        padding: 10px;
        box-shadow: 0 2px 5px rgba(255, 255, 255, 0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    # Footer
    st.markdown("<div class='footer'>© 2024 Prediksi Cuaca. Hak cipta dilindungi.</div>", unsafe_allow_html=True)

        
def get_historical_data(selected_city, keywords, start_date, end_date):
    """Mengambil data historis untuk kota dan model yang dipilih."""   
    # Direktori data historis kota yang dipilih
    model_directory = os.path.join(os.path.join(os.path.join(os.getcwd(), "data"), selected_city), "forecasting_data")
    
    # Daftar untuk menyimpan DataFrame
    dataframes = []

    # Tampilkan isi direktori model untuk debugging
    print("Isi dari model_directory:", os.listdir(model_directory))
    
    # Iterasi setiap kata kunci (model) dalam pilihan
    for keyword in keywords:
        # Mencari file Excel yang cocok dengan keyword
        for item in os.listdir(model_directory):
            if keyword in item and item.endswith('.xls'):
                print(f"Data cocok ditemukan untuk {keyword}") 
                file_path = os.path.join(model_directory, item)
                complete_data = pd.read_excel(file_path)
                complete_data['Tanggal'] = pd.to_datetime(complete_data['Tanggal'])

                # Konversi tanggal mulai dan akhir ke datetime
                start_date = pd.to_datetime(start_date)
                end_date = pd.to_datetime(end_date)

                # Filter data sesuai rentang tanggal yang dipilih
                filtered_data = complete_data[(complete_data['Tanggal'] >= start_date) & (complete_data['Tanggal'] <= end_date)]
                
                # Tambahkan DataFrame yang difilter ke daftar
                dataframes.append(filtered_data)
                break  # Keluar setelah menemukan kecocokan pertama untuk menghindari duplikasi

    # Gabungkan semua DataFrame dalam daftar
    if dataframes:
        combined_data = pd.concat(dataframes, ignore_index=True)
        return combined_data  # Kembalikan data yang sudah digabungkan
    else:
        print("Tidak ditemukan file yang cocok untuk kata kunci apa pun.")
        return None  # Kembalikan None jika tidak ada file yang ditemukan

