from genericpath import exists
import time,os,sys
from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = ('https://discord.com/api/webhooks/984204763090550814/mBDSMlFFFrBkauQOiIO8hI4H9lQO7CjDSNmEKeJCXYQ_S1PwvCBnFFPDgzIcqKzOPpRh')

if os.path.exists('Cry.ConsoleApp.exe'):
    print('Viridian ConsoleApp Detected')
else:
    print('viridian file not found move')
    

webhook = DiscordWebhook(url=webhook)
#HEX CODE COLORS
embed = DiscordEmbed(title='Viridian Restarted', description='Sucessfully Restarted', color='00B6FF')
webhook.add_embed(embed)




while True:
    os.startfile('Cry.ConsoleApp.exe')
    print('Starting Viridian')
    #3600 is an hour
    time.sleep(3600)
    os.system('TASKKILL /F /IM Cry.ConsoleApp.exe')
    if os.path.exists('players.txt'):
        os.remove('players.txt')
        response = webhook.execute()