import discord, string, random, os, json
from discord.ext import commands
from Utilities import Utilities, Colours

Utilities = Utilities()

with open('config.json') as f:
    configData = json.load(f)
 
token = configData["Token"]
prefix = configData["Prefix"]

bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())
bot.remove_command("help")

@bot.event
async def on_connect():
    Utilities.Logo()
    #Utilities.type(f"{Colours.Green} [>] Connected to {bot.user} ({bot.user.id}){Colours.Reset}")
    #Utilities.type(f"{Colours.Green} [>] Waiting to edit... {Colours.Reset}")

@bot.event
async def on_message(message):
    
    channels = []
    messages = 0

    if message.content == ".edit":
        channels.append(message.channel)
        await message.delete()
    else:
        return
    for ch in channels:
        try:
            async for msg in ch.history(limit=None):
                if msg.author == bot.user:
                    print(f"{Colours.Green} [>] Edited: {msg.content} {Colours.Reset}")
                try:
                    letters = string.ascii_letters + string.digits
                    str1ng = (''.join(random.choice(letters) for i in range(15)))
                    await msg.edit(content=str1ng)
                    await message.channel.purge(check=lambda m: m.attachments != [])
                    messages += 1

                except:
                    continue
        except:
            Utilities.type(f"{Colours.Red} [>] Can't read message history! {Colours.Reset}")
        print(f"{Colours.Green} [>] Successfully edited {messages} messages in the channel: {ch}! {Colours.Reset}")
        Utilities.Clear()
        Utilities.Logo()
        Utilities.type(f"{Colours.Green} [>] Waiting to edit... {Colours.Reset}")


if __name__ == '__main__':
    bot.run(token, bot=False)
