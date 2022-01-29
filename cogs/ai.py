import requests
import discord
from discord.ext import commands
import os

class AI(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    pgamerxapi = os.getenv("RandomStuffAPIKEY")
    rapidapi = os.getenv("RapidAPIKey")

    url = "https://random-stuff-api.p.rapidapi.com/ai"
    headers = { 
        'authorization': pgamerxapi,
        'x-rapidapi-host': "random-stuff-api.p.rapidapi.com",
        'x-rapidapi-key': rapidapi
    }

    @commands.command()
    async def ai(self, ctx, *, msg):
        querystring = {"msg":f"{msg}","bot_name":"Shinero Bot","bot_gender":"Male","bot_master":"Shinero","bot_age":"18","bot_company":"PGamerX Development","bot_location":"India","bot_email":"team@pgamerx.com","bot_build":"Public","bot_birth_year":"2003","bot_birth_date":"1st January, 2002","bot_birth_place":"India","bot_favorite_color":"Blue","bot_favorite_book":"Harry Potter","bot_favorite_band":"Imagine Doggos","bot_favorite_artist":"Dua Lipa","bot_favorite_actress":"Emma Watson","bot_favorite_actor":"Jim Carrey","id":"For customised response for each user"}
        request = requests.get(url=self.url, params=querystring, headers=self.headers)
        res = request.json()
        stuff = res['AIResponse']
        await ctx.send(res['AIResponse'])

def setup(bot):
    bot.add_cog(AI(bot))