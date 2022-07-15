import discord 
from discord.ext import commands
import os
import random

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
    
@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        
        whole_message = str(message.content).split(" ")
        user = whole_message[0]
        tag = whole_message[1]
        message_its_self = whole_message[2]

        print(message_its_self)
        await message.channel.send('yep')

        if tag == "t":
            pass
        elif tag == "p":
            pass
        elif tag == "pa":
            pass
        else:
            pass
        
bot.run(TOKEN)