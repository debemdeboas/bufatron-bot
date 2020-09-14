import discord

from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong')

    @commands.command()
    async def clear(self, ctx, amount : int = 10):
        await ctx.channel.purge(limit = amount + 1)

    @commands.command()
    async def show_server_info(self, ctx):
        guild   = ctx.guild
        message = []
        message.append(f'Server information for server {guild.name} (ID {guild.id}):')
        message.append(f'Owner: {guild.owner}')
        message.append(f'Members: {guild.member_count}')
        message.append(f'Server region: {guild.region}')
        message.append(f'Created at (UTC): {guild.created_at}')
        message.append(f'Server features: {guild.features}')
        message.append(f'Server categories: {guild.categories}')
        await ctx.send('\n'.join(message))



def setup(client):
    client.add_cog(Utility(client))
