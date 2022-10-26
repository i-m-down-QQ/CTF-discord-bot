import time
from datetime import date

import requests
from bs4 import BeautifulSoup
import nextcord
from nextcord.ext import commands

from ..params import GUILD_ID, USER_AGENT
from ..utility import parseCTFEvent, createEmbed

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
		"""
		Fetch upcoming CTFs
		"""
		now = int(time.time())
		res = requests.get(
			f"https://ctftime.org/api/v1/events/?limit={limit}&start={now}&finish=",
			headers={"user-agent": USER_AGENT}
		)
		ctfDatas = res.json()

		embeds = []
		for i in range(len(ctfDatas)):
			ctfEvent = parseCTFEvent(ctfDatas[i])
			embed = createEmbed(ctfEvent)
			embeds.append(embed)

		await interaction.response.send_message(embeds=embeds)

	@ctf.subcommand()
	async def nowrunning(self, interaction: nextcord.Interaction) -> None:
		"""
		Fetch current running CTFs
		"""
		year = date.today().year
		res = requests.get(
			f"https://ctftime.org/event/list/?year={year}&online=-1&format=0&restrictions=-1&now=true",
			headers={"user-agent": USER_AGENT}
		)
		soup = BeautifulSoup(res.text, features="html.parser")
		datas = soup.find_all('tr')

		ctf_ids = []
		for data in datas[1:]:
			id = int(data.find("a").get("href").split('/')[2])
			ctf_ids.append(id)
		
		embeds = []
		for id in ctf_ids:
			res = requests.get(
				f"https://ctftime.org/api/v1/events/{id}/",
				headers={"user-agent": USER_AGENT}
			)
			ctfData = res.json()
			ctfEvent = parseCTFEvent(ctfData)
			embed = createEmbed(ctfEvent, is_running=True)
			embeds.append(embed)
		
		await interaction.response.send_message(embeds=embeds)

def setup(bot: commands.Bot) -> None:
	bot.add_cog(CTF(bot))
