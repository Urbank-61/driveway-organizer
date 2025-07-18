"""**************************************************
    File: backend/models.py
    Type: Python
    Project: driveway-organizer
    Author: urban
    Created: 2024-06-20

    Description: Core logic for interpreting car 
    events and managing the driveway state (e.g. who
    is blocked, who can leave, etc.)

    Version --  Date  -- Author
    1.0      2024-06-20  Kurban  
**************************************************"""


from shared.protocol import CarStatus, CarEventType
from typing import Dict, List
from datetime import datetime

class DrivewayState:
    def __init__(self):
        # positions: 0 = front of driveway, 4 = back
        self.slots: Dict[int, CarStatus] = {}
        self.max_slots = 5  # Number of spots in your layout

    def handle_event(self, car_id: str, event_type: CarEventType) -> None:
        timestamp = datetime.now().isoformat()

        if event_type == CarEventType.ARRIVAL:
            self._add_car(car_id, timestamp)
        elif event_type == CarEventType.DEPARTURE:
            self._remove_car(car_id, timestamp)

    def _add_car(self, car_id: str, timestamp: str):
        if car_id in [c.car_id for c in self.slots.values()]:
            return  # Already parked

        for pos in range(self.max_slots):
            if pos not in self.slots:
                self.slots[pos] = CarStatus(
                    car_id=car_id,
                    position=pos,
                    event_type=CarEventType.ARRIVAL,
                    timestamp=timestamp
                )
                return

        print("Driveway full!")

    def _remove_car(self, car_id: str, timestamp: str):
        for pos, status in list(self.slots.items()):
            if status.car_id == car_id:
                del self.slots[pos]
                return

    def get_status(self) -> List[CarStatus]:
        return [self.slots[pos] for pos in sorted(self.slots.keys())]

    def who_is_blocked(self) -> Dict[str, List[str]]:
        # Simple logic: any car not in slot 0 is potentially blocked
        blocked_map = {}
        for pos, status in self.slots.items():
            if pos > 0:
                blockers = [self.slots[p].car_id for p in range(0, pos) if p in self.slots]
                if blockers:
                    blocked_map[status.car_id] = blockers
        return blocked_map
