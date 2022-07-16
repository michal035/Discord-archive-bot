import discord 
from discord.ext import commands
import os
import random
import requests

with open("token.txt") as f:
    file = f.readlines()
    the_line = file[0]


TOKEN = the_line

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Sigma grindset"))
    print("Bot is ready!")

@bot.command()
async def c(ctx, *, message: str):
    channel=bot.get_channel(887034916821430303)
    await ctx.send(message)


def download_file(url, downloadUrl, filename=''):
    
    req = requests.get(downloadUrl)

    bytes = int(req.headers['Content-Length'])
    megabyte = float(bytes/1000000)
    

    try:
        if filename:
            pass            
        else:
            filename = req.url[downloadUrl.rfind('/')+1:]
        if megabyte > 10:
            pass
        else:
            with requests.get(url) as req:
                with open(filename, 'wb') as f:
                    for chunk in req.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                return filename

    except Exception as e:
        print(e)
        return None


@bot.command()
async def keyword(ctx, *, word: str):
    channel = bot.get_channel(841776407344709666)
    messages = await ctx.channel.history(limit=200).flatten()

    for msg in messages:
        if word in msg.content:
            print(msg.jump_url)
            ctx.send(msg)

"""
@bot.command()
async def cc(ctx):
    messages = ctx.history(limit=10).flatten()
    contents = []

    for message in messages:
        contents.append(message.content)

    print(contents)



@bot.command()
async def find(ctx, *, phrase:str):
    print("e")
    if not (phrase):
        return await bot.send("Please enter a phrase and days")
        
    if  phrase:
        messages = await bot.channel.history(limit=10, oldest_first=True).flatten()
        for message in messages:
            if phrase in message.content:
                print(message)
    else:
        await ctx.send("please enter the number of days wanted")
"""

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        
        whole_message = str(message.content).split(" ")
        user = whole_message[0]
        tag = whole_message[1]
        
        try:
            message_its_self = whole_message[2]
        except:
            tag = "None"
            message_its_self = whole_message[1]


        print(message_its_self)
        await message.channel.send('yep')

        if tag == "t":
            pass
        elif tag == "p":
            pass
        elif tag == "pa":
            pass
        else:
            download_file(message_its_self,message_its_self, '')


bot.run(TOKEN)