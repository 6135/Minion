import discord

class Food:
    foods = ['Hamburguer','Pizza','Cinnamon Rolls','Lasagna']
    async def food(self,message): 
        cmd = message.content.split()
        
        if 'add' in message.content:
            add = cmd[cmd.index('add')+1] 
            if add is not None and add not in Food.foods:
                Food.foods.append(add)
            else:
                embed = discord.Embed(title="Foods",description= "No food to add or food already added!",color=0xa69ea8)
                await message.channel.send(embed=embed)
        else:
            d = ''
            for f in Food.foods: d+=f+"\n"
            embed = discord.Embed(title="Foods",description= d,color=0xa69ea8)
            await message.channel.send(embed=embed)