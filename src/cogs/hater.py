import discord

from discord.ext import commands

class Hater(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.client.hated_list = []

    @commands.command()
    async def hate(self, ctx, hated):
        hated_id     = int(hated[3:-1])
        hated_member = ctx.guild.get_member(hated_id)
        self.client.hated_list.append(hated_member)
        await ctx.send(f'Added **{hated_member.name}** ({hated_member.mention}) to the naughties list.')

    @commands.command()
    async def show_hated(self, ctx):
        message = []
        message.append('**--- The naughties list ---**')
        [message.append(f'{member.name} ({member.mention})') for member in self.client.hated_list]
        await ctx.send('\n'.join(message))

def setup(client):
    client.add_cog(Hater(client))
