import nextcord
from nextcord.ext import commands

from ..secret import GUILD_ID

class MyCog(commands.Cog):
	def __init__(self, bot: commands.Bot) -> None:
		self.bot = bot
		
	@nextcord.slash_command(guild_ids=[GUILD_ID])
	async def ping(self, interaction: nextcord.Interaction) -> None:
		""" test bot is alive """
		latency = round(self.bot.latency * 1000, 1)
		await interaction.response.send_message(f"pong!\nlatency: {latency} ms")

def setup(bot: commands.Bot) -> None:
	bot.add_cog(MyCog(bot))
