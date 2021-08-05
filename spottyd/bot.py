#!/usr/bin/env python
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

from src.spotify import SpotifyMiddleware

if __name__=="__main__":
    print("\n=========== RESTART ============\n")
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix='!', intents = intents)
    bot.add_cog(SpotifyMiddleware(bot))
    bot.run(TOKEN)
    print("Bot Started")
