import discord
import json
import os
import sys
import requests

from components.get import *
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
        if ctx.message.guild:
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
                                query = getSuggest(usrId)[int(args[1]) - 1]
                                await ctx.send("Resolved " + str(usrName) + "'s suggestion index: " + str(args[1]))
                                await channel.send("Suggestion " + str(args[1]) + ": \"" + query + " was resolved!")
                                postResolveSuggest(args[1], usrId)
                            else:
                                await ctx.send("Invalid resolve command! Use !resolveSuggest <user> <index> \"<message>\"")
                        elif len(args) == 3:
                            query = getSuggest(usrId)[int(args[1]) - 1]
                            resolveMsg = str(args[2])
                            await ctx.send("Resolved " + str(usrName) + "'s suggestion index: " + str(args[1]) + " with message: " + resolveMsg)
                            await channel.send("```\nSuggestion " + str(args[1]) + ": \"" + query + "\" was resolved with message:\n" + resolveMsg + "\n```")
                            postResolveSuggest(str(int(args[1]) - 1), usrId)
                        else:
                            await ctx.send("Invalid resolve command! Use !resolveSuggest <user> <index> \"<message>\"")
                    else:
                        await ctx.send("Invalid resolve command! Use !resolveSuggest <user> <index> \"<message>\"")
                else:
                    await ctx.send("You do not have permissions to do this.")
            except:
                await ctx.send("Invalid user!")
        else:
            await ctx.send("This command can only be used in a server.")

    @commands.command()
    async def resolveAsk(self, ctx, *args):
        if ctx.message.guild:
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
                                query = getAsk(usrId)[int(args[1]) - 1]
                                await ctx.send("Resolved " + str(usrName) + "'s question index: " + str(args[1]))
                                await channel.send("```\nQuestion " + str(args[1]) + ": \"" + query + "\" was resolved!\n```")
                                postResolveAsk(str(int(args[1]) - 1), usrId)
                            else:
                                await ctx.send("Invalid resolve command! Use !resolveAsk <user> <index> \"<message>\"")
                        elif len(args) == 3:
                            query = getAsk(usrId)[int(args[1]) - 1]
                            resolveMsg = str(args[2])
                            await ctx.send("Resolved " + str(usrName) + "'s question index: " + str(args[1]) + " with message: " + resolveMsg)
                            await channel.send("```\nQuestion " + str(args[1]) + ": \"" + query + "\" was resolved with message:\n" + resolveMsg + "\n```")
                            postResolveAsk(str(int(args[1]) - 1), usrId)
                        else:
                            await ctx.send("Invalid resolve command! Use !resolveAsk <user> <index> \"<message>\"")
                    else:
                        await ctx.send("Invalid resolve command! Use !resolveAsk <user> <index> \"<message>\"")
                else:
                    await ctx.send("You do not have permissions to do this.")
            except:
                    await ctx.send("Invalid user!")
        else:
            await ctx.send("This command can only be used in a server.")

def setup(bot):
    bot.add_cog(Resolve(bot))