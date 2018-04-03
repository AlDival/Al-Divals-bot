import random
import asyncio
import time
import os
import sys
import discord


client = discord.Client()

@client.event
async def on_message(message):
    if message.content == '!test':
        await client.send_message(message.channel, 'hello, ' + message.author.mention)
        print("Someone noticed me")





@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
print('------')


client.run('token')
