# prediction.py
from datetime import datetime
import streamlit as st
import os
import pandas as pd
import plotly.graph_objects as go

def app():
    st.title("🌤️ Metrics Evaluation")
    st.write("This section displays the weather predictions using SVR and LSTM techniques.")

    # Define the model directory
    model_directory = os.path.join(os.getcwd(), "data")

    # List all directories (cities) in the model_directory
    cities = [d for d in os.listdir(model_directory) if os.path.isdir(os.path.join(model_directory, d))]
    
    # Dropdown for city selection
    selected_city = st.selectbox("Select City", cities)
    
    # Dropdown for model selection
    model_options = ["LSTM", "SVR"]
    selected_model = st.selectbox("Select Model", model_options)

    if st.button("Load Metrics"):
        with st.spinner('Loading metrics...'):
            historical_data = get_metrix_evaluation(selected_city, selected_model)
        
        if historical_data:
            # Only plot if there is data
            plot_all_predictions(historical_data)
            
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

def get_metrix_evaluation(selected_city, selected_model):
    # Define the path to the testing predictions directory
    model_directory = os.path.join(os.path.join(os.path.join(os.getcwd(), "data"), selected_city), selected_model + "_Metrics")
    
    # Print the contents of the model directory for debugging
    print("Contents of model_directory:", os.listdir(model_directory))
    
    # List to store loaded DataFrames
    dataframes = []

    # Load each CSV file in the directory
    for item in os.listdir(model_directory):
        if item.endswith('.csv'):
            file_path = os.path.join(model_directory, item)
            # Load the CSV file into a DataFrame
            df = pd.read_csv(file_path)
            
            # Ensure 'Tanggal' is a datetime object
            df['Tanggal'] = pd.to_datetime(df['Tanggal'])
            # Append the DataFrame to the list
            dataframes.append(df)

    if not dataframes:
        st.warning("No CSV files found in the selected city directory.")
    return dataframes

def plot_all_predictions(dataframes):
    """Plot Actual vs Predicted values for all DataFrames."""
    for df in dataframes:
        plot_predictions(df)

def plot_predictions(df):
    """Plot Actual vs Predicted values using Plotly."""
    fig = go.Figure()

    # Add Actual trace
    fig.add_trace(go.Scatter(
        x=df['Tanggal'],
        y=df['Actual'],
        mode='lines+markers',
        name='Actual',
        line=dict(color='green'),
        marker=dict(size=5),
        hovertemplate='Actual: %{y:.2f}<br>Tanggal: %{x}<extra></extra>'
    ))

    # Add Predicted trace
    fig.add_trace(go.Scatter(
        x=df['Tanggal'],
        y=df['Predicted'],
        mode='lines+markers',
        name='Predicted',
        line=dict(color='red', dash='dash'),
        marker=dict(size=5),
        hovertemplate='Predicted: %{y:.2f}<br>Tanggal: %{x}<extra></extra>'
    ))

    # Update layout
    fig.update_layout(
        title='Actual vs Predicted Values',
        xaxis_title='Tanggal',
        yaxis_title='Value',
        legend_title='Legend',
        template='plotly_white',
        height=400
    )

    # Show the plot in Streamlit
    st.plotly_chart(fig, use_container_width=True)
    
    