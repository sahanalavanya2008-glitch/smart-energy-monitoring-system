import random
import time
from datetime import datetime

devices = [
    "Powerwall_01",
    "SolarPanel_01",
    "EV_Charger_01"
]

while True:
    device = random.choice(devices)
    energy = round(random.uniform(1, 10), 2)
    battery = random.randint(20, 100)

    data = {
        "device_id": device,
        "energy_usage_kwh": energy,
        "battery_percentage": battery,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    print(data)

    time.sleep(5)
