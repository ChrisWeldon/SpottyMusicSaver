#!/usr/bin/env python
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

from src.spotify import SpotifyMiddleware
from src.database import DatabaseMiddleware

if __name__=="__main__":
    print("\n=========== STARTING BOT ============\n")
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix='!', intents = intents)
    bot.add_cog(DatabaseMiddleware(bot)) # Maybe we should toss this in the Spotify module
    bot.add_cog(SpotifyMiddleware(bot))
    bot.run(TOKEN)
    print("Bot Started")
