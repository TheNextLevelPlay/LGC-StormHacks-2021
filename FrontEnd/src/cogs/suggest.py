import discord
import json
import os
import sys
import requests

from components.post import postSuggest
from discord.ext import commands

class Suggest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def suggest(self, ctx, *args):
        if ctx.message.guild:
            if len(args) == 1:
                usrId = ctx.message.author.id
                query = str(args[0]).strip("\"")
                await ctx.send('<@{}> suggests: '.format(ctx.message.author.id) + query)
                postSuggest(query, usrId)
            else:
                await ctx.send("Invalid use. Use !suggest \"<message>\"")
        else:
            await ctx.send("This command can only be used in a server.")

def setup(bot):
    bot.add_cog(Suggest(bot))