import asyncio
import random
import discord
class RPS:
    async def rockps(self,client,message):
        embed = discord.Embed(title="Rock, Paper, Scissor", description = "Choose a reaction to play the game!",color=0xa69ea8)
        rpsMsg=await message.channel.send(embed=embed)
        await rpsMsg.add_reaction("⛰")
        await rpsMsg.add_reaction("📰")
        await rpsMsg.add_reaction("✂")
        await rpsMsg.add_reaction("♻")

        def checkRPS(reaction,user):
            return reaction.message.id==rpsMsg.id and user == message.author and reaction.emoji in ["⛰","📰","✂","♻"]

        try:
            reaction, user = await client.wait_for('reaction_add',timeout=60.0,check=checkRPS)
            
        except asyncio.TimeoutError:
            pass
        else:
            
            if reaction.emoji == "♻":
                await rpsMsg.delete() 
                await self.rockps(client,message) 
            else:
                jarvisChoice=random.choice(["⛰","📰","✂"])
                new_embed = discord.Embed(title=self.gameResult(reaction.emoji,jarvisChoice), description = reaction.emoji+" vs "+jarvisChoice,color=0xa69ea8)
                await rpsMsg.edit(embed=new_embed)
              
            
            
           
            
           
    def gameResult(self,userChoice,jarvisChoice):        
        if userChoice == "⛰" and jarvisChoice == "✂" or userChoice == "📰" and jarvisChoice == "⛰" or userChoice == "✂" and jarvisChoice == "📰":
            return "You won!"
        elif userChoice == jarvisChoice:
            return "It's a tie!"
        else:
            return "You lost!"


class CoinFlip:
    async def flip(self,client,message):
        choice = random.choice(["Heads!", "Tails!"])
        embed = discord.Embed(title="Coin Flip!", description = "It was... " + choice ,color=0xa69ea8)
        msgEmbed = await message.channel.send(embed=embed)
        await msgEmbed.add_reaction("♻")

        def checkflip(reaction,user):
            return reaction.message.id == msgEmbed.id and user == message.author and reaction.emoji == "♻"

        try:
            reaction, user = await client.wait_for('reaction_add',timeout=30.0,check=checkflip)
        except asyncio.TimeoutError:
            pass
        else:
            await msgEmbed.delete() 
            await self.flip(client,message)

 