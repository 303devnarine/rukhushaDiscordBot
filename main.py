import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
from time import sleep

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="r.", intents=intents)

@bot.event
async def on_ready():
    print(f"Ready, {bot.user.name}")
    print(bot.users)

@bot.event
async def on_member_join(member):
    await member.send(f"Get the fuck out, {member.name}")

@bot.event
async def on_message(message):
    nameOfUser = message.author.global_name
    sleep(0.1)

    if message.author == bot.user:
        return

    if "hallo" in message.content.lower():
        await message.channel.send(f"hallo {nameOfUser}!")

    if "goedemorgen" in message.content.lower():
        await message.channel.send(f"Good morning to you, {nameOfUser}!")

    if "goede nacht" in message.content.lower():
        await message.channel.send(f"Good night to you too, {nameOfUser}!")

    if "goodbye, rukhusha" in message.content.lower():
        await message.channel.send(f"goodbye, {nameOfUser}.")

    await bot.process_commands(message)

@bot.command()
async def hug(ctx, *, target):
    await ctx.send(f"*{ctx.author.global_name} sends hugs to {target}!*")

bot.run(token, log_handler = handler, log_level=logging.DEBUG)