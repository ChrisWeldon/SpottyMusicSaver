#!/usr/bin/env python
import os
import random
import re

from discord.ext import commands
from dotenv import load_dotenv
import discord


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents = intents)

def getSession(ctx):
    return bot.SESSIONS[ctx.guild.name]

# FIXME : not threadsafe
def setSession(ctx, session):
    bot.SESSIONS[ctx.guild.name] = session

async def tard_bin(user):
    # Kicks for now
    session = getSession(user)
    session["TARDS"][user.discriminator]["count"] = 0
    await user.kick(reason="TARD BINNN")


@bot.event
async def on_ready():
    # TODO add tard
    print(f'{bot.user.name} has connected to Discord!')

    # TODO classify this
    bot.SESSIONS = {
        "FMTG" : {
            "TARDS": {
                "8545":{
                    'max_warn': 3,
                    'count_warn':0,
                }
            },
            "PHOTO_CHANNEL_ID": 785322697633693696
        },
        "Cumdog Millionaires":{
            "TARDS": {
                "5037":{
                    'max_warn': 3,
                    'count_warn':0,
                }
            },
            "PHOTO_CHANNEL_ID": 605860350629380190
        }
    }

    for guild in bot.guilds:
        print("Guild: "+ guild.name)
        for member in guild.members:
            print("\t - " +member.name);

@bot.event
async def on_message(msg):
    session = getSession(msg)
    print(msg)


@bot.command(name='command', help="Use this command to set the photo")
async def setPhotoChannel(ctx):
    session = getSession(ctx)
    session["PHOTO_CHANNEL_ID"] = ctx.channel.id
    setSession(ctx, session)
    await ctx.channel.send("*Photo Channel Set*")


if __name__=="__main__":
    print("Bot Started")
    
    bot.run(TOKEN)
