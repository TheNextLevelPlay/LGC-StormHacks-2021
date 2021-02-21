import discord
import json
import os
import sys
import requests

from components.get import getUsers
from discord.ext import commands

class Mail(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mail(self, ctx, *args):
        nmbOfSuggests = 0
        nmbOfAsks = 0
        if len(args) == 0:
            jsonData = getUsers()
            for i in jsonData:
                nmbOfSuggests += int(i['suggestSize'])
                nmbOfAsks += int(i['askSize'])
            message = "```"
            message += "Number of questions: " + str(nmbOfAsks) + "\n"
            message += "Number of suggestions: " + str(nmbOfSuggests) + "\n"
            message += "```"
            await ctx.message.author.send(message)
        else:
            await ctx.send("Invalid number of arguments sent. Use: !mail")


def setup(bot):
    bot.add_cog(Mail(bot))