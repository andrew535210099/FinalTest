from datetime import datetime
from dateutil.relativedelta import relativedelta
import streamlit as st
import os
import numpy as np
import pandas as pd
from keras.models import load_model
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

import plotly.graph_objects as go

def plot_predictions(historical_data, selected_data):
    """Plot historical data and predictions with Plotly for better aesthetics."""
    
    # Create traces for LSTM and SVR predictions
    lstm_column = f'{selected_data} (LSTM)'
    svr_column = f'{selected_data} (SVR)'

    fig = go.Figure()

    # Add LSTM trace
    fig.add_trace(go.Scatter(
        x=historical_data['Tanggal'],
        y=historical_data[lstm_column],
        mode='lines+markers',
        name='LSTM',
        line=dict(color='orange', width=2),
        marker=dict(size=8, symbol='circle', color='orange', opacity=0.6),
        hovertemplate='LSTM: %{y:.2f} mm<br>Tanggal: %{x}<extra></extra>'
    ))

    # Add SVR trace
    fig.add_trace(go.Scatter(
        x=historical_data['Tanggal'],
        y=historical_data[svr_column],
        mode='lines+markers',
        name='SVR',
        line=dict(color='blue', width=2, dash='dash'),
        marker=dict(size=8, symbol='square', color='blue', opacity=0.6),
        hovertemplate='SVR: %{y:.2f} mm<br>Tanggal: %{x}<extra></extra>'
    ))

    # Update layout
    fig.update_layout(
        title=f'Prediksi {selected_data} dengan LSTM dan SVR',
        xaxis_title='Tanggal',
        yaxis_title=f'{selected_data} (mm)',
        legend_title='Model',
        hovermode='x unified',
        template='plotly_white',
        margin=dict(l=40, r=40, t=40, b=40),
        height=500
    )

    # Show the plot in Streamlit
    st.plotly_chart(fig, use_container_width=True)

def app():
    st.title("🌤️ Weather Prediction")
    st.write("This application displays weather predictions using SVR and LSTM techniques. You can compare predictions for different cities and dates.")
    
    # Loaded Model
    # model_directory = os.getcwd() + "..\data\"
    # Define the model directory one level up
    model_directory = os.path.join(os.getcwd(), "data")

    # List all directories (cities) in the model_directory
    cities = [d for d in os.listdir(model_directory) if os.path.isdir(os.path.join(model_directory, d))]
    
    # Dropdown for city selection
    selected_city = st.selectbox("Select City", cities)
    
    # Construct the path for the selected city's model directory
    city_model_directory = os.path.join(model_directory, selected_city)
    
    # Find the first .h5 file in the selected city's model directory
    # model_files = [f for f in os.listdir(city_model_directory) if f.endswith('.csv')]
    model_files = ["Temperatur Minimum", "Temperatur Maksimum", "Temperatur Rata-rata", "Kelembapan Rata-rata", "Curah Hujan",
                    "Lamanya Penyinaran Matahari", "Kecepatan Angin Maksimum", "Arah Angin Saat Kecepatan Maksimum", "Kecepatan Angin Rata-rata"]
    
    if model_files:
        # Load the model
        selected_data = st.multiselect("Select Model", model_files)
        
        col1, col2 = st.columns(2)
        
        default_start_date = datetime(2024, 1, 1)
        
        with col1:
            start_date = st.date_input("Select Start Date",  value=default_start_date, min_value=default_start_date)

        # Hitung tanggal minimum untuk end_date (1 bulan setelah start_date)
        end_date = start_date + relativedelta(days=7)

        # Input tanggal akhir dengan batasan minimum
        with col2:
            end_date = st.date_input("Select End Date", value=end_date, disabled=True)

        # Tombol untuk memprediksi
        if st.button("Predict"):
            # Check if both dates are selected
            if start_date and end_date:
                # st.write(f"Predictions will be made for the date range: {start_date} to {end_date}")

                # Prepare the range of dates
                date_range = pd.date_range(start=start_date, end=end_date)

                # Ensure there are enough days to make predictions
                if len(date_range) < 7:
                    st.warning("Please select a date range of at least 30 days.")
                else:
                    with st.spinner("Fetching historical data..."):
                        historical_data = get_historical_data(selected_city, selected_data, start_date, end_date)  # Use the selected city
                        
                        for data in selected_data:
                            plot_predictions(historical_data, data)
                        
                        # plot_predictions(predictions_df)
            else:
                st.warning("Please select both start and end dates.")
    else:
        st.error("No model file found for the selected city.")
        
    
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

        
def get_historical_data(selected_city, keywords, start_date, end_date):
    """Fetch historical data for the selected city and models."""
    
    # Get the model directory and dataset directory
    model_directory = os.path.join(os.path.join(os.path.join(os.getcwd(), "data"), selected_city), "forecasting_data")
    
    # Initialize an empty list to store DataFrames
    dataframes = []

    # Display contents of the model_directory for debugging
    print("Contents of model_directory:", os.listdir(model_directory))
    
    # Iterate through each keyword (model) in the selection
    for keyword in keywords:
        # Look for Excel files matching the keyword
        for item in os.listdir(model_directory):
            if keyword in item and item.endswith('.xls'):
                print(f"Found matching data for {keyword}") 
                file_path = os.path.join(model_directory, item)
                complete_data = pd.read_excel(file_path)
                complete_data['Tanggal'] = pd.to_datetime(complete_data['Tanggal'])

                # Convert start_date and end_date to datetime
                start_date = pd.to_datetime(start_date)
                end_date = pd.to_datetime(end_date)

                # Filter the data for the specified date range
                filtered_data = complete_data[(complete_data['Tanggal'] >= start_date) & (complete_data['Tanggal'] <= end_date)]
                
                # Append the filtered DataFrame to the list
                dataframes.append(filtered_data)
                break  # Break after the first match to avoid duplicate matches

    # Concatenate all DataFrames in the list into a single DataFrame
    if dataframes:
        combined_data = pd.concat(dataframes, ignore_index=True)
        return combined_data  # Return the combined data
    else:
        print("No matching files found for any of the keywords.")
        return None  # Return None if no files were found
