import asyncio
import discord
import os

from discord.ext import commands, tasks
from random      import choice          as random_choice

from bot import BufatronBot

#TODO: pesquisas no google
#TODO: streaming de video -> API nao suporta
#TODO: streaming de musica

client = BufatronBot()

@client.listen()
async def on_ready():
    print('Logged in as')
    print(client.user)
    print('------')
    change_status.start()


@client.listen()
async def on_command_error(ctx, error):
    print(error)
    await ctx.send(f'Wow... The NERVE... You managed to break me, are you proud of yourself? Error {error}')

# @client.listen()
# async def on_message(message):
    
@tasks.loop(minutes = 5)
async def change_status():
    await client.change_presence(activity = discord.Game(random_choice(BufatronBot.status)))

for filename in os.listdir('src/cogs'):
    if not filename.startswith('wip_') and filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'Loaded {filename} as a cog.')

client.run(BufatronBot.token)
