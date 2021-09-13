import discord
from discord.ext import commands
import json
import random
with open('setting.json',mode='r',encoding='UTF-8') as jfile:
    jdata=json.load(jfile)

bot=commands.Bot(command_prefix='[')
print("bottest")
@bot.event
async def on_ready():
    print(">>BOT is Online")

@bot.command()
async def ping(ctx):
    await ctx.send(bot.latency)

@bot.command()
async def Imageshow(ctx):
    pic =discord.File('D:\\實況\\FB文.PNG')
    
    await ctx.send(file=pic)

bot.run(jdata['TOKEN'])
