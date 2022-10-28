# CTF discord bot

<!-- TOC -->

- [CTF discord bot](#ctf-discord-bot)
    - [Installation](#installation)
    - [Usage](#usage)
        - [Util](#util)
        - [CTF](#ctf)
    - [Contect](#contect)

<!-- /TOC -->

<!-- Existed bot invite link: https://discord.com/api/oauth2/authorize?client_id=1031857604177178634&permissions=274877991936&scope=bot -->

---

## Installation
1. Enroll a discord bot on [discord developer protal](https://discord.com/developers/applications/)
2. Generate env file from template
    ```bash
    cp .env.template .env

    # modify BOT_TOKEN and GUILD_ID
    vi .env
    ```
3. run docker
    ```bash
    chmod +x rundocker.sh
    ./rundocker.sh
    ```
4. run `/sync` command on your testing server

## Usage
### Util
`/help`

Show help menu

`/ping`

Test bot is alive and get its latency

`/ping_ctftime`

Test CTFtime API is alive and get its latency

`/sync`

(**GUILD ONLY**) Sync commands to all servers

### CTF
`/ctf upcoming [limit_num]`

Fetch upcoming events from CTFtime

`/ctf nowrunning`

Fetch nowrunning events from CTFtime

## Contect
If there is any problem, feel free to contect us.

Email: iamdownqq@gmail.com