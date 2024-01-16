# Smart Traffic Management System

This project implements a Smart Traffic Management System using Python, FastAPI, and Streamlit. The system includes a server for handling traffic data, making predictions, and providing real-time updates, and a Streamlit dashboard for visualization.

## Prerequisites

Before running the project, make sure you have the following installed:

- Python (>=3.6)
- [Sumo](https://www.eclipse.org/sumo/) - Simulation of Urban MObility (Traffic Simulator)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Streamlit](https://streamlit.io/)

## Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/traffic-management-system.git
cd traffic-management-system
```
2. Create a virtual environment (optional but recommended):

```bash
# On Windows
python -m venv smu_ven
.\smu_ven\Scripts\activate

# On Unix or MacOS
python -m venv smu_ven
source smu_ven/bin/activate
```

3. Install Dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project:

1. Start the Sumo simulation:

   ```bash
   sumo-gui -c path/to/your/sumo_config_file.sumocfg


   ```
2. Start the FastAPI server:

```bash
uvicorn main:app --reload

```

3. In a separate terminal, run the Streamlit dashboard:

```bash
streamlit run dashboard.py
```

