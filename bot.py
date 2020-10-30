# bot.py
import os

import keys
import certifi
import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(keys.DISCORD_TOKEN)
