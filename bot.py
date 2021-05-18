import discord
from discord.ext import commands

client = commands.bot(commands_prefix=".")

@client.event
async def on_ready():
	print("bot is ready")

@client.command()
async def hello (ctx):
	await ctx.send("meow")

client.run("ODE1MjU4MTQzNzk2ODg3NTcy.YDpyUA.z6N3OYhgvaPBBfytYci1mHqCmUI")