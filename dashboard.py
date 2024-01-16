import streamlit as st
import requests
import streamlit.components.v1 as components

# Streamlit configuration
st.set_page_config(page_title="Traffic Management Dashboard", layout="wide")

# API Base URL
API_URL = "http://127.0.0.1:8000"

# Websocket connection for real-time traffic signal updates
WEBSOCKET_API_URL = "wss://echo.websocket.org"

# Create a Streamlit component to embed a custom HTML/Javascript component
traffic_signal_action = f"""
<div>
    <p>WebSocket Connection</p>
    <script>
        const socket = new WebSocket('{WEBSOCKET_API_URL}');

        socket.onmessage = (event) => {{
            const data = JSON.parse(event.data);
            console.log('Received data:', data);
            // Do something with the data
        }};
    </script>
</div>
"""

# Display the Streamlit component using st.markdown
st.markdown(traffic_signal_action, unsafe_allow_html=True)

# Streamlit components
st.title("Traffic Management Dashboard")

# Function to get real-time traffic data
def get_realtime_traffic_data():
    response = requests.post(f"{API_URL}/traffic/data")
    return response.json()

# Function to get traffic predictions
def get_traffic_prediction(traffic_data):
    response = requests.post(f"{API_URL}/traffic/predict", json=traffic_data)
    return response.json()["prediction"]

# Function to get system configuration
def get_system_config():
    response = requests.get(f"{API_URL}/config")
    return response.json()

# Display real-time traffic data
st.write("Real-time Traffic Data:")
realtime_data = get_realtime_traffic_data()
st.write(realtime_data)

# Display system configuration
st.write("System Configuration:")
config = get_system_config()
st.write(config)

# Display traffic signal action in real-time
st.write("Traffic Signal Action:")
st.write("No WebSocket Connection in Streamlit")  # Adjust this message as per your requirements
