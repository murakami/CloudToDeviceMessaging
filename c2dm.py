#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os

# Import the Firebase service
import firebase_admin
from firebase_admin import messaging

from datetime import datetime

# env
# GOOGLE_CLOUD_PROJECT
# GOOGLE_APPLICATION_CREDENTIALS
default_app = firebase_admin.initialize_app()
print(default_app.name)

now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

# This registration token comes from the client FCM SDKs.
registration_token = os.environ['TOKEN']
print(registration_token)

# See documentation on defining a message payload.
message = messaging.Message(
	notification=messaging.Notification(
		title='PTT',
		body=formatted_date,
	),
	data={
		'voice_ping_router': 'wss://router-lite.voiceping.info',
		'group_id': 'bitz',
		'user_id': 'demo',
		'message': formatted_date,
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
