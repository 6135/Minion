# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import os
import discord
import re
# Import load_dotenv function from dotenv module.
from dotenv import load_dotenv
from dotenv.main import find_dotenv

# Loads the .env file that resides on the same level as the script.
load_dotenv(find_dotenv())
BOT_TOKEN = os.getenv("BOT_TOKEN")
# Grab the API token from the .env file.

class Jarvis(discord.Client):

	async def on_ready(self):
		print('Logged on as', self.user)

	async def on_message(self, message):
		if message.author == self.user:
			return
		# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
		order = re.search("^("+self.STARTING_SUBSTRING+")([A-z]*)", message.content)
		print(order)
		if order is not None:
			order = order.group(2).casefold()
			funct = self.BOT_KEYWORDS.get(order)
			if funct == None:
				await message.channel.send("Your command seems incorrect, try ```"+ self.STARTING_SUBSTRING + "help``` for more details")
			elif funct.__name__ == self.help.__name__:
				await message.channel.send(embed=funct(self,message))
			else: await message.channel.send(funct(self,message))
				
	def talkback(self, message):
		tbSize = 8 + (len(self.STARTING_SUBSTRING))
		return message.author.name + " said: \n >" + message.content[tbSize:]

	def hello(self, message):
		return "hey :thumbsup: " + message.author.name

	def help(self, message):
		embed=discord.Embed(title="Help", description="Here's a list of all help usefull commands at your disposal, all commands should start with `"+self.STARTING_SUBSTRING +"`", color=0x80ff00)
		embed.set_author(name="Jarvis")
		embed.add_field(name="`"+ self.STARTING_SUBSTRING +"talkback`", value="I will say whatever you said to me right back at you!", inline=False)
		embed.add_field(name="`"+ self.STARTING_SUBSTRING +"hello`", value="I respond with \"Hello\" right back!", inline=False)
		embed.add_field(name="`"+ self.STARTING_SUBSTRING +"help`", value="I Think you know what this does...", inline=False)
		embed.set_footer(text="Jarvis is licensed under CC BY-NC 4.0")
		return embed
		


	STARTING_SUBSTRING = ">!"
	BOT_KEYWORDS = {
		'talkback': talkback,
		'hello': hello,
		'rps': 2,
		'rd': 3,
		'roll': 3,
		'rolldice': 3,
		'coin': 4,
		'help': help,
	}

	 
# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot = Jarvis()
print(BOT_TOKEN)
bot.run(BOT_TOKEN) 