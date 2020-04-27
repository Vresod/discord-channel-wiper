# imports required for running.
import discord
# read tokenfile
with open("tokenfile", "r") as tokenfile:
		token=tokenfile.read()

print(token) # token is stored in plaintext but that shouldn"t be a problem

if token == "":
	print("Provide token in tokenfile")

client = discord.Client()

@client.event
async def on_ready():
		print("logged in as {0.user}".format(client))

@client.event
async def on_message(message):
		if message.author == client.user:
				return
		if message.content.startswith("$deleteall"):
				await message.channel.send("Deleting messages...")
				for i in range(1,3):
					messageid = message.channel.last_message_id
					deletemessage = await message.channel.fetch_message(messageid)
					await deletemessage.delete()
		if message.content.startswith("$check"):
			await message.channel.send(message.channel.id)

client.run(token)