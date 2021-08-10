import discord
import asyncio
import aiomysql
from discord.ext import commands

class DatabaseMiddleware(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener('on_ready')
    async def on_ready(self):
        """ Initializes the Database."""

        print(f'{self.bot.user.name} has connected to Database')
        print(await connect())

    @commands.Cog.listener('on_message')
    async def on_message(self, message):
        """ This is an on_message listener which listens for music recommendations"""

    @commands.command()
    async def database(self, ctx, *s):
        # TODO
        conn = await connect()
        async with conn.cursor() as cursor:
            await cursor.execute('SHOW DATABASES;')
            await ctx.send(cursor.fetchall())

async def connect():
    # Network assigns new ip's, mysqldb is the dns of the msql server

    # TODO try setting bind address
    # TODO revert to old password auth


    return await aiomysql.connect(host='mysqldb', port=3306, user='root', password='p@ssw0rd1', db='musicrecs')
