import discord
import json
import os
import sys
import requests

from discord.ext import commands

directory = os.path.dirname(os.path.abspath(__file__))
listPath = os.path.join(directory, '../assets/list.json')

class Ask(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ask(self, ctx, *args):
        usrId = ctx.message.author.id
        query = str(args[0]).strip("\"")
        await ctx.send('<@{}> asked: '.format(ctx.message.author.id) + query)
        requests.post("http://localhost:8080/api/addSuggestion/" + str(usrId), data = query)


def setup(bot):
    bot.add_cog(Ask(bot))