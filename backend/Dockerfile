
#-------------------------------------------------
#    File: backend/Dockerfile
#    Type: Dockerfile
#    Project: driveway-organizer
#    Author: urban
#    Created: 2024-06-20
#
#    Description: Dockerfile for backend service
#
#    Version --  Date  -- Author
#    1.0      2024-06-20  Kurban  
#-------------------------------------------------
    

FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
