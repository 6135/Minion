# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import os
import discord
# Import load_dotenv function from dotenv module.
from dotenv import load_dotenv
from dotenv.main import find_dotenv
STARTING_SUBSTRING = ">!"
# Loads the .env file that resides on the same level as the script.
load_dotenv(find_dotenv())
BOT_TOKEN = os.getenv("BOT_TOKEN")
# Grab the API token from the .env file.

class Jarvis(discord.Client):
	
	async def on_message(self, message):
		print(message)
		# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
		if message.content.startswith(STARTING_SUBSTRING) and " hello" in message.content:
			# SENDS BACK A MESSAGE TO THE CHANNEL.
			await message.channel.send("hey :thumbsup:" + message.author.name)
			print("test")
		
	async def on_ready(self):
		print('Logged on as', self.user)
	 
# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot = Jarvis()
print(BOT_TOKEN)
bot.run(BOT_TOKEN) 