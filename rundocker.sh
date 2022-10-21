docker build -t discordbot_python . --no-cache

docker run -dt --name discordbot --env-file=.env discordbot_python python /app/app.py

# docker run -dt --name discordbot --env-file=.env -v /mnt/c/Users/frank/Desktop/projects/ctftime_discord_bot/app:/apptemp discordbot_python
# docker exec -it discordbot python /apptemp/app.py