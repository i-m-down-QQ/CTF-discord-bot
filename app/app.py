from discord.ext import commands 
import discord
import os

TOKEN = os.getenv('BOT_TOKEN')
assert TOKEN is not None, "TOKEN disappeared!!"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def pingg(ctx):
	"""Ping test."""
	await ctx.send('pongg')

@bot.command()
async def sayhi(ctx, who: str):
	"""Say hi to sb."""
	await ctx.send(f'hi {who}')

@bot.command()
async def gg(ctx, who: str):
	"""Say hi to sb."""
	await ctx.send(f'gg {who}')

bot.run(TOKEN)

# async def setup(bot: commands.Bot) -> None:
# 	await bot.add_cog(MyCog(bot))