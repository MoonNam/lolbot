import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    game = discord.Game("로또 번호 예측")
    await client.change_presence(status=discord.Status.online, activity=game)
    print("------------------")

@client.event
async def on_message(message):
    if message.content.startswith("/로또 번호 예측"):
        Text = ""
        number = [1, 2, 3, 4, 5, 6, 7]
        count = 0
        for i in range(0, 7):
            num = random.randrange(1, 46)
            number[i] = num
            if count >= 1:
                for i2 in range(0, i):
                    if number[i] == number[i2]:
                        numberText = number[i]
                        print("작동 이전값 : " + str(numberText))
                        number[i] = random.randrange(1, 46)
                        numberText = number[i]
                        print("작동 현재값 : " + str(numberText))
                        if number[i] == number[i2]:
                            numberText = number[i]
                            print("작동 이전값 : " + str(numberText))
                            number[i] = random.randrange(1, 46)
                            numberText = number[i]
                            print("작동 현재값 : " + str(numberText))
                            if number[i] == number[i2]:
                                numberText = number[i]
                                print("작동 이전값 : " + str(numberText))
                                number[i] = random.randrange(1, 46)
                                numberText = number[i]
                                print("작동 현재값 : " + str(numberText))

            count = count + 1
            Text = Text + "  " + str(number[i])

        print(Text.strip())
        embed = discord.Embed(
            title="로또 번호는 !",
            description=Text.strip(),
            colour=discord.Color.gold()
        )
        embed.set_thumbnail(url="https://www.newsinside.kr/news/photo/201409/265844_19464_3015.PNG")
        await message.channel.send(embed=embed)

    if message.content.startswith("!제작자"):
        await message.channel.send("제작자 : 문효찬#1973 (Nam & Don)")

client.run("NjgyMTk2NzkwODYyMjgyNzU3.XlZjqw.zr3g-zOhWGHNiKcdmO8nZXx1ShU")