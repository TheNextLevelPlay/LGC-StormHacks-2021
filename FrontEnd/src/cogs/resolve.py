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
            if len(args) != 0:
                converter = MemberConverter()
                usrName = await converter.convert(ctx, args[0])
                usrId = usrName.id
                if len(args) == 1:
                    await ctx.send("Resolved " + str(usrName) + "'s suggestions")
                    postResolveSuggestAll(usrId)
                elif len(args) == 2:
                    if self.is_integer(args[1]) is True:
                        await ctx.send("Resolved " + str(usrName) + "'s suggestion index: " + str(args[1]))
                        postResolveSuggest(args[1], usrId)
                    else:
                        await ctx.send("Invalid resolve command!")
                else:
                    await ctx.send("Invalid resolve command!")
            else:
                await ctx.send("Invalid resolve command!")
        except:
            await ctx.send("Invalid user!")

    @commands.command()
    async def resolveAsk(self, ctx, *args):
        try:
            if len(args) != 0:
                converter = MemberConverter()
                usrName = await converter.convert(ctx, args[0])
                usrId = usrName.id
                if len(args) == 1:
                    await ctx.send("Resolved " + str(usrName) + "'s question")
                    postResolveAskAll(usrId)
                elif len(args) == 2:
                    if self.is_integer(args[1]) is True:
                        await ctx.send("Resolved " + str(usrName) + "'s question index: " + str(args[1]))
                        postResolveAsk(args[1], usrId)
                    else:
                        await ctx.send("Invalid resolve command!")
                else:
                    await ctx.send("Invalid resolve command!")
            else:
                await ctx.send("Invalid resolve command!")
        except:
                await ctx.send("Invalid user!")

def setup(bot):
    bot.add_cog(Resolve(bot))