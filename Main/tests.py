from django.test import TestCase

# Create your tests here.
import requests
from UzbegimProject import settings
from tokens import *


host = settings.ALLOWED_HOSTS[0]
api_url = f"https://api.telegram.org/bot{tokenlist['uzbegim']}/setWebhook?url=https://{host}/api"
r = requests.get(api_url)
print(r)