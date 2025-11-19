#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "25933223"))
API_HASH = environ.get("API_HASH", "6ef5a426d85b7f01562a41e6416791d3")
BOT_TOKEN = environ.get("BOT_TOKEN", "6554222504:AAGGbj-0VTPqJ4oHNWVf209F-_rKPQRIF9A")
OWNER = int(environ.get("OWNER", "5881684718"))
CREDIT = environ.get("CREDIT", "Rahul")
AUTH_USER = os.environ.get('AUTH_USERS', '5881684718').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

