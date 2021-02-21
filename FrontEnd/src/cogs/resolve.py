import discord
import json
import os
import sys
import requests

from components.post import *
from discord.ext import commands
from discord.ext.commands import MemberConverter

directory = os.path.dirname(os.path.abspath(__file__))
listPath = os.path.join(directory, '../assets/list.json')

class Resolve(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    def is_integer(self, value):
        try:
            int(value)
            return True
        except:
            return False

    @commands.command()
    async def resolveSuggest(self, ctx, *args):
        try:
            if ctx.message.author.guild_permissions.administrator:
                if len(args) != 0:
                    converter = MemberConverter()
                    usrName = await converter.convert(ctx, args[0])
                    usrId = usrName.id
                    channel = await usrName.create_dm()
                    if len(args) == 1:
                        await ctx.send("Resolved " + str(usrName) + "'s suggestions")
                        await channel.send("All suggestions were resolved!")
                        postResolveSuggestAll(usrId)
                    elif len(args) == 2:
                        if self.is_integer(args[1]) is True:
                            await ctx.send("Resolved " + str(usrName) + "'s suggestion index: " + str(args[1]))
                            await channel.send("Suggestion " + str(args[1]) + " was resolved!")
                            postResolveSuggest(args[1], usrId)
                        else:
                            await ctx.send("Invalid resolve command!")
                    else:
                        await ctx.send("Invalid resolve command!")
                else:
                    await ctx.send("Invalid resolve command!")
            else:
                await ctx.send("You do not have permissions to do this.")
        except:
            await ctx.send("Invalid user!")

    @commands.command()
    async def resolveAsk(self, ctx, *args):
        try:
            if ctx.message.author.guild_permissions.administrator:
                if len(args) != 0:
                    converter = MemberConverter()
                    usrName = await converter.convert(ctx, args[0])
                    usrId = usrName.id
                    channel = await usrName.create_dm()
                    if len(args) == 1:
                        await ctx.send("Resolved " + str(usrName) + "'s question")
                        await channel.send("All questions were resolved!")
                        postResolveAskAll(usrId)
                    elif len(args) == 2:
                        if self.is_integer(args[1]) is True:
                            await ctx.send("Resolved " + str(usrName) + "'s question index: " + str(args[1]))
                            await channel.send("Question " + str(args[1]) + " was resolved!")
                            postResolveAsk(args[1], usrId)
                        else:
                            await ctx.send("Invalid resolve command!")
                    else:
                        await ctx.send("Invalid resolve command!")
                else:
                    await ctx.send("Invalid resolve command!")
            else:
                await ctx.send("You do not have permissions to do this.")
        except:
                await ctx.send("Invalid user!")

def setup(bot):
    bot.add_cog(Resolve(bot))