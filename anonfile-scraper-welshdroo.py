import string
import random
import requests
from discord_webhook import DiscordWebhook
from bs4 import BeautifulSoup
import time

WEBHOOK = '[DISCORD WEBHOOK HERE]'

def get_random_alphaNumeric_string(stringLength=8):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))

def build_url():
    base_url = "https://anonfile.com/"
    file_id = get_random_alphaNumeric_string(10)
    final_url = base_url + file_id
    return final_url

while True:
 response = requests.get(build_url())
 soup = BeautifulSoup(response.text, 'html.parser')

 last_links = soup.find(class_='AlphaNav')

 if response.status_code == 200:
  artist_name_list = soup.find(class_='row top-wrapper')
  artist_name_list_items = artist_name_list.find_all('h1')
  for artist_name in artist_name_list_items:
   names = artist_name.contents[0]
  webhook = DiscordWebhook(url=WEBHOOK, content=build_url()+" - "+names)
  response = webhook.execute()
 else:
  print("BAD - "+build_url())
  time.sleep(5)
