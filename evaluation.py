from datetime import datetime
import streamlit as st
import os
import pandas as pd
import plotly.graph_objects as go

def app():
    st.title("🌤️ Evaluasi Prediksi Cuaca")
    st.write("Selamat datang di halaman evaluasi prediksi cuaca! Di sini, Anda bisa melihat performa model prediksi cuaca menggunakan metode SVR dan LSTM. Pilih kota dan model untuk memulai.")

    # Tentukan direktori model
    model_directory = os.path.join(os.getcwd(), "data")

    # Menampilkan daftar kota dalam direktori model
    cities = [d for d in os.listdir(model_directory) if os.path.isdir(os.path.join(model_directory, d))]
    
    # Dropdown untuk memilih kota
    selected_city = st.selectbox("Pilih Kota", cities)
    
    # Dropdown untuk memilih model
    model_options = ["LSTM", "SVR"]
    selected_model = st.selectbox("Pilih Model Prediksi", model_options)

    with st.container():
        if st.button("Tampilkan Evaluasi"):
            historical_data, filenames = get_metrix_evaluation(selected_city, selected_model)
            # Tampilkan plot jika data berhasil dimuat
            if historical_data:
                plot_all_predictions(historical_data, filenames)
            else:
                st.warning("Tidak ada data tersedia untuk ditampilkan. Pastikan Anda telah memilih kota dan model yang benar.")

    # Gaya footer dan tampilan tambahan
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
        border-radius: 5px;  /* Sudut yang membulat */
        padding: 10px;  /* Padding */
        box-shadow: 0 2px 5px rgba(255, 255, 255, 0.2);  /* Efek bayangan */
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    # Footer
    st.markdown("<div class='footer'>© 2024 Prediksi Cuaca. Semua hak cipta dilindungi.</div>", unsafe_allow_html=True)

def get_metrix_evaluation(selected_city, selected_model):
    # Tentukan path ke direktori metrik pengujian
    model_directory = os.path.join(os.path.join(os.path.join(os.getcwd(), "data"), selected_city), selected_model + "_Metrics")
    
    # Cetak isi dari direktori model untuk debugging
    print("Isi dari model_directory:", os.listdir(model_directory))
    
    # Daftar untuk menyimpan DataFrame yang dimuat dan nama file
    dataframes = []
    filenames = []

    # Gunakan spinner saat memuat data
    with st.spinner('Sedang memuat data...'):
        # Memuat setiap file CSV dalam direktori
        for item in os.listdir(model_directory):
            if item.endswith('.csv'):
                file_path = os.path.join(model_directory, item)
                # Memuat file CSV ke dalam DataFrame
                df = pd.read_csv(file_path)
                
                # Pastikan 'Tanggal' adalah objek datetime
                df['Tanggal'] = pd.to_datetime(df['Tanggal'])
                # Tambahkan DataFrame dan nama file ke dalam daftar
                dataframes.append(df)
                filenames.append(item)  # Simpan nama file

    if not dataframes:
        st.warning("Tidak ada file CSV ditemukan di direktori kota yang dipilih.")
    return dataframes, filenames  # Kembalikan dataframes dan filenames

def plot_all_predictions(dataframes, filenames):
    """Tampilkan Grafik Nilai Aktual vs Prediksi untuk semua DataFrame."""
    for df, filename in zip(dataframes, filenames):
        plot_predictions(df, filename)

def plot_predictions(df, filename):
    """Menampilkan Grafik Nilai Aktual vs Prediksi menggunakan Plotly."""
    fig = go.Figure()

    # Asumsi kolom pertama adalah 'Tanggal', kedua adalah 'Aktual', dan ketiga adalah 'Prediksi'
    date_column = 'Tanggal'
    actual_column = df.columns[1]  # Asumsi kolom kedua adalah nilai aktual
    predicted_column = df.columns[2]  # Asumsi kolom ketiga adalah nilai prediksi
    
    display_name = filename.replace('.csv', '')

    # Tambahkan jejak Nilai Aktual
    fig.add_trace(go.Scatter(
        x=df[date_column],
        y=df[actual_column],
        mode='lines+markers',
        name=f'Nilai Aktual ({actual_column})',
        line=dict(color='green'),
        marker=dict(size=5),
        hovertemplate=f'{actual_column}: %{{y:.2f}}<br>Tanggal: %{{x}}<extra></extra>'
    ))

    # Tambahkan jejak Nilai Prediksi
    fig.add_trace(go.Scatter(
        x=df[date_column],
        y=df[predicted_column],
        mode='lines+markers',
        name=f'Nilai Prediksi ({predicted_column})',
        line=dict(color='red', dash='dash'),
        marker=dict(size=5),
        hovertemplate=f'{predicted_column}: %{{y:.2f}}<br>Tanggal: %{{x}}<extra></extra>'
    ))

    # Update tata letak dengan judul dan label yang dinamis
    fig.update_layout(
        title=f'Perbandingan Nilai Aktual vs Prediksi untuk {display_name}',
        xaxis_title='Tanggal',
        yaxis_title=display_name,  # Set label sumbu y menggunakan nama file
        legend_title='Legenda',
        template='plotly_dark',  # Gunakan template dark agar lebih sesuai dengan tema
        height=400
    )

    # Tampilkan plot di Streamlit
    st.plotly_chart(fig, use_container_width=True)
