import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import cogs

# Tyndale Bot made by DeeDeeAich in September 2021
# This is simply a theological dictionary bot for looking up definitions of theological terms.

load_dotenv("key.env")
discord_token = os.getenv("DISCORD_TOKEN")

bot = commands.Bot("?", description="Theological Dictionary Bot", case_insensitive=True)
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Ready")
    activity = discord.Game("? | Tyndale")
    await bot.change_presence(activity=activity)

cogs.setup(bot)

bot.run(discord_token)