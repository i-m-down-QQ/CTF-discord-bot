import os

import nextcord
from nextcord.ext import commands

GUILD_ID = os.getenv("GUILD_ID")
assert GUILD_ID is not None, "GUILD_ID disappeared!!"
GUILD_ID = int(GUILD_ID)

class MyCog(commands.Cog):
	def __init__(self, bot: commands.Bot) -> None:
		self.bot = bot
		
	@nextcord.slash_command(guild_ids=[GUILD_ID])
	async def tests(self, interaction: nextcord.Interaction) -> None:
		""" test command """
		await interaction.response.send_message("Hello from command 1!")

def setup(bot: commands.Bot) -> None:
	bot.add_cog(MyCog(bot))