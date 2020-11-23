import asyncio
import platform
import psutil
import os
import discord
import re
from datetime import datetime
from dotenv import load_dotenv
from dotenv.main import find_dotenv
from .MiniGames import RPS, CoinFlip
class Jarvis(discord.Client):

	async def on_ready(self):
		print('Logged on as', self.user, "on", datetime.now())

	async def on_message(self, message):
		if message.author == self.user:
			return
		if "jarvis?" in message.content.casefold():
			await message.channel.send("What do you need Sir?")
			return
		# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
		order = re.search("^("+self.STARTING_SUBSTRING+")([A-z]+)", message.content)
		
		if order is not None:
			order = order.group(2).casefold()
			funct = self.BOT_KEYWORDS.get(order)
			if funct == None:
				await message.channel.send("Your command seems incorrect, try `"+ self.STARTING_SUBSTRING + "help` for more details")
			
			elif funct.__name__ == "rockps":
				await message.delete()
				rps = RPS()
				await rps.rps(client=self, message=message)
			elif funct.__name__ == "flip":
				await message.delete()
				coin = CoinFlip()
				await coin.flip(client=self, message=message)
			else:
				await funct(self,message)
		

	async def talkback(self, message):
		await message.delete()
		tbSize = 8 + (len(self.STARTING_SUBSTRING))
		await message.channel.send(message.author.name + " said: \n >" + message.content[tbSize:])

	async def hello(self, message):
		await message.channel.send("hey :thumbsup: " + message.author.name)

	async def help(self, message):
		await message.delete()
		embed=discord.Embed(title="Help", description="Here's a list of all usefull commands at your disposal, all commands should start with `"+self.STARTING_SUBSTRING +"`", color=0x80ff00)
		embed.set_author(name="Jarvis")
		embed.add_field(name="`"+ self.STARTING_SUBSTRING +"talkback`", value="I will say whatever you said to me right back at you!", inline=False)
		embed.add_field(name="`"+ self.STARTING_SUBSTRING +"hello`", value="I respond with \"Hello\" right back!", inline=False)
		embed.add_field(name="`"+ self.STARTING_SUBSTRING +"rps`", value="Plays Rock Paper Scissors!", inline=False)
		embed.add_field(name="`"+ self.STARTING_SUBSTRING +"coin`", value="Flips a coin, bet with your friends!", inline=False)
		embed.add_field(name="`"+ self.STARTING_SUBSTRING +"prune X`", value="X is a number between 1 and 100, deletes said number of messages in that channel.\n\
						Requires user to have permission to manage messages in that channel", inline=False)
		embed.add_field(name="`"+ self.STARTING_SUBSTRING +"clean`", value="Removes all the bots messages in that channel.\n\
						Requires user to have permission to manage messages in that channel", inline=False)				
		embed.add_field(name="`"+ self.STARTING_SUBSTRING +"help`", value="I Think you know what this does...", inline=False)
		
		embed.set_footer(text="Jarvis is licensed under CC BY-NC 4.0")
		await message.channel.send(embed=embed)


	STARTING_SUBSTRING = ">!"
	BOT_KEYWORDS = {
		'talkback': talkback,
		'hello': hello,
		'rps': RPS.rockps,
		'rd': 3,
		'roll': 3,
		'rolldice': 3,
		'coin': CoinFlip.flip,
		'help': help,
		'rb': reactBack,
		'prune': prune,
		'clean': clean,
		'sysinfo': sysintel,
	}

load_dotenv(find_dotenv())
BOT_TOKEN = os.getenv("BOT_TOKEN")
Jarvis().run(BOT_TOKEN) 