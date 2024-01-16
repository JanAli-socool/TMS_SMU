# main.py
from fastapi import FastAPI, WebSocket, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
import traci  # Import SUMO's TraCI library for communication

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return {"message": "Hello, this is the root endpoint!"}

# Model for traffic data
class TrafficData(BaseModel):
    location: str
    speed: float
    congestion: bool

# Websocket for real-time updates
class TrafficWebSocket(WebSocket):
    async def on_connect(self, websocket: WebSocket):
        await websocket.accept()

# Function to initialize SUMO simulation
def initialize_sumo():
    # Connect to SUMO and configure simulation
    traci.start(["sumo", "-c", "D:/project/Traffic_SMU/sumo_config_file.sumocfg"])

# Function to get adaptive traffic signal control action using reinforcement learning model
def get_traffic_signal_action():
    # Implement your reinforcement learning logic to determine the optimal signal phase
    # This can involve querying the current traffic state and using a trained model
    action = "phase_1_green"  # Replace with your logic
    return action

# Websocket endpoint for real-time traffic signal updates
@app.websocket("/traffic/signal")
async def traffic_signal_updates(websocket: WebSocket):
    await websocket.accept()
    initialize_sumo()
    while True:
        traffic_signal_action = get_traffic_signal_action()
        await websocket.send_text(traffic_signal_action)

# Add more endpoints as needed

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
