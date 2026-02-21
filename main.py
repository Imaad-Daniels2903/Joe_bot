import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

joe = commands.Bot(command_prefix='!', intents=intents)

@joe.event
async def on_ready():
    print("Hey there... YOU")

@joe.command()
async def hello(ctx):
    await ctx.send(f"Hello ...{ctx.author}, right?")
    await ctx.send(f"Nice to see YOU again {ctx.author}...")

joe.run(token, log_handler=handler, log_level=logging.DEBUG)