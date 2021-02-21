import discord
import json
import os
import sys
import requests

from components.post import postAsk
from discord.ext import commands

class Ask(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ask(self, ctx, *args):
        usrId = ctx.message.author.id
        query = str(args[0]).strip("\"")
        await ctx.send('<@{}> asked: '.format(ctx.message.author.id) + query)
        postAsk(query, usrId)


def setup(bot):
    bot.add_cog(Ask(bot))