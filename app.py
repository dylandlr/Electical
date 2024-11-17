import streamlit as st
import pandas as pd
import plotly.express as px
from preprocessing.preprocess import DataPreprocessor

# Initialize preprocessor
preprocessor = DataPreprocessor()

# Page config
st.set_page_config(
    page_title="Electical: 2024 Election Insights",
    page_icon="📊",
    layout="wide"
)

# Title and description
st.title("Electical: 2024 Election Insights")
st.markdown("Dashboard for visualizing predictions and analyses.")

# Sidebar
st.sidebar.header("Data Selection")
data_type = st.sidebar.selectbox(
    "Choose Data Source",
    ["Social Media Analysis", "Polling Data", "Stock Market Impact", "Election Results"]
)

# Main content
if data_type == "Social Media Analysis":
    st.header("Social Media Sentiment Analysis")
    st.info("Upload social media data to analyze sentiment trends")
    
    uploaded_file = st.file_uploader("Upload CSV file", type="csv")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file, low_memory=False)
        processed_data = preprocessor.process_social_media_data(data)
        
        # Display sentiment distribution
        fig = px.histogram(processed_data, x="sentiment_score", 
                          title="Sentiment Distribution")
        st.plotly_chart(fig)

elif data_type == "Polling Data":
    st.header("Polling Data Analysis")
    st.info("Upload polling data to visualize trends")
    
    uploaded_file = st.file_uploader("Upload CSV file", type="csv")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file, low_memory=False)
        processed_data = preprocessor.process_polling_data(data)
        st.write(processed_data)

elif data_type == "Stock Market Impact":
    st.header("Stock Market Analysis")
    st.info("Upload stock market data to analyze market trends")
    
    uploaded_file = st.file_uploader("Upload CSV file", type="csv")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file, low_memory=False)
        processed_data = preprocessor.process_stock_data(data)
        
        # Display stock trends
        fig = px.line(processed_data, x=processed_data.index, y=['close', 'MA5', 'MA20'],
                     title="Stock Price Trends")
        st.plotly_chart(fig)

else:  # Election Results
    st.header("Election Results Analysis")
    st.info("Upload election results data for analysis")
    
    uploaded_file = st.file_uploader("Upload CSV file", type="csv")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file, low_memory=False)
        processed_data = preprocessor.process_election_results(data)
        st.write(processed_data)