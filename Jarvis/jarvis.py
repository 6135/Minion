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

async def sysintel(client, message):
	if message.author.id == 522010502138822666 or message.author.id == 362697372758966312:

		def get_size(bytes, suffix="B"):
			factor = 1024
			for unit in ["", "K", "M", "G", "T", "P"]:
				if bytes < factor:
					return f"{bytes:.2f}{unit}{suffix}"
				bytes /= factor
		uname = platform.uname()
		botRsp = "```"
		botRsp += f"="*5 + f"System Information" + f"="*5 +\
				f"\nSystem: {uname.system}\n" +\
				f"Node Name: N/A\n" +\
				f"Release: {uname.release}\n" +\
				f"Version: {uname.version}\n" +\
				f"Machine: {uname.machine}\n" +\
				f"Processor: {uname.processor}\n"
		boot_time_timestamp = psutil.boot_time()
		bt = datetime.fromtimestamp(boot_time_timestamp)
		cpufreq = psutil.cpu_freq()
		botRsp += f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}\n"
		botRsp += f"="*5 + f"CPU Information" + f"="*5 +"\n" +\
			f"Physical cores: {psutil.cpu_count(logical=False)}\n"+\
			f"Total cores: {psutil.cpu_count(logical=True)}\n"+\
			f"Max Frequency: {cpufreq.max:.2f}Mhz\n"+\
			f"Min Frequency: {cpufreq.min:.2f}Mhz\n"+\
			f"Current Frequency: {cpufreq.current:.2f}Mhz\n"

		svmem = psutil.virtual_memory()
		swap = psutil.swap_memory()
		botRsp += f"="*5 + f"Memory Information" + f"="*5 +"\n" +\
			f"Total: {get_size(svmem.total)}\n"+\
			f"Available: {get_size(svmem.available)}\n"+\
			f"Used: {get_size(svmem.used)}\n"+\
			f"Percentage: {svmem.percent}%\n"+\
			f"="*20 + f"SWAP" + f"="*20 +"\n" +\
			f"Total: {get_size(swap.total)}\n" +\
			f"Free: {get_size(swap.free)}\n"+\
			f"Used: {get_size(swap.used)}\n"+\
			f"Percentage: {swap.percent}%\n"

		await message.channel.send(botRsp+"```")
	else:
		await message.channel.send("You don't have permission to use this command")	
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