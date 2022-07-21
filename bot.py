import discord 
from discord.ext import commands
import os
import random
import requests
import shutil
import uuid


with open("token.txt") as f:
    file = f.readlines()
    the_line = file[0]


TOKEN = the_line


client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Test"))
    print("Bot is ready!")



@client.command()
async def love(ctx):
    await ctx.send(f"❤️ <@{ctx.author.id}>")

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


@client.command()
async def download_all(ctx):
    messages = await ctx.channel.history(limit=200).flatten()

    counter = 0
    for msg in messages:
        #print(msg.content) #.jump_url
        counter += 1 
        if msg.attachments:
            url = msg.attachments[0]
            r = requests.get(url, stream=True)
            imageName = str(uuid.uuid4()) + '.jpg'      # uuid creates random unique id to use for image names

            with open(imageName, 'wb') as out_file:
                print('Saving image: ' + imageName)
                shutil.copyfileobj(r.raw, out_file)
        
        elif msg.content[0:26] == "https://cdn.discordapp.com":
            the_url = msg.content
            req = requests.get(the_url)

            bytes = int(req.headers['Content-Length'])
            megabyte = float(bytes/1000000)

            
            filename = req.url[the_url.rfind('/')+1:]
            if megabyte > 10:
                pass
            else:
                with requests.get(the_url) as reqq:
                    with open(filename, 'wb') as f:
                        for chunk in reqq.iter_content(chunk_size=8192):
                            if chunk:
                                f.write(chunk)
                    print('Saving vid: ' + filename)
                    
        else:
            pass

    print(counter)

client.run(TOKEN)