import discord
import json
import os
import sys
import requests

from components.get import getSuggest
from components.get import getAsk
from discord.ext import commands

class View(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def view(self, ctx, *args):
        if len(args) == 2:
            if args[0] == "suggest":
                try:
                    user = ctx.message.mentions[0]
                    viewId = str(user.id)
                    usrList = getSuggest(viewId)
                    message = "```\n" + str(user) + "'s Suggestion List:\n"
                    for i in range(len(usrList)):
                        message += str(i + 1) + ". " + usrList[i] + "\n"
                    message += "```"
                    await ctx.message.author.send(message)
                except:
                    await ctx.send("User not found or list was empty.")
            elif args[0] == "ask":
                try:
                    user = ctx.message.mentions[0]
                    viewId = str(user.id)
                    usrList = getAsk(viewId)
                    message = "```\n" + str(user) + "'s Ask List:\n"
                    for i in range(len(usrList)):
                        message += str(i + 1) + ". " + usrList[i] + "\n"
                    message += "```"
                    await ctx.message.author.send(message)
                except:
                    await ctx.send("User not found or list was empty.")
            else:
                await ctx.send("Invalid argument. Use /view <type> <user>")
        else:
            await ctx.send("Invalid use. Use /view <type> <user>")

        

def setup(bot):
    bot.add_cog(View(bot))