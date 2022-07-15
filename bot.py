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