import discord
BOT_TOKEN = "MTQ2MTQ0MDgxMjA4NzkwNjM1Nw.GLcykS.6ob0pk_H3hjQg46ZnqvVM5PV5LgJyQyKuRPgkg"

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')


intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(BOT_TOKEN)