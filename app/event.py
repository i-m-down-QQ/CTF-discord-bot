import discord
from discord import app_commands
from discord.ext import commands

class MyCog(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot
    
  group = app_commands.Group(name="parent", description="...")
  # Above, we declare a command Group, in discord terms this is a parent command
  # We define it within the class scope (not an instance scope) so we can use it as a decorator.
  # This does have namespace caveats but i don't believe they're worth outlining in our needs.

  @app_commands.command(name="top-command")
  async def my_top_command(self, interaction: discord.Interaction) -> None:
    """ /top-command """
    await interaction.response.send_message("Hello from top level command!", ephemeral=True)

  @group.command(name="sub-command") # we use the declared group to make a command.
  async def my_sub_command(self, interaction: discord.Interaction) -> None:
    """ /parent sub-command """
    await interaction.response.send_message("Hello from the sub command!", ephemeral=True)

if __name__ == "__main__":
    print("Entrypoint: app.py")
    exit(1)