"""**************************************************
    File: backend/app.py
    Type: Python
    Project: driveway-organizer
    Author: urban
    Created: 2024-06-20

    Description: REST API or FastAPI server to handle
    external communication.

    Version --  Date  -- Author
    1.0      2024-06-20  Kurban  
**************************************************"""


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from backend import db
from shared.protocol import CarStatus, DrivewaySlot

app = FastAPI(title="Driveway Organizer API")

# Initialize DB when server starts
@app.on_event("startup")
def startup():
    db.init_db()


# API model for POST requests
class CarStatusRequest(BaseModel):
    slot: DrivewaySlot
    car_id: str
    apartment_id: str


@app.post("/update")
async def update_status(status: CarStatusRequest):
    try:
        car_status = CarStatus(
            slot=status.slot,
            car_id=status.car_id,
            apartment_id=status.apartment_id
        )
        db.insert_car_status(car_status)
        return {"message": "Status updated"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/status", response_model=List[CarStatusRequest])
async def get_status():
    return db.get_latest_driveway_status()
