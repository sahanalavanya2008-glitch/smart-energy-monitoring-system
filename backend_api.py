from fastapi import FastAPI
from datetime import datetime
import sqlite3

app = FastAPI()

DATABASE = "energy_data.db"


def connect_db():
    return sqlite3.connect(DATABASE)


@app.get("/")
def home():
    return {
        "message": "Smart Energy Monitoring System API Running"
    }


@app.post("/energy")
def add_energy(device_id: str, usage: float, battery: int):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO energy_readings
        (device_id, energy_usage, battery_percentage, timestamp)
        VALUES (?, ?, ?, ?)
        """,
        (device_id, usage, battery, timestamp)
    )

    connection.commit()
    connection.close()

    return {
        "device_id": device_id,
        "energy_usage": usage,
        "battery": battery,
        "timestamp": timestamp
    }


@app.get("/energy")
def get_energy():

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM energy_readings")

    data = cursor.fetchall()

    connection.close()

    return data
