# 🚗 Driveway Organizer System

A Raspberry Pi-powered smart driveway manager designed for duplex apartments or multi-tenant homes. The system tracks parked cars using RF remotes and displays real-time positions on a local display and central dashboard.

## 🧠 Overview

Each apartment unit gets:
- A local Raspberry Pi (Zero 2 W or Pi 4)
- 433 MHz RF button(s) to mark parking changes
- Optional local display (e.g. HDMI screen or LED matrix)

All data syncs to a central web dashboard showing who is parked where, who is blocking who, and optionally sends notifications.

---

## 🧱 Project Structure

```plaintext
driveway-organizer/
├── README.md
├── .gitignore
├── backend/              # REST API & driveway logic
│   ├── app.py
│   ├── models.py
│   ├── db.py
│   ├── config.py
│   └── requirements.txt
├── local_pi/             # Code running on each Pi unit
│   ├── listener.py
│   ├── display.py
│   ├── cache.py
│   └── config.py
├── dashboard/            # Web interface
│   ├── index.html
│   ├── script.js
│   └── style.css
├── shared/               # Shared data formats / protocol
│   └── protocol.py
├── tests/                # Unit tests and mocks
│   ├── test_state_logic.py
│   └── mock_data.json
└── docker/               # Deployment configs
    ├── Dockerfile
    └── docker-compose.yml
