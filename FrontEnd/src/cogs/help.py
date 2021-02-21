import discord
import json
import os
import sys

from discord.ext import commands

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, *args):
        helpMsg = "```"
        if len(args) == 1:
            if args[0] == "add":
                helpMsg += "\nAdd Commands:"
                helpMsg += "\nAsk - !ask \"<message>\"\n - \"<message>\" - The question you want to ask in quotations\n"
                helpMsg += "\nSuggest - !suggest \"<message>\"\n - \"<message>\" - The suggestion you want to send in quotations\n"
            elif args[0] == "view":
                helpMsg += "\nView Commands:"
                helpMsg += "\nView Questions - !viewAsk <user>\n - <user> - The user's question list you want to look up (Optional)\n"
                helpMsg += "\nView Suggestions - !viewSuggest <user>\n - <user> -  The user's question list you want to look up (Optional)\n"
                helpMsg += "\nView All User Questions - !viewSuggestAll\n"
                helpMsg += "\nView All User Suggestions - !viewSuggestAll\n"
            elif args[0] == "remove":
                helpMsg += "\nRemove Commands:"
                helpMsg += "\nRemove Question - !removeAsk <index>\n - <index> - The number of the question you want to remove\n"
                helpMsg += "\nRemove Suggestion - !removeSuggest <index>\n - <index> - The number of the suggestion you want to remove\n"
            elif args[0] == "resolve":
                helpMsg += "\nResolve Commands:"
                helpMsg += "\nAnswer Question - !resolveAsk <user> <index> \"<message>\"\n - <user> - The user's list you want to answer from\n - <index> - The number of the question you want to answer (Optional) (Resolves all without argument)\n - \"<message>\" - Your answer to the question in quotations (Optional)\n"
                helpMsg += "\nAnswer Suggestion - !resolveSuggest <user> <index> \"<message>\"\n - <user> - The user's list you want to answer from\n - <index> - The number of the suggestion you want to answer (Optional) (Resolves all without argument)\n - \"<message>\" - Your answer to the suggestion in quotations (Optional)\n"
            elif args[0] == "poll":
                helpMsg += "\nPoll Commands:"
                helpMsg += "\nStart Poll - !poll \"<options>\"\n - \"<options>\" - The poll options you want in quotations. Can have up to 10 options\n"
        else:
            helpMsg += "\nHelp Categories (Use /help <category>):"
            helpMsg += "\n - add - Commands that add to query lists"
            helpMsg += "\n - view - Commands that can view query lists"
            helpMsg += "\n - remove - Commands that can remove from query lists"
            helpMsg += "\n - resolve - Commands that can answer query lists (Admin only)"
            helpMsg += "\n - poll - Commands that can create polls"

        helpMsg += "```"
        await ctx.send(helpMsg)

def setup(bot):
    bot.add_cog(HelpCommand(bot))