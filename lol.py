import bs4
import discord
import requests
from bs4 import BeautifulSoup
import os


client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    game = discord.Game("롤 전적 검색")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message, value=None):
    if message.content.startswith('/롤'):
        name = message.content[3:len(message.content)]

        req = requests.get('https://www.op.gg/summoner/userName=' + name)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        rank1 = bsObj.find("div", {"class": "TierRankInfo"})
        rank2 = rank1.find("div", {"class": "TierRank"})
        rank3 = rank2.find("span", {"class": "tierRank"})
        rank4 = rank2.text
        print(rank4)
        if rank4 != 'Unranked':
            jumsu1 = rank1.find("div", {"class": "TierInfo"})
            jumsu2 = jumsu1.find("span", {"class": "LeaguePoints"})
            jumsu3 = jumsu2.text
            jumsu4 = jumsu3.strip()
            print(jumsu4)

            winlose1 = jumsu1.find("span", {"class": "WinLose"})
            winlose2 = winlose1.find("span", {"class": "wins"})
            winlose2_1 = winlose1.find("span", {"class": "losses"})
            winlose2_2 = winlose1.find("span", {"class": "winratio"})

            winlose2txt = winlose2.text
            winlose2_1txt = winlose2_1.text
            winlose2_2txt = winlose2_2.text

            print(winlose2txt + " " + winlose2_1txt + " " + winlose2_2txt)
        # print(soup)

        try:
            rank_solo = soup.find('div', {'class': 'TierRank'}).get_text()
            point = soup.find('span', {'class': 'LeaguePoints'}).get_text().split('\n')[1].split('LP')[0]
            wins = soup.find('span', {'class': 'wins'}).get_text().split('W')[0] + '승'
            losses = soup.find('span', {'class': 'losses'}).get_text().split('L')[0] + '패'
            winratio = '승률' + soup.find('span', {'class': 'winratio'}).get_text().split('Ratio')[1]

            rank_sub = soup.find('div', {'class': 'sub-tier__rank-tier'}).get_text().split('\n')[1]
            point_sub = soup.find('div', {'class': 'sub-tier__league-point'}).get_text().split('LP')[0]
            wins_losses_sub = soup.find('span', {'class': 'sub-tier__gray-text'}).get_text()
            wins_sub = wins_losses_sub.split('W')[0].split('/')[1] + 'W'
            losses_sub = wins_losses_sub.split('W')[1].split('L')[0] + 'L'
            winratio_sub = \
                '승률 ' + soup.find('div', {'class': 'sub-tier__gray-text'}).get_text().split('\n')[1].split('Rate')[1]

            champ_name = soup.find('div', {'class': 'ChampionName'}).get_text().split('\n')[2].strip()
            champ_kda = soup.find('div', {'class': 'KDA'}).get_text().split('KDA')[0].strip()
            kdaint = champ_kda.split(':')[0]
            champ_KDAEach = soup.find_all('div', {'class': 'KDAEach'})[0].get_text()
            champ_kill = champ_KDAEach.split('/')[0].strip()
            champ_death = champ_KDAEach.split('/')[1].strip()
            champ_assist = champ_KDAEach.split('/')[2].strip()
            champ_winrate_playtime = soup.find('div', {'class': 'Played'}).get_text().strip()
            champ_winrate ='승률 ' + champ_winrate_playtime.split('\n')[0].strip()
            champ_playtime = champ_winrate_playtime.split('\t\t\t\t')[1].strip().split('Played')[0]
            # print(champ_winrate)
            # print(champ_playtime)

            msg = None
            if float(kdaint) >= 4:
                msg = name + " 님의 " + " 모스트는 " + champ_name + " 입니다. "
            if 3 <= float(kdaint) < 4:
                msg = name + " 님의 " + " 모스트는 " + champ_name + " 입니다. "
            if 2 <= float(kdaint) < 3:
                msg = name + " 님의 " + " 모스트는 " + champ_name + " 입니다. "
            if float(kdaint) < 2:
                msg = name + " 님의 " + " 모스트는 " + champ_name + " 입니다. "
            print(msg)

            temp = str(soup.find('img', {'alt': champ_name}))
            champ_image = temp.split('src="//')[1]
            champ_image = "http://" + champ_image.split('"')[0]

            temp = str(soup.find_all('img', {'class': 'Image'})[2])
            tierurl = temp.split('src="//')[1]
            tierurl = "http://" + tierurl.split('"')[0]
            # print(tierurl)

            embed = discord.Embed(
                title='소환사: ' + name + '\n\n',
                description='-----솔로랭크-----',
                colour=discord.Colour.blue()
            )

            embed.add_field(name='티어(RankTier)', value=rank4, inline=False)
            embed.add_field(name='점수(LP)', value=jumsu4, inline=False)
            embed.add_field(name='승,패(Win,Lose)', value=winlose2txt + " " + winlose2_1txt, inline=False)
            embed.add_field(name='승률(Win Ratio)', value=winratio, inline=False)
            embed.add_field(name=value,
                            value='**-----자유랭크-----**',
                            inline=False)
            embed.add_field(name='티어(RankTier)', value=rank_sub, inline=False)
            embed.add_field(name='점수(LP)', value=point_sub + ' LP', inline=False)
            embed.add_field(name='승,패(Win,Lose)', value=wins_sub + " " + losses_sub, inline=False)
            embed.add_field(name='승률(Win Ratio)', value=winratio_sub, inline=False)
            embed.add_field(name='**-------- Most --------**',
                            value='**-----Champions-----**',
                            inline=False)
            embed.add_field(name='챔피언 이름', value=champ_name, inline=False)
            embed.add_field(name='[K / D / A]', value=' [ '
                                                        + champ_kill + ' / ' + champ_death + ' / ' + champ_assist + ' ] '+ ' - ' + champ_kda, inline=False)
            embed.add_field(name='승률(Win Ratio)', value=champ_winrate, inline=False)
            embed.add_field(name='모스트 게임 수', value=champ_playtime + '게임\n' + msg, inline=False)
            embed.set_image(url=champ_image)  # 모스트 챔피언 이미지
            embed.set_thumbnail(url=tierurl)  # 티어 이미지

            await message.channel.send(embed=embed)
        except:
            print("랭크 정보중 등록되지 않은 정보가 있습니다")
            await message.channel.send("정보를 불러올 수 없어요!\n" +
                                       "솔로랭크 또는 자유랭크 배치를 보지 않은 소환사에요")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
