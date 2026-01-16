import discord
from discord.ext import commands
from discord import app_commands

BOT_TOKEN = 'HIDDEN TOKEN LOL!!!'

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)



@bot.event
async def on_guild_join(guild):
    print(f"Joined server named: {guild.name}")

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}')
    await bot.tree.sync()
    print("Commands ready")

@bot.tree.command(name="bet", description="Bet on your next coin flip.")
@app_commands.describe(amount_to_bet = "how much would you like to bet?")
async def say(interaction: discord.Integration, amount_to_bet: int):
    await interaction.response.send_message("GO AWAY")

@bot.tree.command(name="flip", description="Flips the coin.")
@app_commands.describe(choose_side = "Type in the side you would like to bet on")
async def say(interaction: discord.Integration, choose_side: str):
    await interaction.response.send_message(f"you bet on {choose_side}")

bot.run(BOT_TOKEN)

