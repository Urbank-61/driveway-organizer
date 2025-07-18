"""**************************************************
    File: backend/db.py
    Type: Python
    Project: driveway-organizer
    Author: urban
    Created: 2024-06-20

    Description: Interface with SQLite to store and
    query historical data and driveway status.

    Version --  Date  -- Author
    1.0      2024-06-20  Kurban  
**************************************************"""


import sqlite3
from typing import List
from shared.protocol import CarStatus, DrivewaySlot


DB_PATH = "driveway.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS car_status (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            slot TEXT NOT NULL,
            car_id TEXT NOT NULL,
            apartment_id TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


def insert_car_status(status: CarStatus):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO car_status (slot, car_id, apartment_id)
        VALUES (?, ?, ?)
    """, (status.slot.value, status.car_id, status.apartment_id))
    conn.commit()
    conn.close()


def get_latest_driveway_status() -> List[CarStatus]:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT slot, car_id, apartment_id, MAX(timestamp)
        FROM car_status
        GROUP BY slot
    """)
    rows = cur.fetchall()
    conn.close()
    return [
        CarStatus(
            slot=DrivewaySlot(slot),
            car_id=car_id,
            apartment_id=apartment_id
        )
        for slot, car_id, apartment_id, _ in rows
    ]
