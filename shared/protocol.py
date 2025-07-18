"""**************************************************
    File: shared/protocol.py
    Type: Python
    Project: driveway-organizer
    Author: urban
    Created: 2024-06-20

    Description: Protocol definitions for communication
    between components; fomat CarStaus schema, 
    DrivewaySolt enum, and TimeStamp. shared between 
    backend/ and local_pi/ 

    Version --  Date  -- Author
    1.0      2024-06-20  Kurban  
**************************************************"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional
from datetime import datetime

class CarEventType(str, Enum):
    ARRIVAL = "arrival"
    DEPARTURE = "departure"
    TOGGLE = "toggle"  # Used by RF button if it only has 1 signal

"""
dataclass Truns this: 
    class CarStatus:
    def __init__(self, car_id, position, event_type, timestamp):
        self.car_id = car_id
        self.position = position
        self.event_type = event_type
        self.timestamp = timestamp
    + __repr_ and _eq_ methods
    into this:
"""
@dataclass
class CarStatus:
    car_id: str
    position: int                # Position in the driveway, 0 = curb, higher = further in
    event_type: CarEventType     # arrival / departure / toggle
    timestamp: str               # ISO format


@dataclass
class ParkingSpot:
    position: int
    occupied_by: Optional[str] = None  # car_id or None

@dataclass
class DrivewayState:
    spots: list[ParkingSpot]     # Current snapshot of driveway

@dataclass
class BlockageReport:
    car_id: str
    is_blocked: bool
    blocked_by: Optional[str] = None