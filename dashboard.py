import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Titanic Dashboard", layout="centered")

st.title("🚢 Kaggle: Titanic Survival Dashboard")
st.write("This dashboard pulls live data from our local FastAPI server, which was populated by our ETL script.")

# Fetch data from our own API
try:
    response = requests.get("http://127.0.0.1:8000/survival-by-class")
    data = response.json()
    
    # Convert JSON to a Pandas DataFrame for the chart
    df = pd.DataFrame(list(data.items()), columns=["Passenger Class", "Survival Rate (%)"])
    
    # Draw the UI
    st.subheader("Survival Rate by Ticket Class")
    st.bar_chart(df.set_index("Passenger Class"))
    
    st.success("API Connection Successful!")

except Exception as e:
    st.error("⚠️ Make sure the FastAPI server is running!")