from datetime import datetime
import streamlit as st
import os
import pandas as pd
import plotly.graph_objects as go
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

def app():
    st.title("📊 Evaluasi Prediksi Cuaca")
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
            with st.spinner("Mengambil data historis..."):
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
    st.markdown("<div class='footer'>© 2024 Prediksi Cuaca. Semua hak cipta dilindungi.</div>", unsafe_allow_html=True)

def get_metrix_evaluation(selected_city, selected_model):
    model_directory = os.path.join(os.path.join(os.path.join(os.getcwd(), "data"), selected_city), selected_model + "_Metrics")
    
    print("Isi dari model_directory:", os.listdir(model_directory))
    
    dataframes = []
    filenames = []

    with st.spinner('Sedang memuat data...'):
        for item in os.listdir(model_directory):
            if item.endswith('.csv'):
                file_path = os.path.join(model_directory, item)
                df = pd.read_csv(file_path)
                df['Tanggal'] = pd.to_datetime(df['Tanggal'])
                dataframes.append(df)
                filenames.append(item)

    if not dataframes:
        st.warning("Tidak ada file CSV ditemukan di direktori kota yang dipilih.")
    return dataframes, filenames

def plot_all_predictions(dataframes, filenames):
    """Tampilkan Grafik Nilai Aktual vs Prediksi untuk semua DataFrame."""
    for df, filename in zip(dataframes, filenames):
        plot_predictions(df, filename)

def plot_predictions(df, filename):
    """Menampilkan Grafik Nilai Aktual vs Prediksi menggunakan Plotly."""
    fig = go.Figure()

    date_column = 'Tanggal'
    actual_column = df.columns[1]
    predicted_column = df.columns[2]
    
    display_name = filename.replace('.csv', '')

    fig.add_trace(go.Scatter(
        x=df[date_column],
        y=df[actual_column],
        mode='lines+markers',
        name=f'Nilai Aktual ({actual_column})',
        line=dict(color='green'),
        marker=dict(size=5),
        hovertemplate=f'{actual_column}: %{{y:.2f}}<br>Tanggal: %{{x}}<extra></extra>'
    ))

    fig.add_trace(go.Scatter(
        x=df[date_column],
        y=df[predicted_column],
        mode='lines+markers',
        name=f'Nilai Prediksi ({predicted_column})',
        line=dict(color='red', dash='dash'),
        marker=dict(size=5),
        hovertemplate=f'{predicted_column}: %{{y:.2f}}<br>Tanggal: %{{x}}<extra></extra>'
    ))

    fig.update_layout(
        title=f'Perbandingan Nilai Aktual vs Prediksi untuk {display_name}',
        xaxis_title='Tanggal',
        yaxis_title=display_name,
        legend_title='Legenda',
        template='plotly_dark',
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)
    
    y_actual = df[actual_column]
    y_predicted = df[predicted_column]
    mae = mean_absolute_error(y_actual, y_predicted)
    mse = mean_squared_error(y_actual, y_predicted)
    rmse = mse ** 0.5
    mape = (abs((y_actual - y_predicted) / y_actual).mean()) * 100
    cv = (np.std(y_actual) / np.mean(y_actual)) * 100
    # cv = (rmse / y_actual.mean()) * 100
    r2 = r2_score(y_actual, y_predicted)

    # Calculate evaluation metrics
    st.markdown(f"### Evaluasi untuk {display_name}")
    st.write(f"**Mean Absolute Error (MAE):** {mae:.2f}")
    st.write(f"**Mean Absolute Percentage Error (MAPE):** {mape:.2f}%")
    st.write(f"**Mean Squared Error (MSE):** {mse:.2f}")
    st.write(f"**Root Mean Squared Error (RMSE):** {rmse:.2f}")
    st.write(f"**Coefficient of Variation (CV):** {cv:.2f}%")
    st.write(f"**R² Score:** {r2:.2f}")
