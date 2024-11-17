from datetime import datetime
from dateutil.relativedelta import relativedelta
import streamlit as st
import os
import pandas as pd
import plotly.graph_objects as go

def plot_predictions(data_historis, data_terpilih):
    """Plot data historis, prediksi LSTM, SVR, dan data aktual menggunakan Plotly untuk visualisasi yang lebih menarik."""
    
    # Kolom untuk prediksi LSTM, SVR, dan data aktual
    kolom_lstm = f'{data_terpilih} (LSTM)'
    kolom_svr = f'{data_terpilih} (SVR)'
    kolom_actual = f'{data_terpilih} (Actual)'

    fig = go.Figure()

    # Menambahkan trace data aktual
    if kolom_actual in data_historis.columns:
        fig.add_trace(go.Scatter(
            x=data_historis['Tanggal'],
            y=data_historis[kolom_actual],
            mode='lines+markers',
            name='Actual Data',
            line=dict(color='green', width=2),
            marker=dict(size=8, symbol='diamond', color='green', opacity=0.7),
            hovertemplate='Actual: %{y:.2f} mm<br>Tanggal: %{x}<extra></extra>'
        ))

    # Menambahkan trace LSTM
    if kolom_lstm in data_historis.columns:
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
    if kolom_svr in data_historis.columns:
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
        title=f'Prediksi {data_terpilih} dengan LSTM, SVR, dan Data Aktual',
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
    st.title("🔮 Prediksi Cuaca")
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
        default_start_date = datetime(2015, 4, 14)
        
        max_start_date = datetime(2033, 12, 28)
        
        with col1:
            # start_date = st.date_input("Pilih Tanggal Mulai", value=default_start_date, min_value=default_start_date)
            start_date = st.date_input("Pilih Tanggal Mulai",  value=default_start_date, min_value=default_start_date, max_value=max_start_date
    )

        # Tanggal akhir maksimal 30 hari setelah tanggal mulai
        max_end_date = start_date + relativedelta(days=30)

        # Input tanggal akhir dengan batasan maksimum 30 hari
        with col2:
            end_date = st.date_input("Pilih Tanggal Akhir", value=start_date + relativedelta(days=7), min_value=start_date, max_value=max_end_date)

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

                    with st.spinner("Mengambil data historis..."):
                        data_historis = get_historical_data(selected_city, selected_data, start_date, end_date)
                        
                        if data_historis is not None:
                            print(data_historis)
                            for data in selected_data:
                                plot_predictions(data_historis, data)

                            # Link untuk mengunduh data mentah
                            csv = data_historis.to_csv(index=False).encode('utf-8')
                            st.download_button(
                                label="📥 Unduh Hasil Prediksi",
                                data=csv,
                                file_name=f"data_prediksi_{selected_city}_{start_date}_{end_date}.csv",
                                mime='text/csv'
                            )
                        else:
                            st.warning("Data tidak tersedia untuk rentang tanggal yang dipilih.")
                else:
                    st.warning("Silakan pilih tanggal mulai dan tanggal akhir.")
    else:
        st.error("Tidak ada file model untuk kota yang dipilih.")

def get_historical_data(selected_city, keywords, start_date, end_date):
    """Mengambil data historis untuk kota dan model yang dipilih."""   
    # Direktori data historis kota yang dipilih
    model_directory = os.path.join(os.path.join(os.path.join(os.getcwd(), "data"), selected_city), "forecasting_data")
    
    # Daftar untuk menyimpan DataFrame
    dataframes = []

    # Iterasi setiap kata kunci (model) dalam pilihan
    for keyword in keywords:
        # Mencari file Excel yang cocok dengan keyword
        for item in os.listdir(model_directory):
            if keyword in item and item.endswith('.xls'):
                file_path = os.path.join(model_directory, item)
                complete_data = pd.read_excel(file_path)
                complete_data['Tanggal'] = pd.to_datetime(complete_data['Tanggal'])

                # Konversi tanggal mulai dan akhir ke datetime
                start_date = pd.to_datetime(start_date)
                end_date = pd.to_datetime(end_date)

                # Filter data sesuai rentang tanggal yang dipilih
                filtered_data = complete_data[(complete_data['Tanggal'] >= start_date) & (complete_data['Tanggal'] <= end_date)]

                # Tambahkan kolom nama parameter dengan modelnya (LSTM atau SVR)
                filtered_data = filtered_data.rename(columns={
                    'Temperatur Minimum (LSTM)': f'{keyword} (LSTM)',
                    'Temperatur Minimum (SVR)': f'{keyword} (SVR)',
                    'Temperatur Minimum (Actual)': f'{keyword} (Actual)',  # Pastikan penamaan sesuai file
                })


                # Tambahkan DataFrame yang difilter ke daftar
                dataframes.append(filtered_data)

    # Gabungkan semua DataFrame dalam daftar dan gabungkan berdasarkan 'Tanggal'
    if dataframes:
        combined_data = pd.concat(dataframes, ignore_index=True)
        combined_data = combined_data.groupby('Tanggal', as_index=False).first()
        return combined_data  # Kembalikan data yang sudah digabungkan
    else:
        return None  # Kembalikan None jika tidak ada file yang ditemukan
