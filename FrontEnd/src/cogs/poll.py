import discord
import json
import os
import sys

from discord.ext import commands

class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def poll(self, ctx, *args):
        reactList = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']
        if ctx.message.guild:
            if len(args) <= 10:
                botMsg = "```\n"
                for i in range(len(args)):
                    botMsg += reactList[i] + ": " + args[i] + "\n"
                botMsg += "```"
                if len(botMsg) <= 1900:
                    sentMsg = await ctx.send(botMsg)
                    for i in range(len(args)):
                        await sentMsg.add_reaction(reactList[i])
                else:
                    await ctx.send("Too many characters. Try shortening the option length.")
            else:
                await ctx.send("Too many poll options. Send up to 9.")
        else:
            await ctx.send("This command can only be used in a server.")
        
def setup(bot):
    bot.add_cog(Poll(bot))