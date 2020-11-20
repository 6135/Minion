# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import os
import discord
# Import load_dotenv function from dotenv module.
from dotenv import load_dotenv
from dotenv.main import find_dotenv

# Loads the .env file that resides on the same level as the script.
load_dotenv(find_dotenv())
BOT_TOKEN = os.getenv("BOT_TOKEN")
# Grab the API token from the .env file.

class Jarvis(discord.Client):
	
	async def on_message(self, message):
		# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
		if message.content == "hello":
			# SENDS BACK A MESSAGE TO THE CHANNEL.
			await message.channel.send("hey dirtbag")
	async def on_ready(self):
		print('Logged on as', self.user)
	 
# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot = Jarvis()
print(BOT_TOKEN)
bot.run(BOT_TOKEN)