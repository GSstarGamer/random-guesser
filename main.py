import discord
from discord.ext import commands, tasks
import random
import json
import PyUtls as system
import logging


client = commands.Bot(command_prefix='PREFIXNOTREQUIRED')

client.onmsgready = False

with open('config.json', 'r') as f:
    config = json.load(f)
    system.log('Config loaded')

system.log('Logging in...')


@tasks.loop(seconds=2, minutes=0, hours=0)
async def mainLoop():
    try:
        if client.mode == 1:
            msg = random.choice(client.randRange)
            await client.channel.send(msg)
            system.success(
                f'Attempted number {msg}. {len(client.randRange)} numbers left')
        elif client.mode == 2:
            msg = random.choice(client.brandList)
            await client.channel.send(msg)
            client.brandList.remove(msg)
            system.success(
                f'Attempted brand {msg}. {len(client.brandList)} brands left')

    except discord.RateLimited as e:
        waitinfor = e.retry_after+random.randint(1, 15)
        system.warn(f"Ratelimited for {waitinfor}", f"waiting for {waitinfor}")
        mainLoop.change_interval(seconds=waitinfor)
    else:
        mainLoop.change_interval(seconds=random.randint(2, 4))


@client.event
async def on_ready():
    system.success(f'Logged in {client.user.name}')
    system.log('fetching channel')
    client.channel = client.get_channel(config["channelID"])
    system.success(f'Fetched channel. #{client.channel.name}')

    client.mode = int(system.binput('[1] Random number | [2] Brand\nInput: '))
    if client.mode == 1:
        client.randRange = list(range(1, int(system.binput('Numbers 1 to '))))
        mainLoop.start()
    elif client.mode == 2:
        if system.YnQn('Have you updated your brand file?'):
            with open(config['brainNamesTXT'], 'r') as f:
                client.brandList = f.read().split('\n')
                system.log(f'Got {len(client.brandList)} items')
            await mainLoop.start()
        else:
            system.warn("Press enter once your done.")
            input()
            with open(config['brainNamesTXT'], 'r') as f:
                client.brandList = f.read().split('\n')
                system.log(f'Got {len(client.brandList)} items')
            await mainLoop.start()
    else:
        system.error('invalid')
        exit()
    system.log('Loop started')
    client.onmsgready = True


@client.listen()
async def on_message(ctx: discord.Message):
    if client.onmsgready and client.mode and client.mode == 1:
        if ctx.channel == client.channel:
            if ctx.content.isnumeric():
                if int(ctx.content) in client.randRange:
                    client.randRange.remove(int(ctx.content))
                    if ctx.author != client.user:
                        system.log(
                            f"{ctx.author.display_name} attempted {ctx.content}. {len(client.randRange)} numbers left")


client.run(config["token"], log_level=logging.ERROR)
