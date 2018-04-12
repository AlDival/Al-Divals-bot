import random
import asyncio
import time
import os
import sys
import discord
import requests
from lxml import html


client = discord.Client()

@client.event
async def on_message(message):
    if message.content.lower() == '!test':
        await client.send_message(message.channel, 'hello, ' + message.author.mention)
        print("Someone noticed me")
    
    elif message.content.lower() == '!help':
        await client.send_message(message.channel, message.author.mention + "\n```Commands:\n!test- Check if I am alive,\n!osu- Search the osu map database for a certain song,\n::- Random anime girl from Al's collection \n!Game- will play a short battle game, level up your char ```")
    
    elif message.content == '::':
        folder = os.listdir('./img')
        imgNo = folder[random.randint(0, len(folder))]
        await client.send_message(message.channel, message.author.mention)
        await client.send_file(message.channel, './img/'+imgNo)
    
    elif message.content.startswith('!osu'):
        print('Some one wants to play osu!')
        print(message.content)
        songName= message.content[5:]
        print(songName)
        url='https://osu.ppy.sh/beatmapsets?q='+songName
        response=requests.get(url)
        site = html.fromstring(response.content)
        SongList= site.xpath('//div[@class]/text()')
        print(SongList)

    elif message.content.startswith('!Game'):
        await 
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run('NDI0MTI4ODEwNDQ4MDYwNDE2.DarQQw.uQqN898PxT-jH_U8aAlP2dDkveA')

