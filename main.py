import discord
import time
import random
from discord.ext import commands
from discord import app_commands

currentbal : int
Moneybet : int
gif_link = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbTAwd25zaWNvY2JjN2FianhneGQ0emU0NDU1MzlnMmNvaGZpdGJsMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SABvdsgeZrcu4SbdA6/giphy.gif"

BOT_TOKEN = 'TOKEN WENT THAT WAY ->'

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
bot = commands.Bot(command_prefix='/', intents=intents)


embed1 = discord.Embed(title="Side Selection", description = "Which side would you like to chose?", color=discord.Color.blurple())
embed2 = discord.Embed(title="Flipping the Coin..",description = "Are you lucky enough?", color=discord.Color.blurple()) 
embed2.set_image(url=gif_link)

@bot.event
async def on_guild_join(guild):
    print(f"Joined server named: {guild.name}")

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}')
    await bot.tree.sync()
    print("Commands ready")
    currentbal = 100

@bot.tree.command(name="bet", description="Bet on your next coin flip.")
@app_commands.describe(amount_to_bet = "how much would you like to bet?")
async def say(interaction: discord.Integration, amount_to_bet: int):
    Moneybet = amount_to_bet
    await interaction.response.send_message("GO AWAY")




@bot.tree.command(name="flip", description="Flips the coin.")
async def choseside(ctx):
    chosen : int
    print(ctx.user)
    Heads: bool
    Tails: bool
    rando = random.randint(0,1)
    await ctx.response.send_message(embed=embed1)
    if embed1.author == bot.user:
        return
    msg = await ctx.original_response()
    time.sleep(1)
    await msg.add_reaction("🗣️")
    time.sleep(1)
    await msg.add_reaction("🐱")
    await bot.wait_for('reaction_add')
    await msg.edit(embed=embed2)

    print(Heads)
    print(Tails)





bot.run(BOT_TOKEN)

