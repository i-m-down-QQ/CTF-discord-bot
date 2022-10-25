import os

TOKEN = os.getenv('BOT_TOKEN')
assert TOKEN is not None, "TOKEN disappeared!!"

GUILD_ID = os.getenv("GUILD_ID")
assert GUILD_ID is not None, "GUILD_ID disappeared!!"
GUILD_ID = int(GUILD_ID)