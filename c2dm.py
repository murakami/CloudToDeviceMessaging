#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Import the Firebase service
import firebase_admin
from firebase_admin import messaging

default_app = firebase_admin.initialize_app()
print(default_app.name)

# This registration token comes from the client FCM SDKs.
registration_token = 'e0Ooby2iRM6SdOcW00HICq:APA91bGM0LWfv9UXzdFVRt3OyCCmR-Z1_mY3A8Fi_iVUeoh05T62lFONwlaxOrquRiexvJi94EPe8Hns3VurImiTGyltiU5HgwfLvYTfSKFt9zmSan1bJwY'


# See documentation on defining a message payload.
message = messaging.Message(
	notification=messaging.Notification(
		title='PTT',
		body='message',
	),
	data={
		'score': '850',
		'time': '2:45',
	},
	android=messaging.AndroidConfig(
		priority='high',
	),
	token=registration_token,
)

# Send a message to the device corresponding to the provided
# registration token.
response = messaging.send(message)
# Response is a message ID string.
print('Successfully sent message:', response)

# End Of File
