import discord
import json
import os
import sys
import requests

from components.post import *
from discord.ext import commands

directory = os.path.dirname(os.path.abspath(__file__))
listPath = os.path.join(directory, '../assets/list.json')

class RemoveQuery(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    def is_integer(self, value):
        try:
            int(value)
            return True
        except:
            return False

    @commands.command()
    async def removeSuggest(self, ctx, *args):
        if ctx.message.guild:
            usrId = ctx.message.author.id
            if len(args) == 1:
                if self.is_integer(args[0]) is True:
                    await ctx.send("Suggestion removed")
                    postResolveSuggest(str(int(args[0]) - 1), usrId)
                else:
                    await ctx.send("Invalid arguments sent: !removeSuggest <index>")
            else:
                await ctx.send("Invalid arguments sent: !removeSuggest <index>")
        else:
            await ctx.send("This command can only be used in a server.")

    @commands.command()
    async def removeAsk(self, ctx, *args):
        if ctx.message.guild:
            usrId = ctx.message.author.id
            if len(args) == 1:
                if self.is_integer(args[0]) is True:
                    await ctx.send("Ask removed")
                    postResolveAsk(str(int(args[0]) - 1), usrId)                
                else:
                    await ctx.send("Invalid arguments sent: !removeSuggest <index>")
            else:
                await ctx.send("Invalid arguments sent: !removeSuggest <index>")
        else:
            await ctx.send("This command can only be used in a server.")

def setup(bot):
    bot.add_cog(RemoveQuery(bot))