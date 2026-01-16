import discord
import time
import random
import asyncio
from discord.ext import commands
from discord import app_commands


Moneybet : int
gif_link = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbTAwd25zaWNvY2JjN2FianhneGQ0emU0NDU1MzlnMmNvaGZpdGJsMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SABvdsgeZrcu4SbdA6/giphy.gif"

BOT_TOKEN = 'INSERT BOT TOKEN HERE'

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
bot = commands.Bot(command_prefix='/', intents=intents)


embed1 = discord.Embed(title="Side Selection", description = "Which side would you like to chose?", color=discord.Color.blurple())
embed2 = discord.Embed(title="Flipping the Coin..",description = "Are you lucky enough?", color=discord.Color.blurple()) 
embed2.set_image(url=gif_link)
embed3 = discord.Embed(title="YOU WON!", description="You lucky fella.", color=discord.Color.yellow())
embed4 = discord.Embed(title="YOU LOST", description="haha loser", color=discord.Color.red())
@bot.event
async def on_guild_join(guild):
    print(f"Joined server named: {guild.name}")

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}')
    await bot.tree.sync()
    print("Commands ready")



@bot.tree.command(name="flip", description="Flips the coin.")
async def choseside(ctx):
    won : bool
    Heads: bool
    Tails: bool
    rando = random.randint(0,1)
    if rando == 0:
        Heads = True
        Tails = False
    else:
        Heads = False
        Tails = True
    await ctx.response.send_message(embed=embed1)
    if embed1.author == bot.user:
        return
    msg = await ctx.original_response()
    time.sleep(1)
    await msg.add_reaction("🗣️")
    await msg.add_reaction("🐱")

    def check(reaction, user):
        return reaction.message.id == msg.id and user != bot.user
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout = 60, check=check)
    except asyncio.TimeoutError:
        await ctx.send("no one gets to gamble fine then")
    else:
        print("user input taken")
      
    if reaction.emoji == "🗣️" and Heads == True or reaction.emoji == "🐱" and Tails == True:
        won = True
    else:
        won = False
    await msg.edit(embed=embed2)
    time.sleep(3)  
    print(won)
    if won == True:
        await msg.edit(embed=embed3)
    elif won == False:
        await msg.edit(embed=embed4)       

bot.run(BOT_TOKEN)

