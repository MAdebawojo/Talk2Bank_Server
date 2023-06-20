FROM python:3.9
WORKDIR /bank
COPY Talk2Bank_Server /bank/Talk2Bank_Server
WORKDIR /bank/Talk2Bank_Server
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["./talk2bankServer/Scripts/python", "bankbot.py"]
