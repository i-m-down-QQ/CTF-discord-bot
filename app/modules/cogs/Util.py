import time

import requests
import nextcord
from nextcord.ext import commands

from ..params import GUILD_ID, USER_AGENT


class Util(commands.Cog):
	def __init__(self, bot: commands.Bot) -> None:
		self.bot = bot
		
	@nextcord.slash_command(guild_ids=[GUILD_ID])
	async def ping(self, interaction: nextcord.Interaction) -> None:
		"""
		Test bot is alive
		"""
		latency = round(self.bot.latency * 1000, 1)
		await interaction.response.send_message(f"pong!\nlatency: {latency} ms")
	
	@nextcord.slash_command(guild_ids=[GUILD_ID])
	async def ping_ctftime(self, interaction: nextcord.Interaction) -> None:
		"""
		Test CTFtime API is alive
		"""
		t0 = time.time()
		res = requests.get("https://ctftime.org/api/v1/top/", headers={"user-agent": USER_AGENT})
		t1 = time.time()
		latency = round((t1 - t0) * 1000, 1)
		status_code = res.status_code
		await interaction.response.send_message(f"pong!\nstatus code: {status_code}\nlatency: {latency} ms")

def setup(bot: commands.Bot) -> None:
	bot.add_cog(Util(bot))
