import discord
import requests
import os
import json
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from dotenv import load_dotenv

load_dotenv()
client = commands.Bot(command_prefix = '!')
client.remove_command("help")

token = os.getenv('DISCORD_TOKEN')

extensionList = ['cogs.ask', 'cogs.poll', 'cogs.suggest', 'cogs.resolve']

if __name__ == '__main__':
    for extension in extensionList:
        client.load_extension(extension)

@client.event
async def on_ready():
    print("Bot is ready.")

client.run(token)