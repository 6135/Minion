import asyncio
import platform
import psutil
import os
import discord
import re
from datetime import datetime
from dotenv import load_dotenv
from dotenv.main import find_dotenv
from Commands import Commands
from MiniGames import RPS, CoinFlip
from Food import Food 
from Models import *
from Queuer import Queuer


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
		order = re.search("^("+STARTING_SUBSTRING+")([A-z]+)", message.content)
		
		if order is not None:
			order = order.group(2).casefold()
			funct = BOT_KEYWORDS.get(order)
			if funct is None:
				await message.channel.send("Your command seems incorrect, try `"+ STARTING_SUBSTRING + "help` for more details")
			else: 
				await funct(client=self,message=message)
				#await message.delete()
		
	@classmethod
	def STARTING_SUBSTRING(cls):
		return STARTING_SUBSTRING
	@classmethod
	def BOT_KEYWORDS(cls):
		return BOT_KEYWORDS

STARTING_SUBSTRING = ">!"

BOT_KEYWORDS = {
	'talkback': Commands(STARTING_SUBSTRING).talkback,
	'tb': Commands(STARTING_SUBSTRING).talkback,
	'hello': Commands(STARTING_SUBSTRING).hello,
	'rps': RPS().rockps,
	'rd': 3,
	'roll': 3,
	'rolldice': 3,
	'coin': CoinFlip().flip,
	'help': Commands(STARTING_SUBSTRING).help,
	'rb': Commands(STARTING_SUBSTRING).reactBack,
	'prune': Commands(STARTING_SUBSTRING).prune,
	'clean': Commands(STARTING_SUBSTRING).clean,
	'sysinfo': Commands(STARTING_SUBSTRING).sysintel,
	'food': Food().foods,
	'createqueue': Queuer(STARTING_SUBSTRING).create,
	'joinqueue': Queuer(STARTING_SUBSTRING).put,
	'peekqueue': Queuer(STARTING_SUBSTRING).get,
	'clearqueue': Queuer(STARTING_SUBSTRING).clear,
}

load_dotenv(find_dotenv())
BOT_TOKEN = os.getenv("BOT_TOKEN")
Jarvis().run(BOT_TOKEN) 