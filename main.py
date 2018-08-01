import discord
import asyncio

client = discord.Client()
botkey = ""

@client.event
async def on_ready():
	print ("Logged in as:")
	print (client.user.name)

@client.event
async def on_message(message):
	if "blox" in message.content.lower():
		message = await client.send_message(message.channel, "OOF")

	elif "oofbot" in message.content.lower():
		message = await client.send_message(message.channel, "You called?")

	elif "robux" in message.content.lower():
		message = await client.send_message(message.channel, "$$$ https://www.roblox.com/upgrades/robux $$$")

client.run(botkey)
