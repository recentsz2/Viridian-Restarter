import time,sys,os
from discord_webhook import DiscordWebhook, DiscordEmbed
from configparser import ConfigParser



parser = ConfigParser()
parser.read('config/settings.ini')
(parser.sections())
wbh = (parser.get('Settings', 'Webhook'))
versatile = (parser.get('Settings', 'Reset_Time'))



webhook = DiscordWebhook(url=wbh)

embed = DiscordEmbed(title='Viridian Reset', description='Sucessfully Reset Viridian', color='03b2f8')

webhook.add_embed(embed)

def openFile():
    os.startfile('Cry.ConsoleApp.exe')


def closeFile():
    os.system('TASKKILL /F /IM Cry.ConsoleApp.exe')


while True:
  if os.path.exists("players.txt"):
    os.remove("players.txt")
  print("Players.txt Deleted")
  openFile()
  time.sleep(30)
  closeFile()
  if wbh.startswith('https://discordapp.com/api/webhooks'):
    print('Sending Webhook Message')
    response = webhook.execute()
else:
  print('No Webhook')