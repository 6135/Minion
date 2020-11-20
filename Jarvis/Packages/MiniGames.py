import random
import discord
class RPS:
    async def rps(self,message):
        embed = discord.Embed(title="Rock, Paper, Scissor", description = "Choose a reaction to play the game!",color=0xa69ea8)
        rpsMsg=await message.channel.send(embed=embed)
        await rpsMsg.add_reaction("⛰")
        await rpsMsg.add_reaction("📰")
        await rpsMsg.add_reaction("✂")

    def jarvisChoice(self):
        random.choice("⛰","📰","✂")

    def gameResult(self,userChoice,jarvisChoice):
        if userChoice == "⛰" and jarvisChoice == "✂" or userChoice == "📰" and jarvisChoice == "⛰" or userChoice == "✂" and jarvisChoice == "📰":
            return "You won!"
        elif userChoice == jarvisChoice:
            return "It's a tie!"