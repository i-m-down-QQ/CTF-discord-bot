import os


TOKEN = os.getenv('BOT_TOKEN')
assert TOKEN is not None, "TOKEN disappeared!!"

GUILD_ID = os.getenv("GUILD_ID")
assert GUILD_ID is not None, "GUILD_ID disappeared!!"
GUILD_ID = int(GUILD_ID)

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52"
DEFAULT_IMAGE_URL = "https://pbs.twimg.com/profile_images/2189766987/ctftime-logo-avatar_400x400.png"

DESCRIPTIONS = {
    "util": 
    """
    `/help`
    ➜ Show help menu.
    `/ping`
    ➜ Test bot is alive and get its latency
    `/ping_ctftime`
    ➜ Test CTFtime API is alive and get its latency
    `/sync`
    ➜ (**GUILD ONLY**) Sync commands to all servers

    """,

    "ctf": 
    """
    `/ctf upcoming [limit_num]`
    ➜ Fetch upcoming events from CTFtime
    `/ctf nowrunning`
    ➜ Fetch nowrunning events from CTFtime
    
    """
}