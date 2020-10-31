# bot.py

import keys
import discord

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print('Connected servers:')
    for guild in client.guilds:
        print('-', guild.name, '(id:', guild.id, ')')
        print('-- Members:')
        for member in guild.members:
            print('---', member.name)

client.run(keys.DISCORD_TOKEN)