import sqlite3

connection = sqlite3.connect("energy_data.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS energy_readings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_id TEXT,
    energy_usage REAL,
    battery_percentage INTEGER,
    timestamp TEXT
)
""")

connection.commit()

connection.close()
