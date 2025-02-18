import discord
from discord.ext import commands
import os

TOKEN = "MTM0MTM1NTk0NjIwNjY5MTM0OA.GVyFvk.0uvebvjmEmQo3iLsVgJUIfpAKvQY3jX73DpwCE"
FILE_PATH = "microsoft_hits.txt"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def sendfile(ctx):
    if os.path.exists(FILE_PATH):
        await ctx.author.send(file=discord.File(FILE_PATH))
        await ctx.send("📂 File sent to your DMs!")
    else:
        await ctx.send("❌ File not found.")

bot.run(TOKEN)
