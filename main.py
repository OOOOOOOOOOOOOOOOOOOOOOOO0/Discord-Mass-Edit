import discord, string, random, json
from discord.ext import commands
from Utilities import Utilities, Colours

Utilities = Utilities()

with open('config.json') as f:
    configData = json.load(f)
 
token = configData["Token"]
prefix = configData["Prefix"]
mesg = configData["Message"]

bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all(), self_bot=True)
bot.remove_command("help")

@bot.event
async def on_connect():
    Utilities.Logo()
    print(f"{Colours.Green} [>] Connected to {bot.user} ({bot.user.id}){Colours.Reset}")
    Utilities.type(f"{Colours.Green} [>] Waiting to edit... {Colours.Reset}")

@bot.command()
async def edit(ctx, limit: int=None):
    messages = 0
    att = 0
    try:
        async for message in ctx.message.channel.history(limit=None).filter(lambda m: m.author == bot.user):
            try:
                if mesg == "":
                    letters = string.ascii_letters + string.digits
                    str1ng = (''.join(random.choice(letters) for i in range(15)))
                    await message.edit(content=str1ng)
                    messages +=1
                    if message.attachments:
                        await message.channel.purge(check=lambda m: m.attachments != [])
                        att += 1
                    print(f'{Colours.Green} [>] Edited: {str1ng} {Colours.Reset}')
                else:
                    await message.edit(content=mesg)
                    messages += 1
                print(f'{Colours.Green} [>] Edited: {str1ng} {Colours.Reset}')
            except:
                continue 
        Utilities.type(f'{Colours.Green} [>] Successfully edited {messages} messages and deleted {att} attatchments! {Colours.Reset}')
        Utilities.Clear()
        Utilities.Logo()
        Utilities.type(f"{Colours.Green} [>] Waiting to edit... {Colours.Reset}")
    except:
        Utilities.type(f"{Colours.Red} [>] Can't read message history! {Colours.Reset}")


if __name__ == '__main__':
    bot.run(token, bot=False)

