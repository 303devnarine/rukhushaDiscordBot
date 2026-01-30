import discord
# import messageProcessor as msgPro
from discord.ext import commands
# from discord import app_commands
import logging
from dotenv import load_dotenv
import os
from time import sleep
import random
from inspirational_quotes import quote
from threading import Thread
from flask import Flask

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()

intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="r.", owner_id=916816688186527844, intents=intents)

# Flask app for health checks
app = Flask(__name__)

@app.route('/')
def home():
    return "Discord bot is running!", 200

@app.route('/health')
def health():
    return "OK", 200

def run_flask():
    port = int(os.getenv("PORT", 15500))
    app.run(host='0.0.0.0', port=port)

@bot.event
async def on_ready():
    print(f"{bot.user} is online")
    await bot.tree.sync()

@bot.event
async def on_message(message):
    if message.author != bot.user:
        # await msgPro.process(message)
        return

    await bot.process_commands(message)

@bot.tree.command(name="hug", description="Send Rukhusha a virtual hug!")
async def hug(interaction: discord.Interaction):
    username = interaction.user.mention
    await interaction.response.send_message(f"*{username} sent a virtual hug to Rukhusha!*")
    sleep(1)
    await interaction.user.send(f"Thank you, {interaction.user.global_name}!")

@bot.tree.command(name="coinflip", description="Flips a coin.")
async def coinflip(interaction: discord.Interaction):
    username = interaction.user.mention
    await interaction.response.send_message(f"{username}, the coin landed on {"Heads" if random.randint(0,1) == 0 else "Tails" }.")

@bot.tree.command(name="inspirational_quote", description="Sends you an inspiration quote!")
async def inspirational_quote(interaction: discord.Interaction):
    q = quote()
    print(q)
    await interaction.response.send_message(f"*{q['quote']}*\n{q['author']}")

if __name__ == "__main__":
    # Start Flask server in a separate thread
    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    # Start Discord bot
    bot.run(token, log_handler=handler, log_level=logging.DEBUG)


