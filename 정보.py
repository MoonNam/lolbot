import discord
import datetime

client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    game = discord.Game("마케팅")
    await client.change_presence(status=discord.Status.online, activity=game)
    print("------------------")

@client.event
async def on_message(message, value=None):
    if message.content.startswith("/명함"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name="회사", value="남&돈", inline=True)
        embed.add_field(name="성함", value=message.author.name, inline=True)
        embed.add_field(name="직급", value=message.author.display_name, inline=True)
        embed.add_field(name="TEL", value="032-999-1943", inline=True)
        embed.add_field(name="주소", value="인천광역시 남동구 테크노벨리", inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    if message.content.startswith("/제작자"):
        await message.channel.send("제작자 : 문효찬#1973 (Nam & Don)")

client.run("NjgxODczOTgxMDc4NjM0NTA3.XlUyxg.iwKgwSdAPzVRtwDn6LN2zNvLnok")