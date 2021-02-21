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
    async def viewSuggest(self, ctx, *args):
        if len(args) == 1:
            try:
                user = ctx.message.mentions[0]
                if ctx.message.author.guild_permissions.administrator or user == ctx.message.author:
                    viewId = str(user.id)
                    usrList = getSuggest(viewId)
                    if len(usrList) != 0:
                        message = "```\n" + str(user) + "'s Suggestion List:\n"
                        for i in range(len(usrList)):
                            msgLen = len(message)
                            if msgLen + len(usrList[i]) <= 1900:
                                message += str(i + 1) + ". " + usrList[i] + "\n"
                            else:
                                message += "```"
                                await ctx.message.author.send(message)
                                message = "```"
                                message += str(i + 1) + ". " + usrList[i] + "\n"
                        message += "```"
                        await ctx.message.author.send(message)
                        await ctx.send("List sent to DMs.")
                    else:
                        await ctx.send("List is empty.")
                else:
                    await ctx.send("You do not have permissions to access this list.")
            except:
                await ctx.send("User not found.")
        else:
            await ctx.send("Invalid arguments. Use /viewSuggest <user>")

    @commands.command()
    async def viewAsk(self, ctx, *args):
        if len(args) == 1:
            try:
                user = ctx.message.mentions[0]
                if ctx.message.author.guild_permissions.administrator or user == ctx.message.author:
                    viewId = str(user.id)
                    usrList = getAsk(viewId)
                    if len(usrList) != 0:
                        message = "```\n" + str(user) + "'s Ask List:\n"
                        for i in range(len(usrList)):
                            msgLen = len(message)
                            if msgLen + len(usrList[i]) <= 1900:
                                message += str(i + 1) + ". " + usrList[i] + "\n"
                            else:
                                message += "```"
                                await ctx.message.author.send(message)
                                message = "```"
                                message += str(i + 1) + ". " + usrList[i] + "\n"
                        message += "```"
                        await ctx.message.author.send(message)
                        await ctx.send("List sent to DMs.")
                    else:
                        await ctx.send("List is empty.")
                else:
                    await ctx.send("You do not have permissions to access this list.")
            except:
                await ctx.send("User not found.")
        else:
            await ctx.send("Invalid arguments. Use /viewAsk <user>")

    #async def viewAskAll(self, ctx):


        
def setup(bot):
    bot.add_cog(View(bot))