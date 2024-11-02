import streamlit as st
from streamlit_option_menu import option_menu
import evaluation, preview, home, prediction

st.set_page_config(
    page_title="Meteorological Data Prediction in Nusa Tenggara",
    page_icon="🏪"
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
                        margin-bottom: -10px; /* Adjust this value to bring text closer to the menu */
                    }
                    hr {
                        border: 1px solid #333;
                        margin-top: 0px; /* Remove space above line */
                        margin-bottom: 10px; /* Adjust spacing as needed */
                    }
                </style>
                """, 
                unsafe_allow_html=True
            )
            
            st.markdown("<h2 class='sidebar-title'>🌦️ Weather Prediction</h2>", unsafe_allow_html=True)
            st.markdown("<hr>", unsafe_allow_html=True)
            
            app = option_menu(
                menu_title=None,
                options=["Homepage", "Preview Trend", "Prediction", "Evaluation"],
                icons=['house', 'bar-chart', 'cloud-sun', 'check-circle'],  # Updated icons
                default_index=0,
                styles={
                    "container": {"padding": "5!important"},
                    "nav-link-selected": {"background-color": "#1E3A8A"},
                }
            )
            
            # Content rendering based on selected option
            if app == "Homepage":
                st.markdown(
                    """
                    <div style="background-color: #333; padding: 15px; border-radius: 8px; border: 1px solid #444;">
                        <h2 style="text-align: center; color: #fff; font-size: 24px;">🌤️ Weather Prediction Homepage</h2>
                        <p style="text-align: center; font-size: 16px; color: #ddd;">
                            Welcome to the Weather Prediction App! Gain insights into meteorological data trends and forecasts for Nusa Tenggara.
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            elif app == "Prediction":
                st.markdown(
                    """
                    <div style="background-color: #333; padding: 15px; border-radius: 8px; border: 1px solid #444;">
                        <h2 style="text-align: center; color: #fff; font-size: 24px;">🌤️ Make Weather Predictions</h2>
                        <p style="text-align: center; font-size: 16px; color: #ddd;">
                            Leverage our advanced models to forecast weather conditions. Enter your parameters to get accurate predictions for Nusa Tenggara's climate.
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            elif app == "Preview Trend":
                st.markdown(
                    """
                    <div style="background-color: #333; padding: 15px; border-radius: 8px; border: 1px solid #444;">
                        <h2 style="text-align: center; color: #fff; font-size: 24px;">📈 Preview Weather Trends</h2>
                        <p style="text-align: center; font-size: 16px; color: #ddd;">
                            Explore historical weather patterns and trends for Nusa Tenggara. This section offers visual insights into past meteorological data to help understand evolving climate patterns.
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            elif app == "Evaluation":
                st.markdown(
                    """
                    <div style="background-color: #333; padding: 15px; border-radius: 8px; border: 1px solid #444;">
                        <h2 style="text-align: center; color: #fff; font-size: 24px;">📝 Model Evaluation</h2>
                        <p style="text-align: center; font-size: 16px; color: #ddd;">
                            Assess the accuracy and performance of our weather prediction models. Dive into the results to understand how well our forecasts align with actual data.
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        # Call the respective app function
        if app == "Homepage":
            home.app()
        elif app == "Preview Trend":
            preview.app()
        elif app == "Prediction":
            prediction.app()   
        elif app == "Evaluation":
            evaluation.app()    

# Create an instance of the MultiApp and run it
app = MultiApp()
app.run()
