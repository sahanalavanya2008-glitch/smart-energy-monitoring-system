from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

energy_data = []

@app.get("/")
def home():
    return {
        "message": "Smart Energy Monitoring System API Running"
    }


@app.post("/energy")
def add_energy(device_id: str, usage: float, battery: int):

    data = {
        "device_id": device_id,
        "energy_usage_kwh": usage,
        "battery_percentage": battery,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    energy_data.append(data)

    return data


@app.get("/energy")
def get_energy():

    return energy_data
