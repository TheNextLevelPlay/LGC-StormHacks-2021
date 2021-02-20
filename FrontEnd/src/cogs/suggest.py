import discord
import json
import os
import sys
import requests

from components.post import postSuggest
from discord.ext import commands

directory = os.path.dirname(os.path.abspath(__file__))
listPath = os.path.join(directory, '../assets/list.json')

class Suggest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def suggest(self, ctx, *args):
        usrId = ctx.message.author.id
        query = str(args[0]).strip("\"")
        await ctx.send('<@{}> suggests: '.format(ctx.message.author.id) + query)
        postSuggest(query, usrId)

def setup(bot):
    bot.add_cog(Suggest(bot))