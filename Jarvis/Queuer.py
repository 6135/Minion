# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD`S API.
import os
import discord
from Models import Queue
from db import cnx
import re
# Import load_dotenv function from dotenv module.

class Queuer():
    def __init__(self,STARTING_SUBSTRING):
        self.STARTING_SUBSTRING = STARTING_SUBSTRING

    async def get(self,client,message): #>!QueuePlace @user
        mention_id = re.search('(<@!)([0-9]*)>',message.content)
        if mention_id is not None:
            mention_id = mention_id.group(2)
        else: 
            embed=discord.Embed(title="", description="You should mention whose queue you'd like to join.", color=0x80ff00)
            embed.add_field(name='Example:', value=f"{self.STARTING_SUBSTRING}peek <@!{message.author.id}>", inline=True)
            await message.channel.send(embed=embed)
            return 
        queue_id = f"{str(mention_id)}-{message.guild.id}"
        if self.exists(queue_id) and len(Queue(queue_id=queue_id).get_all()) > 0:
            list_members = f"The positions in <@!{mention_id}>'s queue are as follows:\n```md\n"
            all_members = Queue(queue_id=queue_id).get_all()
            member_pos = 1
            for member in all_members:
                member_id = member.memberID
                user_obj = client.get_user(int(member_id))
                member_row = f"{member_pos}.\t <{user_obj.name}>\n"
                list_members+=member_row
                member_pos+=1
            list_members+="\n```"
            await message.channel.send(list_members)
        else: await message.channel.send("The queue doesn't exist or is empty")

    async def create(self,client,message):
        sqlQuery = f"""
            DROP TABLE IF EXISTS `Queue-{message.author.id}-{message.guild.id}`"""
        cursor = cnx.cursor()
        cursor.execute(sqlQuery)
        sqlQuery = f"""
            CREATE TABLE `Queue-{message.author.id}-{message.guild.id}` (
            `id` int(11) NOT NULL,
            `memberID` varchar(64) NOT NULL,
            `priority` int(11) NOT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=latin1"""
        cursor = cnx.cursor()
        cursor.execute(sqlQuery)
        sqlQuery = f"""
            ALTER TABLE `Queue-{message.author.id}-{message.guild.id}`
            ADD PRIMARY KEY (`id`)"""     
        cursor = cnx.cursor()
        cursor.execute(sqlQuery)    
        sqlQuery = f"""
            ALTER TABLE `Queue-{message.author.id}-{message.guild.id}`
            MODIFY `id` int(11) NOT NULL AUTO_INCREMENT"""
        cursor = cnx.cursor()
        cursor.execute(sqlQuery)   
        await message.channel.send("Queue created. Have a nice day!")

    def exists(self,queue_id): #NOT A COMMAND
        cursor = cnx.cursor()
        sqlQuery = f"""
            SELECT COUNT(*)
            FROM information_schema.tables
            WHERE table_name = \'Queue-{queue_id}\'"""
        cursor.execute(sqlQuery)
        return cursor.fetchone()[0]==1

    async def put(self,client,message):
        mention_id = re.search('(<@!)([0-9]*)>',message.content)
        if mention_id is not None:
            mention_id = mention_id.group(2)
        else: 
            embed=discord.Embed(title="", description="You should mention whose queue you'd like to join.", color=0x80ff00)
            embed.add_field(name='Example:', value=f"{self.STARTING_SUBSTRING}joinqueue <@!{message.author.id}>", inline=True)
            await message.channel.send(embed=embed)
            return
        queue_id = f"{str(mention_id)}-{message.guild.id}"
        if self.exists(queue_id):
            if len(Queue(queue_id=queue_id).get(memberID=str(message.author.id))) > 0:
                await message.channel.send("You're already in this queue!")
            else:
                Queue(queue_id=queue_id,memberID=message.author.id,priority=1).save()
                position = len(Queue(queue_id=queue_id).get_all())
                await message.channel.send(f"You have joined the queue!, your spot is: {position}")
        else: await message.channel.send("The queue doesn't exist")
        return

    async def clear(self,client,message):
        sqlQuery = f"""
            DROP TABLE IF EXISTS `Queue-{message.author.id}-{message.guild.id}`"""
        cursor = cnx.cursor()
        cursor.execute(sqlQuery)
        sqlQuery = f"""
            CREATE TABLE `Queue-{message.author.id}-{message.guild.id}` (
            `id` int(11) NOT NULL,
            `memberID` varchar(64) NOT NULL,
            `priority` int(11) NOT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=latin1"""
        cursor = cnx.cursor()
        cursor.execute(sqlQuery)
        sqlQuery = f"""
            ALTER TABLE `Queue-{message.author.id}-{message.guild.id}`
            ADD PRIMARY KEY (`id`)"""     
        cursor = cnx.cursor()
        cursor.execute(sqlQuery)    
        sqlQuery = f"""
            ALTER TABLE `Queue-{message.author.id}-{message.guild.id}`
            MODIFY `id` int(11) NOT NULL AUTO_INCREMENT"""
        cursor = cnx.cursor()
        cursor.execute(sqlQuery)   
        await message.channel.send("Queue cleared. Have a nice day!")

    async def next(self,client,message):
        pass

    async def position_in_queue(self,client,message):
        pass
