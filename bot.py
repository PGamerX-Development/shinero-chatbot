import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix="s+")

token = os.getenv("TOKEN")

bot.load_extension("cogs.ai")

bot.run(token)