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
        usrId = ctx.message.author.id
        if len(args) == 1:
            if self.is_integer(args[0]) is True:
                await cwt.send("Suggestion removed")
                postResolveSuggest(args[0], usrId)
            else:
                await cwt.send("Invalid arguments sent: !removeSuggest <index>")
        else:
            await cwt.send("Invalid arguments sent: !removeSuggest <index>")

    @commands.command()
    async def removeAsk(self, ctx, *args):
        usrId = ctx.message.author.id
        if len(args) == 1:
            if self.is_integer(args[0]) is True:
                await cwt.send("Ask removed")
                postResolveAsk(args[0], usrId)                
            else:
                await cwt.send("Invalid arguments sent: !removeSuggest <index>")
        else:
            await cwt.send("Invalid arguments sent: !removeSuggest <index>")

    

def setup(bot):
    bot.add_cog(RemoveQuery(bot))