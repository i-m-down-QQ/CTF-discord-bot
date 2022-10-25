import nextcord
from nextcord.ext import commands

from modules.secret import TOKEN

intents = nextcord.Intents.default()
intents.message_content = True
help_cmd = commands.DefaultHelpCommand(show_parameter_descriptions=True)
bot = commands.Bot(intents=intents, help_command=help_cmd)

@bot.event
async def on_ready():
	print(f"Logged in as {bot.user}.")

if __name__ == "__main__":
	cogs = ["MyCog"]
	for cog in cogs:
		bot.load_extension(f"modules.cogs.{cog}")

	bot.run(TOKEN)
