
#-------------------------------------------------
#    File: local_pi/Dockerfile
#    Type: Dockerfile
#    Project: driveway-organizer
#    Author: urban
#    Created: 2024-06-20
#
#    Description: Dockerfile for local_pi service
#
#    Version --  Date  -- Author
#    1.0      2024-06-20  Kurban  
#-------------------------------------------------

FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "listener.py"]

