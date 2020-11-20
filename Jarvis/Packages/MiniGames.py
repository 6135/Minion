import asyncio
import random
import discord


class RPS:
    async def rps(self,client,message):
        embed = discord.Embed(title="Rock, Paper, Scissor", description = "Choose a reaction to play the game!",color=0xa69ea8)
        rpsMsg=await message.channel.send(embed=embed)
        await rpsMsg.add_reaction("⛰")
        await rpsMsg.add_reaction("📰")
        await rpsMsg.add_reaction("✂")

        def check(reaction,user):
            return reaction.message.id==rpsMsg.id and user == message.author

        try:
            reaction, user = await client.wait_for('reaction_add',timeout=30.0,check=check)
        except asyncio.TimeoutError:
            await client.delete_message(message)
        else: 
            print(reaction)
            print(user)
            new_message = discord.Embed(title="Rock, Paper, Scissor", description = self.gameResult(reaction.emoji),color=0xa69ea8)
            await message.edit(content=new_message)
        

    def gameResult(self,userChoice):
        jarvisChoice=random.choice(["⛰","📰","✂"])
        if userChoice == "⛰" and jarvisChoice == "✂" or userChoice == "📰" and jarvisChoice == "⛰" or userChoice == "✂" and jarvisChoice == "📰":
            return "You won!"
        elif userChoice == jarvisChoice:
            return "It's a tie!"