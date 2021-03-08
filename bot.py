import discord
import time
import SchoolEvents

def printer(month):
    if month == 1 or month == 2 or month == 3 or month == 4:
        return SchoolEvents.구기대회
    if month == 5:
        pack = SchoolEvents.yd_ted + '\n' + SchoolEvents.사회과_프로젝트 + '\n' + SchoolEvents.해청예술상_사진 + '\n' + SchoolEvents.해청예술상_소설 + '\n' + SchoolEvents.구기대회 
        return pack
    if month == 6:
        pack = yd_ted + '\n' + SchoolEvents.사회과_프로젝트 + '\n' + SchoolEvents.해청예술상_사진 + '\n' + SchoolEvents.해청예술상_소설 + '\n' + SchoolEvents.영어논술 + '\n' + SchoolEvents.의학탐구 + '\n' + SchoolEvents.영어말하기 + '\n' + SchoolEvents.과학과_프로젝트 + '\n' +  SchoolEvents.모의UN + '\n' + SchoolEvents.구기대회
        return pack
    if month == 7:
        pack = SchoolEvents.사회과_프로젝트 + '\n' + SchoolEvents.해청예술상_사진 + '\n' + SchoolEvents.해청예술상_소설 + '\n' + SchoolEvents.영어말하기 + '\n' + SchoolEvents.디지털_능력 + '\n' + SchoolEvents.국어경시 + '\n' + SchoolEvents.구기대회
        return pack
    if month == 8:
        pack = SchoolEvents.사회과_프로젝트 + '\n' + SchoolEvents.해청예술상_사진 + '\n' + SchoolEvents.해청예술상_소설 + '\n' + SchoolEvents.의학탐구 + '\n' + SchoolEvents.과학과_프로젝트 + '\n' + SchoolEvents.한국사골든벨 + '\n' + SchoolEvents.수학_문제해결력 + '\n' + SchoolEvents.과학경시1 + '\n' + SchoolEvents.시사상식 + '\n' + SchoolEvents.봉사체험3 + '\n' + SchoolEvents.학술주제 + '\n' + SchoolEvents.구기대회
        return pack
    if month == 9:
        pack = SchoolEvents.사회과_프로젝트 + '\n' + SchoolEvents.해청예술상_사진 + '\n' + SchoolEvents.해청예술상_소설 + '\n' + SchoolEvents.구기대회 + '\n' + SchoolEvents.심리학퀴즈 + '\n' + SchoolEvents.학술토론대회 + '\n' + SchoolEvents.스토리텔링 + '\n' + SchoolEvents.광고대회
        return pack
    if month == 10:
        pack = SchoolEvents.해청예술상_사진 + '\n' + SchoolEvents.해청예술상_소설 + '\n' + SchoolEvents.과학과_프로젝트 + '\n' + SchoolEvents.구기대회 + '\n' + SchoolEvents.미술대회 + '\n' + SchoolEvents.세계사골든벨 + '\n'
        return pack
    if month == 11:
        pack = SchoolEvents.사회과_프로젝트 + '\n' + SchoolEvents.해청예술상_사진 + '\n' + SchoolEvents.해청예술상_소설 + '\n' + SchoolEvents.과학과_프로젝트 + '\n' + SchoolEvents.구기대회 + '\n' + SchoolEvents.스토리텔링 + '\n' + SchoolEvents.마인드맵대회 + '\n' + SchoolEvents.수리통계디자인 + '\n'
        return pack
    if month == 12:
        pack = SchoolEvents.해청예술상_사진 + '\n' + SchoolEvents.해청예술상_소설 + '\n' + SchoolEvents.구기대회 + '\n' + SchoolEvents.봉사체험 + '\n' + SchoolEvents.역사능력 + '\n' + SchoolEvents.경제NIE + '\n' + SchoolEvents.진로활동 + '\n' + SchoolEvents.과학경시대회2 + '\n' + SchoolEvents.세계탐구 + '\n' + SchoolEvents.동아리활동
        return pack
today = int(time.strftime('%m', time.localtime(time.time())))
client = discord.Client()

activity = discord.Activity(name='!도와줘', type=discord.ActivityType.listening)

@client.event
async def on_ready():
    print('영동봇 도착~')
    await client.change_presence(activity=activity)
    #print(today)

@client.event
async def on_message(message):
    if message.content.startswith('!급식') or message.content.startswith('!점심'):
        embedCook = discord.Embed(title="급식정보 바로가기", description="영동고등학교의 급식 시간표에요😁", color=0x00ff00, url='http://yd.hs.kr/118220/subMenu.do')
        cookFile = discord.File("/mnt/c/Rev-1/Ubuntu/Codes/Python_Project/discord_bot/img/cookv2.jpg", filename='cookv2.jpg')
        embedCook.set_image(url='attachment://cookv2.jpg')
        await message.channel.send(file=cookFile, embed=embedCook)

    if message.content.startswith('!도와줘') or message.content.startswith('!help'):
        embedHelp = discord.Embed(title="명령 리스트", description="제가 할 수 있는 기능들이에요😎", color=0x9723A9)
        embedHelp.add_field(name='1. 명령 리스트 보기', value='!도와줘 또는 !help')
        embedHelp.add_field(name='2. 급식정보 바로가기', value='!급식 또는 !점심')
        embedHelp.add_field(name='3. 가정통신문 바로가기', value='!가통 또는 !가정통신문')
        embedHelp.add_field(name='4. 공지사항 바로가기', value='!공지 또는 !공지사항')
        embedHelp.add_field(name='5. e-book 도서관 바로가기', value='!전자책 또는 !도서관')
        embedHelp.add_field(name='6. 독서교육종합지원시스템 바로가기', value='!독후감 또는 !독서교육종합지원시스템')
        embedHelp.add_field(name='7. 교내대회일정 보기', value='!대회 또는 !교내대회일정')
        embedHelp.add_field(name='8. 만든 친구들', value='!credit 또는 !개발')
        botFile = discord.File("/mnt/c/Rev-1/Ubuntu/Codes/Python_Project/discord_bot/img/botv2.jpg", filename='botv2.jpg')
        embedHelp.set_image(url='attachment://botv2.jpg')
        await message.channel.send(file=botFile, embed=embedHelp)

    if message.content.startswith('!공지사항') or message.content.startswith('!공지'):
        embedGongji = discord.Embed(title="공지사항 바로가기", description="학교의 공지사항을 알려드릴게요😊", color=0x00FFFF, url='http://yd.hs.kr/66192/subMenu.do')
        alertFile = discord.File("/mnt/c/Rev-1/Ubuntu/Codes/Python_Project/discord_bot/img/alertv2.jpg", filename='alertv2.jpg')
        embedGongji.set_image(url='attachment://alertv2.jpg')
        await message.channel.send(file=alertFile, embed=embedGongji)

    if message.content.startswith('!가정통신문') or message.content.startswith('!가통'):
        embedGatong = discord.Embed(title='가정통신문 바로가기', description='우리 학교의 가정통신문이에요!', color=0x01AB74, url='http://yd.hs.kr/66193/subMenu.do')
        docFile = discord.File("/mnt/c/Rev-1/Ubuntu/Codes/Python_Project/discord_bot/img/docv2.jpg", filename='docv2.jpg')
        embedGatong.set_image(url='attachment://docv2.jpg')
        await message.channel.send(file=docFile, embed=embedGatong)

    if message.content.startswith('!전자책') or message.content.startswith('!도서관'):
        embedEbook = discord.Embed(title='e-book 도서관 바로가기', description='우리 학교의 e-book 도서관이에요 이건 몰랐죠?', color=0xFF8100, url='http://ydhs.yes24library.com')
        bookFile = discord.File("/mnt/c/Rev-1/Ubuntu/Codes/Python_Project/discord_bot/img/book.jpg", filename='book.jpg')
        embedEbook.set_image(url='attachment://book.jpg')
        await message.channel.send(file=bookFile, embed=embedEbook)

    if message.content.startswith('!독후감') or message.content.startswith('!독서교육종합지원시스템'):
        embedDokhugam = discord.Embed(title='독서교육종합지원시스템 바로가기', description='독후감을 작성할 수 있는 독서교육종합지원시스템이에요', color=0xFFE100, url='http://reading.ssem.or.kr')
        bookFile = discord.File("/mnt/c/Rev-1/Ubuntu/Codes/Python_Project/discord_bot/img/book.jpg", filename='book.jpg')
        embedDokhugam.set_image(url='attachment://book.jpg')
        await message.channel.send(file=bookFile, embed=embedDokhugam)


    if message.content.startswith('!대회') or message.content.startswith('!교내대회일정'):
        embedChallenge = discord.Embed(title='교내대회일정', description='이번달의 영동고등학교의 교내대회일정이에요. 많이 참가해주실거죠?', color=0x000000)
        embedChallenge.add_field(name='이번 달 대회 일정', value=printer(today))
        embedChallenge.add_field(name='다른 달 대회 일정 보기', value='다른 대회 일정을 보시려면 !(보고싶은 달)월을 입력해주세요. 예) !1월')
        winFile = discord.File("/mnt/c/Rev-1/Ubuntu/Codes/Python_Project/discord_bot/img/winv2.jpg", filename='winv2.jpg')
        embedChallenge.set_image(url='attachment://winv2.jpg')
        await message.channel.send(file=winFile, embed=embedChallenge)

    if message.content.startswith('!credit') or message.content.startswith('!개발'):
        embedDevelop = discord.Embed(title='만든 친구들', description='영동봇을 만든 친구들이에요', color=0xB8B2D0)
        embedDevelop.add_field(name='기획', value='21207 남기범, 20922 장민서, 2???? 박평준, 20511 백승현')
        embedDevelop.add_field(name='개발', value='20922 장민서, 20511 백승현')
        embedDevelop.add_field(name='디자인', value='20511 백승현')
        Devfile = discord.File("/mnt/c/Rev-1/Ubuntu/Codes/Python_Project/discord_bot/img/dev2.png", filename='dev2.png')
        embedDevelop.set_image(url='attachment://dev2.png')
        await message.channel.send(file=Devfile, embed=embedDevelop)

    if message.content.startswith('!1월'):
        embed1 = discord.Embed(title='1월 교내대회일정', description='1월의 교내대회일정이에요. 많이 참가해주실거죠?', color=0x000000)
        embed1.add_field(name='1월 대회 일정', value=printer(1))
        winFile = discord.File("/mnt/c/Rev-1/Ubuntu/Codes/Python_Project/discord_bot/img/winv2.jpg", filename='winv2.jpg')
        embed1.set_image(url='attachment://winv2.jpg')
        await message.channel.send(file=winFile, embed=embed1)

    if message.content.startswith('!2월'):
        embed2 = discord.Embed(title='2월 교내대회일정', description='2월의 교내대회일정이에요. 많이 참가해주실거죠?', color=0x000000)
        embed2.add_field(name='2월 대회 일정', value=printer(2))
        winFile = discord.File("/mnt/c/Rev-1/Ubuntu/Codes/Python_Project/discord_bot/img/winv2.jpg", filename='winv2.jpg')
        embed2.set_image(url='attachment://winv2.jpg')
        await message.channel.send(file=winFile, embed=embed2)

    if message.content.startswith('!3월'):
        embed3 = discord.Embed(title='3월 교내대회일정', description='3월의 교내대회일정이에요. 많이 참가해주실거죠?', color=0x000000)
        embed3.add_field(name='3월 대회 일정', value=printer(3))
        winFile = discord.File("/mnt/c/Rev-1/Ubuntu/Codes/Python_Project/discord_bot/img/winv2.jpg", filename='winv2.jpg')
        embed3.set_image(url='attachment://winv2.jpg')
        await message.channel.send(file=winFile, embed=embed3)

    if message.content.startswith('!4월'):
        embed4 = discord.Embed(title='4월 교내대회일정', description='4월의 교내대회일정이에요. 많이 참가해주실거죠?', color=0x000000)
        embed4.add_field(name='4월 대회 일정', value=printer(4))
        winFile = discord.File("/mnt/c/Rev-1/Ubuntu/Codes/Python_Project/discord_bot/img/winv2.jpg", filename='winv2.jpg')
        embed4.set_image(url='attachment://winv2.jpg')
        await message.channel.send(file=winFile, embed=embed4)

    if message.content.startswith('!5월'):
        embed5 = discord.Embed(title='5월 교내대회일정', description='5월의 교내대회일정이에요. 많이 참가해주실거죠?', color=0x000000)
        embed5.add_field(name='5월 대회 일정', value=printer(5))
        winFile = discord.File("/mnt/c/Rev-1/Ubuntu/Codes/Python_Project/discord_bot/img/winv2.jpg", filename='winv2.jpg')
        embed5.set_image(url='attachment://winv2.jpg')
        await message.channel.send(file=winFile, embed=embed5)

    if message.content.startswith('!6월'):
        embed6 = discord.Embed(title='6월 교내대회일정', description='6월의 교내대회일정이에요. 많이 참가해주실거죠?', color=0x000000)
        embed6.add_field(name='6월 대회 일정', value=printer(6))
        winFile = discord.File("/mnt/c/Rev-1/Ubuntu/Codes/Python_Project/discord_bot/img/winv2.jpg", filename='winv2.jpg')
        embed6.set_image(url='attachment://winv2.jpg')
        await message.channel.send(file=winFile, embed=embed6)

    if message.content.startswith('!7월'):
        embed7 = discord.Embed(title='7월 교내대회일정', description='7월의 교내대회일정이에요. 많이 참가해주실거죠?', color=0x000000)
        embed7.add_field(name='7월 대회 일정', value=printer(7))
        winFile = discord.File("/mnt/c/Rev-1/Ubuntu/Codes/Python_Project/discord_bot/img/winv2.jpg", filename='winv2.jpg')
        embed7.set_image(url='attachment://winv2.jpg')
        await message.channel.send(file=winFile, embed=embed7)

    if message.content.startswith('!8월'):
        embed8 = discord.Embed(title='8월 교내대회일정', description='8월의 교내대회일정이에요. 많이 참가해주실거죠?', color=0x000000)
        embed8.add_field(name='8월 대회 일정', value=printer(8))
        winFile = discord.File("/mnt/c/Rev-1/Ubuntu/Codes/Python_Project/discord_bot/img/winv2.jpg", filename='winv2.jpg')
        embed8.set_image(url='attachment://winv2.jpg')
        await message.channel.send(file=winFile, embed=embed8)

    if message.content.startswith('!9월'):
        embed9 = discord.Embed(title='9월 교내대회일정', description='9월의 교내대회일정이에요. 많이 참가해주실거죠?', color=0x000000)
        embed9.add_field(name='9월 대회 일정', value=printer(9))
        winFile = discord.File("/mnt/c/Rev-1/Ubuntu/Codes/Python_Project/discord_bot/img/winv2.jpg", filename='winv2.jpg')
        embed9.set_image(url='attachment://winv2.jpg')
        await message.channel.send(file=winFile, embed=embed9)

    if message.content.startswith('!10월'):
        embed10 = discord.Embed(title='10월 교내대회일정', description='10월의 교내대회일정이에요. 많이 참가해주실거죠?', color=0x000000)
        embed10.add_field(name='10월 대회 일정', value=printer(10))
        winFile = discord.File("/mnt/c/Rev-1/Ubuntu/Codes/Python_Project/discord_bot/img/winv2.jpg", filename='winv2.jpg')
        embed10.set_image(url='attachment://winv2.jpg')
        await message.channel.send(file=winFile, embed=embed10)

    if message.content.startswith('!11월'):
        embed11 = discord.Embed(title='11월 교내대회일정', description='11월의 교내대회일정이에요. 많이 참가해주실거죠?', color=0x000000)
        embed11.add_field(name='1월 대회 일정', value=printer(11))
        winFile = discord.File("/mnt/c/Rev-1/Ubuntu/Codes/Python_Project/discord_bot/img/winv2.jpg", filename='winv2.jpg')
        embed11.set_image(url='attachment://winv2.jpg')
        await message.channel.send(file=winFile, embed=embed11)

    if message.content.startswith('!12월'):
        embed12 = discord.Embed(title='12월 교내대회일정', description='12월의 교내대회일정이에요. 많이 참가해주실거죠?', color=0x000000)
        embed12.add_field(name='12월 대회 일정', value=printer(12))
        winFile = discord.File("/mnt/c/Rev-1/Ubuntu/Codes/Python_Project/discord_bot/img/winv2.jpg", filename='winv2.jpg')
        embed12.set_image(url='attachment://winv2.jpg')
        await message.channel.send(file=winFile, embed=embed12)

client.run(token)
#you can generate token in https://discord.com/developers/applications
