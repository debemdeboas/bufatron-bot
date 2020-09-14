import discord

from discord.ext import commands

# i have no idea of what im doing here

class Audio(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def connect(self, ctx):
        voice_bot = await discord.VoiceClient.connect(self)

def setup(client):
    client.add_cog(Audio(client))
