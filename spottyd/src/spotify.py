import discord
from discord.ext import commands

class SpotifyMiddleware(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener('on_ready')
    async def on_ready(self):
        """ Initializes the Database and the Spotify API"""

        print(f'{self.bot.user.name} has connected to Discord with SpotifyMiddleware!')
        for guild in self.bot.guilds:
            print("Guild: "+ guild.name)
            for member in guild.members:
                print("\t - " +member.name);
        #TODO

    @commands.Cog.listener('on_message')
    async def on_message(self, message):
        """ This is an on_message listener which listens for music recommendations"""
        # TODO
        # if(is_spotify_rec(message)):
        #    add_to_database_and_playlist(message)

    @commands.command()
    async def set_channel(self, ctx, *, member):
        """Sets as the music recommendation channel"""
        # TODO
        await ctx.send(f"{ctx.channel} set as music recs channel!")

    @commands.command()
    async def set_api(self, ctx, *, member):
        await ctx.send(f"API key set")
