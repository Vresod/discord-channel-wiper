# imports required for running.
import discord
# read file
with open('tokenfile', 'r') as tokenfile:
		token=tokenfile.read()

print(token) # token is stored in plaintext but that shouldn't be a problem

if token == "":
	print("Provide token in tokenfile")

class MyClient(discord.Client):
		async def on_ready(self):
				print('Logged on as {0}!'.format(self.user))

		async def on_message(self, message):
				print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run(token)