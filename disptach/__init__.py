import discord
from discord.ext import commands


@commands.command()
async def dispatch(ctx):
    embed = discord.Embed(
        title='Dispatch Notification',
        description='A dispatch has been initiated.',
        color=0x00f431
    )
    await ctx.send(embed=embed)
