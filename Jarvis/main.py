# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import asyncio
import os
import discord
import re
from discord.colour import Color
# Import load_dotenv function from dotenv module.
from dotenv import load_dotenv
from dotenv.main import find_dotenv
from Packages.MiniGames import RPS, coinFlip
# Loads the .env file that resides on the same level as the script.
load_dotenv(find_dotenv())
BOT_TOKEN = os.getenv("BOT_TOKEN")


# Grab the API token from the .env file.

async def reactBack(client,message):
	embed=discord.Embed(title="React to this message", color=0x80ff00)
	embed.set_author(name="Jarvis - RB")
	msgEmbed = await message.channel.send(embed=embed)

	def checkReactBack(reaction,user):
		return reaction.message.id == msgEmbed.id and\
			   client.user == reaction.message.author and\
			   "Jarvis - RB" == reaction.message.embeds[0].author.name and\
				user == message.author
	try:
		reaction, user = await client.wait_for('reaction_add', timeout=60.0,check=checkReactBack)
	except asyncio.TimeoutError:
		await message.channel.send("You took to long to react!")
	else: await message.channel.send("❤")

async def prune(client,message):
	num = re.search("("+Jarvis().STARTING_SUBSTRING+")([A-z]+)( [0-9]+|[0-9]+|)", message.content).group(3)
	if num != '' and int(num) < 101 and int(num) > 0:
		user_perms = message.author.permissions_in(message.channel)
		if user_perms.manage_messages is True:
			await message.delete()
			await message.channel.purge(limit=int(num))
		else: await message.channel.send("You dont have permissions to run this command!")
	else: await message.channel.send("Woah there! You need to choose a number between 1 and 100, like this `prune100`")

async def clean(client,message):
	channel = message.channel
	def is_me(m):
		return m.author == client.user

	if message.author.permissions_in(message.channel).manage_messages is True:
		await message.delete()
		await channel.purge(limit=100, check=is_me)
	else: await message.channel.send("You dont have permissions to run this command!")
class Jarvis(discord.Client):

	async def on_ready(self):
		print('Logged on as', self.user)

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
			
			elif funct.__name__ == "rps":
				await message.delete()
				rps = RPS()
				await rps.rps(client=self, message=message)
			elif funct.__name__ == "coinFlip":
				await message.delete()
				coin = coinFlip()
				await coin.coinFlip(client=self, message=message)
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
		'rps': RPS.rps,
		'rd': 3,
		'roll': 3,
		'rolldice': 3,
		'coin': coinFlip.coinFlip,
		'help': help,
		'rb': reactBack,
		'prune': prune,
		'clean': clean,
	}



# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot = Jarvis()
bot.run(BOT_TOKEN) 