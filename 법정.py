import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    game = discord.Game("남&돈을 변호")
    await client.change_presence(status=discord.Status.online, activity=game)
    print("------------------")

@client.event
async def on_message(message):
    if message.content.startswith("/법정"):
        choice = message.content.split(" ")
        choicenumber = random.randint(1, len(choice)-1)
        choiceresult = choice[choicenumber]
        await message.channel.send(choiceresult)
    if message.content.startswith("/안녕"):
        await message.channel.send("안녕하세요 !")
    if message.content.startswith("/제작자"):
        await message.channel.send("제작자 : 문효찬#1973 (Nam & Don)")
client.run("NjgyMTA4ODUzOTk5MTA4MTI2.XlYOGw.PHQPaLLNwCfdSlxkoRTEs9TCN9k")

