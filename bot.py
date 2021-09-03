import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import commands_cog

load_dotenv("key.env")
discord_token = os.getenv("DISCORD_TOKEN")

bot = commands.Bot("?def ", description="Theological Dictionary Bot", case_insensitive=True)
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Ready")
    activity = discord.Game("def? | Tyndale | Theological Dictionary Bot")
    await bot.change_presence(activity=activity)

commands_cog.setup(bot)

bot.run(discord_token)