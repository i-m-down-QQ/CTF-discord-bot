import time

import requests
import nextcord
from nextcord.ext import commands

from ..secret import GUILD_ID


class CTF(commands.Cog):
	def __init__(self, bot: commands.Bot) -> None:
		self.bot = bot

	@nextcord.slash_command(guild_ids=[GUILD_ID])
	async def ctf(interaction: nextcord.Interaction):
		"""
		This is the main slash command that will be the prefix of all commands below.
		This will never get called since it has subcommands.
		"""
		pass

	@ctf.subcommand()
	async def upcoming(self, interaction: nextcord.Interaction, limit: int=3) -> None:
		""" fetch upcoming CTFs """
		default_image = "https://pbs.twimg.com/profile_images/2189766987/ctftime-logo-avatar_400x400.png"

		USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52"
		now = int(time.time())
		res = requests.get(f"https://ctftime.org/api/v1/events/?limit={limit}&start={now}&finish=", headers={"user-agent": USER_AGENT})
		ctfData = res.json()

		embeds = []
		for i in range(len(ctfData)):
			imageurl = ctfData[i]["logo"]
			imageurl = default_image if imageurl == "" else imageurl
			location = ctfData[i]["location"] if ctfData[i]["onsite"] else "Onsite"
			organizers = "".join([o["name"] for o in ctfData[i]["organizers"]])
			duration = f"{ctfData[i]['duration']['days']} days {ctfData[i]['duration']['hours']} hours"
			date = ctfData[i]["start"] + "\n-\n" + ctfData[i]["finish"]
			restriction = "None" if ctfData[i]["restrictions"] == "Open" else ctfData[i]["restrictions"]

			embed = nextcord.Embed(
				title = ctfData[i]["title"], 
				description=ctfData[i]["description"],
				url = ctfData[i]["url"]
			)
			embed.set_thumbnail(url=imageurl)
			embed.add_field(name="Origanizers", value=organizers, inline=True)
			embed.add_field(name="Location", value=location, inline=True)
			embed.add_field(name="Format", value=ctfData[i]["format"], inline=True)

			embed.add_field(name="Weight", value=str(ctfData[i]["weight"]), inline=True)
			embed.add_field(name="Duration", value=duration, inline=True)
			embed.add_field(name="Date", value=date, inline=True)

			embed.add_field(name="Restriction", value=restriction, inline=True)
			embed.set_footer(text=f"CTF ID: {ctfData[i]['id']}")

			embeds.append(embed)

		await interaction.response.send_message(embeds=embeds)

	@ctf.subcommand()
	async def my_sub_command(self, interaction: nextcord.Interaction) -> None:
		""" /parent sub-command """
		await interaction.response.send_message("Hello from the sub command!", ephemeral=True)

def setup(bot: commands.Bot) -> None:
	bot.add_cog(CTF(bot))
