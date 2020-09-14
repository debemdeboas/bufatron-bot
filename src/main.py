import asyncio
import discord
import os
import sys

from discord.ext import commands, tasks
from random      import choice          as random_choice

from clear import *

_description = '''
Bufatron Bot

we wuz kangs
'''

#TODO: pesquisas no google
#TODO: streaming de video
#TODO: streaming de musica

class BufatronBot(commands.Bot):
    status = ['Destroying Gustavoland', 'Mamando a tua mãe']

client = BufatronBot(command_prefix = '$', description = _description)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user)
    print('------')
    change_status.start()


@client.event
async def on_command_error(ctx, error):
    print(error)

@client.command()
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit = amount)


@tasks.loop(seconds = 5)
async def change_status():
    next_status = random_choice(BufatronBot.status)
    print(client.activity, next_status)
    await client.change_presence(activity = discord.Game(next_status))

print(HELL)
token = os.getenv('BUFATRON_BOT_OAUTH_TOKEN')
print(token)
client.run(token)
