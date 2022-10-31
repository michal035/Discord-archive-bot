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
    await client.change_presence(activity=discord.Game(name="Memes go brrrr"))
    print("Bot is ready!")




def download_file(url, downloadUrl, filename=''):
    
    try:
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
                    with open(f"memes/{filename}", 'wb') as f:
                        for chunk in req.iter_content(chunk_size=8192):
                            if chunk:
                                f.write(chunk)
                    return filename

        except Exception as e:
            print(e)
            return None

    except:
        print("file error")


@client.command()
async def download_all(ctx):
    messages = await ctx.channel.history(limit=1000).flatten()

    counter = 0
    for msg in messages:
        #print(msg.content) #.jump_url
        counter += 1 
        if msg.attachments:
            url = msg.attachments[0]
            
            try:
                r = requests.get(url, stream=True)
                imageName = str(uuid.uuid4()) + '.jpg'      # uuid creates random unique id to use for image names

                with open(f"memes/{imageName}", 'wb') as out_file:
                    print('Saving image: ' + imageName)
                    shutil.copyfileobj(r.raw, out_file)
            
            except:
                print("file error")
        
        elif msg.content[0:26] == "https://cdn.discordapp.com":
            the_url = msg.content
            
            try:
                req = requests.get(the_url)

                bytes = int(req.headers['Content-Length'])
                megabyte = float(bytes/1000000)

            
                filename = req.url[the_url.rfind('/')+1:]
                if megabyte > 20:
                    pass
                else:
                    with requests.get(the_url) as reqq:
                        with open(f"memes/{filename}", 'wb') as f:
                            for chunk in reqq.iter_content(chunk_size=8192):
                                if chunk:
                                    f.write(chunk)
                        print('Saving vid: ' + filename)
            
            except:
                print("file error")

                    
        else:
            pass

    print(counter)

@client.command()
async def d(ctx, *, message: str):
    #await ctx.send(message)
    if True:
        whole_message = message.split(" ")
        #print(whole_message)
        
        try:
            whole_message.remove('')
        except:
            pass
        

        tag = whole_message[0]
        
        try:
            message_its_self = whole_message[1]
        except:
            tag = "None"
            message_its_self = whole_message[0]


        print(message_its_self)
        await ctx.channel.send('yep')

        if tag == "t":
            pass
        elif tag == "p":
            pass
        elif tag == "pa":
            pass
        else:
            download_file(message_its_self,message_its_self, '')


@client.command()
async def download_all_new(ctx):
    messages = await ctx.channel.history(limit=300).flatten()

    counter = 0
    for msg in messages:
        #print(msg.content) #.jump_url
        counter += 1 
        
        try:
            text = msg.content
        except:
            pass
        
        if text[0:1] == "!d":
            pass
        elif text == "!download_all" or text == "!download_all_new":
            break
        else:

            if msg.attachments:
                url = msg.attachments[0]
            
                try:
                    r = requests.get(url, stream=True)
                    imageName = str(uuid.uuid4()) + '.jpg'      # uuid creates random unique id to use for image names

                    with open(f"memes/{imageName}", 'wb') as out_file:
                        print('Saving image: ' + imageName)
                        shutil.copyfileobj(r.raw, out_file)
            
                except:
                    print("file error")
        
            elif msg.content[0:26] == "https://cdn.discordapp.com":
                the_url = msg.content
            
                try:
                    req = requests.get(the_url)

                    bytes = int(req.headers['Content-Length'])
                    megabyte = float(bytes/1000000)

            
                    filename = req.url[the_url.rfind('/')+1:]
                    if megabyte > 20:
                        pass
                    else:
                        with requests.get(the_url) as reqq:
                            with open(f"memes/{filename}", 'wb') as f:
                                for chunk in reqq.iter_content(chunk_size=8192):
                                    if chunk:
                                        f.write(chunk)
                            print('Saving vid: ' + filename)
            
                except:
                    print("file error")

                    
            else:
                pass

    print(counter)

    
@client.command()
async def get_random_meme(ctx):
    path = os.path.abspath(os.getcwd())
    new_path = f"{path}/memes"
    
    array = os.listdir(new_path)
    random_file = array[random.randint(0,len(array))]
    final_path = f"{new_path}/{random_file}"
    #await ctx.send(final_path)
    await ctx.send('Here you go', file=discord.File(final_path))
  

@client.command()
async def love(ctx):
    await ctx.send(f"❤️ <@{ctx.author.id}>")

client.run(TOKEN)
