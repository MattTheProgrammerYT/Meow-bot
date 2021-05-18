import discord
from discord.ext import commands

client = commands.bot(commands_prefix=".")

@client.event
async def on_ready():
	print("bot is ready")

@client.command()
async def hello (ctx):
	await ctx.send("meow")

client.run("HZgQZApgE9tjb7RkQ8SvA8la42Ja3SMt")
