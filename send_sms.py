import os
from twilio.rest import Client
import cv2

os.system("main.py") #import the blinking file

from main import Main


if (cv2.PutText == "No Eyes Detected" or "No face detected"):
    account_SID = []
    auth_token = []
    client = Client(account_SID, auth_token)

    message = client.messages \
        .create(
        body="The less you foam, the further away from Swaziland",
        from_='',
        to='+26876031890'
    )

    print(message.sid)
else :
    continue

