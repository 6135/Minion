import asyncio
import platform
import psutil
import os
import discord
import re
from datetime import datetime
from dotenv import load_dotenv
from dotenv.main import find_dotenv
from MiniGames import RPS, CoinFlip

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
	pass

load_dotenv(find_dotenv())
BOT_TOKEN = os.getenv("BOT_TOKEN")
Jarvis().run(BOT_TOKEN) 