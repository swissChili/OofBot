import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
	print ("Logged in as:")
	print (client.user.name)

@client.event
async def on_message(message):
	if "roblox" in message.content.lower():
		message = await client.send_message(message.channel, "OOF")

	elif "oofbot" in message.content.lower():
		message = await client.send_message(message.channel, "You called?")
		
	elif "robux" in message.content.lower():
		message = await client.send_message(message.channel, "$$$ https://www.roblox.com/upgrades/robux $$$")

client.run("NDQ5OTg1MDI0MTM4MjgwOTcw.DesowQ.Rk0Z8n8jBm3ynH8pZ2zsnF8Mw3U")