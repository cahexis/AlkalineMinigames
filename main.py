import discord
from discord.ext import commands
from discord import app_commands

BOT_TOKEN = 'BOT TOKEN HERE'

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')


intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(BOT_TOKEN)

