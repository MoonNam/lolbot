import discord
import openpyxl

client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    game = discord.Game("남&돈과 함께")
    await client.change_presence(status=discord.Status.online, activity=game)
    print("------------------")



@client.event
async def on_message(message, value=None):
    if message.content.startswith("/제작자"):
        await message.channel.send("제작자 : 문효찬#1973 (Nam & Don)")
    if message.content.startswith("/경고 안내"):
        await message.channel.send("경고 누적 10회 시 반성문, 누적 30회 시 퇴장입니다.")

    if message.content.startswith("/채널메시지"):
        channel = message.content[7:25]
        msg = message.content[26:]
        await client.get_channel(int(channel)).send(msg)

    if message.content.startswith("/경고"):
        author = message.guild.get_member(int(message.content[4:22]))
        file = openpyxl.load_workbook("경고.xlsx")
        sheet = file.active
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(message.author.id):
                sheet["B" + str(i)].value = int(sheet["B" + str(i)].value) + 1
                file.save("경고.xlsx")
                if sheet["B" + str(i)].value == 30:
                    await message.guild.ban(author)
                    await message.channel.send("경고 30회 누적입니다. 서버에서 추방됩니다.")
                else:
                    await message.channel.send("경고를 1회 받았습니다.")
                break
            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(message.author.id)
                sheet["B" + str(i)].value = 1
                file.save("경고.xlsx")
                await message.channel.send("경고를 1회 받았습니다.")
                break
            i += 1


client.run("NjgxODE0MzUxNzc4NTQ1Njk1.XlT7KA.ne8e3yxbyySqOGz5wZT35OqTvyo")