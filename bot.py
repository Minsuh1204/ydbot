#! /usr/bin/python3
import discord
import time
import SchoolEvents as ev
import usr_manager as man
#import pingpong as ai
import credentials as cred
import timer

def printer(month):
    if month == 1 or month == 2 or month == 3 or month == 4:
        return ev.EventDict['구기대회']
    if month == 5:
        pack = ev.EventDict['yd_ted'] + '\n' + ev.EventDict['사회과_프로젝트'] + '\n' + ev.EventDict['해청예술상_사진'] + '\n' + ev.EventDict['해청예술상_소설'] + '\n' + ev.EventDict['구기대회'] 
        return pack
    if month == 6:
        pack = ev.EventDict['yd_ted'] + '\n' + ev.EventDict['사회과_프로젝트'] + '\n' + ev.EventDict['해청예술상_사진'] + '\n' + ev.EventDict['해청예술상_소설'] + '\n' + ev.EventDict['영어논술'] + '\n' + ev.EventDict['의학탐구'] + '\n' + ev.EventDict['영어말하기'] + '\n' + ev.EventDict['과학과_프로젝트'] + '\n' +  ev.EventDict['모의UN'] + '\n' + ev.EventDict['구기대회']
        return pack
    if month == 7:
        pack = ev.EventDict['사회과_프로젝트'] + '\n' + ev.EventDict['해청예술상_사진'] + '\n' + ev.EventDict['해청예술상_소설'] + '\n' + ev.EventDict['영어말하기'] + '\n' + ev.EventDict['디지털_능력'] + '\n' + ev.EventDict['국어경시'] + '\n' + ev.EventDict['구기대회']
        return pack
    if month == 8:
        pack = ev.EventDict['사회과_프로젝트'] + '\n' + ev.EventDict['해청예술상_사진'] + '\n' + ev.EventDict['해청예술상_소설'] + '\n' + ev.EventDict['의학탐구'] + '\n' + ev.EventDict['과학과_프로젝트'] + '\n' + ev.EventDict['한국사_골든벨'] + '\n' + ev.EventDict['수학_문제해결력'] + '\n' + ev.EventDict['과학경시1'] + '\n' + ev.EventDict['시사상식'] + '\n' + ev.EventDict['봉사체험'] + '\n' + ev.EventDict['학술주제'] + '\n' + ev.EventDict['구기대회']
        return pack
    if month == 9:
        pack = ev.EventDict['사회과_프로젝트'] + '\n' + ev.EventDict['해청예술상_사진'] + '\n' + ev.EventDict['해청예술상_소설'] + '\n' + ev.EventDict['구기대회'] + '\n' + ev.EventDict['심리학퀴즈'] + '\n' + ev.EventDict['학술토론대회'] + '\n' + ev.EventDict['스토리텔링'] + '\n' + ev.EventDict['광고대회']
        return pack
    if month == 10:
        pack = ev.EventDict['해청예술상_사진'] + '\n' + ev.EventDict['해청예술상_소설'] + '\n' + ev.EventDict['과학과_프로젝트'] + '\n' + ev.EventDict['구기대회'] + '\n' + ev.EventDict['미술대회'] + '\n' + ev.EventDict['세계사_골든벨'] + '\n'
        return pack
    if month == 11:
        pack = ev.EventDict['사회과_프로젝트'] + '\n' + ev.EventDict['해청예술상_사진'] + '\n' + ev.EventDict['해청예술상_소설'] + '\n' + ev.EventDict['과학과_프로젝트'] + '\n' + ev.EventDict['구기대회'] + '\n' + ev.EventDict['스토리텔링'] + '\n' + ev.EventDict['마인드맵대회'] + '\n' + ev.EventDict['수리통계디자인'] + '\n'
        return pack
    if month == 12:
        pack = ev.EventDict['해청예술상_사진'] + '\n' + ev.EventDict['해청예술상_소설'] + '\n' + ev.EventDict['구기대회'] + '\n' + ev.EventDict['봉사체험'] + '\n' + ev.EventDict['역사능력'] + '\n' + ev.EventDict['경제NIE'] + '\n' + ev.EventDict['진로활동'] + '\n' + ev.EventDict['과학경시대회2'] + '\n' + ev.EventDict['세계탐구'] + '\n' + ev.EventDict['동아리활동']
        return pack
today = int(time.strftime('%m', time.localtime(time.time())))
client = discord.Client()

activity = discord.Activity(name='!도와줘', type=discord.ActivityType.listening)
ev.EventLoader()
man.usrLoader()
global mentionerList
@client.event
async def on_ready():
    print('영동봇 도착~')
    await client.change_presence(activity=activity)
    #print(today)

@client.event
async def on_message(message):
    global mentionerList
    global TimesDict
    if message.content.startswith('!급식') or message.content.startswith('!점심'):
        timer.Benchmark(0, '!급식')
        embedCook = discord.Embed(title="급식정보 바로가기", edescription="영동고등학교의 급식 시간표에요😁", color=0x00ff00, url='http://yd.hs.kr/118220/subMenu.do')
        cookFile = discord.File("./img/cookv2.jpg", filename='cookv2.jpg')
        embedCook.set_image(url='attachment://cookv2.jpg')
        await message.channel.send(file=cookFile, embed=embedCook)
        timer.Benchmark(1, '!급식')
        

    if message.content.startswith('!도와줘') or message.content.startswith('!help'):
        timer.Benchmark(0, '!도와줘')
        embedHelp = discord.Embed(title="명령 리스트", description="제가 할 수 있는 기능들이에요😎", color=0x9723A9)
        embedHelp.add_field(name='1. 명령 리스트 보기', value='!도와줘 또는 !help')
        embedHelp.add_field(name='2. 급식정보 바로가기', value='!급식 또는 !점심')
        embedHelp.add_field(name='3. 가정통신문 바로가기', value='!가통 또는 !가정통신문')
        embedHelp.add_field(name='4. 공지사항 바로가기', value='!공지 또는 !공지사항')
        embedHelp.add_field(name='5. e-book 도서관 바로가기', value='!전자책 또는 !도서관')
        embedHelp.add_field(name='6. 독서교육종합지원시스템 바로가기', value='!독후감 또는 !독서교육종합지원시스템')
        embedHelp.add_field(name='7. 교내대회일정 보기', value='!대회 또는 !교내대회일정')
        embedHelp.add_field(name='8. 만든 친구들', value='!credit 또는 !개발')
        embedHelp.add_field(name='9. 봇 추가하기', value='!add 또는 !추가')
        embedHelp.add_field(name='10. 우리반 시간표 보기', value='!시간표 또는 !timetable')
        botFile = discord.File("./img/botv2.jpg", filename='botv2.jpg')
        embedHelp.set_image(url='attachment://botv2.jpg')
        await message.channel.send(file=botFile, embed=embedHelp)
        timer.Benchmark(1, '!도와줘')

    if message.content.startswith('!공지사항') or message.content.startswith('!공지'):
        timer.Benchmark(0, '!공지')
        embedGongji = discord.Embed(title="공지사항 바로가기", description="학교의 공지사항을 알려드릴게요😊", color=0x00FFFF, url='http://yd.hs.kr/66192/subMenu.do')
        alertFile = discord.File("./img/alertv2.jpg", filename='alertv2.jpg')
        embedGongji.set_image(url='attachment://alertv2.jpg')
        await message.channel.send(file=alertFile, embed=embedGongji)
        timer.Benchmark(1, '!공지')

    if message.content.startswith('!가정통신문') or message.content.startswith('!가통'):
        timer.Benchmark(0, '!가통')
        embedGatong = discord.Embed(title='가정통신문 바로가기', description='우리 학교의 가정통신문이에요!', color=0x01AB74, url='http://yd.hs.kr/66193/subMenu.do')
        docFile = discord.File("./img/docv2.jpg", filename='docv2.jpg')
        embedGatong.set_image(url='attachment://docv2.jpg')
        await message.channel.send(file=docFile, embed=embedGatong)
        timer.Benchmark(1, '!가통')

    if message.content.startswith('!전자책') or message.content.startswith('!도서관'):
        timer.Benchmark(0, '!전자책')
        embedEbook = discord.Embed(title='e-book 도서관 바로가기', description='우리 학교의 e-book 도서관이에요 이건 몰랐죠?', color=0xFF8100, url='http://ydhs.yes24library.com')
        bookFile = discord.File("./img/book.jpg", filename='book.jpg')
        embedEbook.set_image(url='attachment://book.jpg')
        await message.channel.send(file=bookFile, embed=embedEbook)
        timer.Benchmark(1, '!전자책')

    if message.content.startswith('!독후감') or message.content.startswith('!독서교육종합지원시스템'):
        timer.Benchmark(0, '!독후감')
        embedDokhugam = discord.Embed(title='독서교육종합지원시스템 바로가기', description='독후감을 작성할 수 있는 독서교육종합지원시스템이에요', color=0xFFE100, url='http://reading.ssem.or.kr')
        bookFile = discord.File("./img/book.jpg", filename='book.jpg')
        embedDokhugam.set_image(url='attachment://book.jpg')
        await message.channel.send(file=bookFile, embed=embedDokhugam)
        timer.Benchmark(1, '!독후감')


    if message.content.startswith('!대회') or message.content.startswith('!교내대회일정'):
        timer.Benchmark(0, '!대회')
        embedChallenge = discord.Embed(title='교내대회일정', description='이번달의 영동고등학교의 교내대회일정이에요. 많이 참가해주실거죠?', color=0x000000)
        embedChallenge.add_field(name='이번 달 대회 일정', value=printer(today))
        embedChallenge.add_field(name='다른 달 대회 일정 보기', value='다른 대회 일정을 보시려면 !(보고싶은 달)월을 입력해주세요. 예) !1월')
        winFile = discord.File("./img/winv2.jpg", filename='winv2.jpg')
        embedChallenge.set_image(url='attachment://winv2.jpg')
        await message.channel.send(file=winFile, embed=embedChallenge)
        timer.Benchmark(1, '!대회')

    if message.content.startswith('!credit') or message.content.startswith('!개발') or message.content.startswith('!dev'):
        timer.Benchmark(0, '!dev')
        embed_gbnam = discord.Embed(title='남기범', description='카카오톡 챗봇 개발을 담당한 남기범입니다. 챗봇으로 즐거운 학교생활하세요', color=0x658FFD)
        file_gbnam = discord.File('./img/gbnam.jpg', filename='gbnam.jpg')
        embed_gbnam.set_image(url='attachment://gbnam.jpg')
        embed_mschang = discord.Embed(title='장민서', description='디스코드 챗봇 개발을 담당한 장민서입니다. 잘 써주세요!~~', color=0xFFCA19)
        file_mschang = discord.File('./img/ms_chang.jpg', filename='ms_chang.jpg')
        embed_mschang.set_image(url='attachment://ms_chang.jpg')
        embed_paiksh = discord.Embed(title='백승현', description='디스코드 챗봇 디자인을 담당한 백승현입니다. 학교 알림을 확인하세요~', color=0xEF7A0F)
        file_paiksh = discord.File('./img/paik_sh.jpg', filename='paik_sh.jpg')
        embed_paiksh.set_image(url='attachment://paik_sh.jpg')
        embed_pjpark = discord.Embed(title='박평준', description='카카오톡 챗봇 디자인을 담당한 박평준입니다. 감사합니다~!', color=0xF0F0F0)
        file_pjpark = discord.File('./img/pjpark.jpg', filename='pjpark.jpg')
        embed_pjpark.set_image(url='attachment://pjpark.jpg')
        await message.channel.send(file=file_mschang, embed=embed_mschang)
        await message.channel.send(file=file_paiksh, embed=embed_paiksh)
        await message.channel.send(file=file_gbnam, embed=embed_gbnam)
        await message.channel.send(file=file_pjpark, embed=embed_pjpark)
        timer.Benchmark(1, '!dev')

    if message.content.startswith('!add') or message.content.startswith('!추가') or message.content.startswith('!share') or message.content.startswith('!공유'):
        timer.Benchmark(0, '!add')
        embedShare = discord.Embed(title='디스코드 봇 추가하기', description='우리 디스코드 봇을 이 링크를 통해서 추가해주세요!', color=0xB8B2D0, url='https://discord.com/api/oauth2/authorize?client_id=796194055964459038&permissions=63488&scope=bot')
        shareFile = discord.File('./img/qrcode.jpg', filename='qrcode.jpg')
        embedShare.set_image(url='attachment://qrcode.jpg')
        await message.channel.send(file=shareFile, embed=embedShare)
        timer.Benchmark(1, '!add')

    if message.content.startswith('!timetable') or message.content.startswith('!시간표'):
        timer.Benchmark(0, '!시간표')
        timeSplited = message.content.split()
        if len(timeSplited) > 1 and str(type(timeSplited[1])) == "<class 'int'>":
            embedOtherClass = discord.Embed(title='시간표 보기', description='시간표를 보여드릴게요!', color=0xB8B2D0)
            OtherClassFile = discord.File('./img/{0}.jpg'.format(timeSplited[1]), filename='{0}.jpg'.format(timeSplited[1]))
            embedOtherClass.set_image(url='attachment://{0}.jpg'.format(timeSplited[1]))
            await message.channel.send(file=OtherClassFile, embed=embedOtherClass)
        else:
            if int(message.author.id) == int(client.user.id):
                if man.Whereis(int(mentionerList[0])) == 0:
                    embedClass = discord.Embed(title='사용자 반 등록하기', description='봇을 더 유용하게 사용하기 위해 반정보를 등록해주세요!', color=0xB8B2D0)
                    embedClass.add_field(name='등록법', value='!등록 (반)으로 반을 등록해주세요!')
                    embedClass.add_field(name='예시', value='2학년 9반일 경우 -> !등록 209  /  1학년 10반일 경우 -> !등록 110')
                    await message.channel.send(embed=embedClass)
                else:
                    usr_class = man.Whereis(int(mentionerList[0]))
                    embedUsrClass = discord.Embed(title='우리반 시간표 보기', description='우리반 시간표를 보여드릴게요!    다른 반 시간표를 보시려면 "!시간표 (반)"을 입력해주세요~', color=0xB8B2D0)
                    UsrClassFile = discord.File('./img/{0}.jpg'.format(usr_class), filename='{0}.jpg'.format(usr_class))
                    embedUsrClass.set_image(url='attachment://{0}.jpg'.format(usr_class))
                    await message.channel.send(file=UsrClassFile, embed=embedUsrClass)
            else:
                if man.Whereis(int(message.author.id)) == 0:
                    embedClass = discord.Embed(title='사용자 반 등록하기', description='봇을 더 유용하게 사용하기 위해 반정보를 등록해주세요!', color=0xB8B2D0)
                    embedClass.add_field(name='등록법', value='!등록 (반)으로 반을 등록해주세요!')
                    embedClass.add_field(name='예시', value='2학년 9반일 경우 -> !등록 209  /  1학년 10반일 경우 -> !등록 110')
                    await message.channel.send(embed=embedClass)
                else:
                    usr_class = man.Whereis(int(message.author.id))
                    embedUsrClass = discord.Embed(title='우리반 시간표 보기', description='우리반 시간표를 보여드릴게요!    다른 반 시간표를 보시려면 "!시간표 (반)"을 입력해주세요~', color=0xB8B2D0)
                    UsrClassFile = discord.File('./img/{0}.jpg'.format(usr_class), filename='{0}.jpg'.format(usr_class))
                    embedUsrClass.set_image(url='attachment://{0}.jpg'.format(usr_class))
                    print(man.usrDict)
                    print('\n')
                    await message.channel.send(file=UsrClassFile, embed=embedUsrClass)
        timer.Benchmark(1, '!시간표')

    if message.content.startswith('!sec'):
        devSplited = message.content.split()
        if devSplited[1] == 'discrimination':
            await message.channel.send(message.author.id)
        if devSplited[1] == 'show_list':
            await message.channel.send(man.usrDict)
        if devSplited[1] == 'time_check':
            await message.channel.send(timer.TimesDict)
        if devSplited[1] == 'time_average':
            await message.channel.send(timer.Average(str(devSplited[2])))

    if message.content.startswith('!등록') or message.content.startswith('!register'):
        timer.Benchmark(0, '!등록')
        classSplited = message.content.split()
        man.usrAdd(int(message.author.id), int(classSplited[1]))
        if man.Whereis(int(message.author.id)) == int(classSplited[1]):
            await message.channel.send('등록 성공! 이제 "!시간표"만으로 시간표를 보여드릴 수 있게 됐어요!')
        else:
            await message.channel.send('알 수 없는 문제로 등록이 되지 않았습니다. mschang1204@naver.com으로 문제상황을 알려주세요')
        timer.Benchmark(1, '!등록')

    if message.content.startswith('!1월'):
        embed1 = discord.Embed(title='1월 교내대회일정', description='1월의 교내대회일정이에요. 많이 참가해주실거죠?', color=0x000000)
        embed1.add_field(name='1월 대회 일정', value=printer(1))
        winFile = discord.File("./img/winv2.jpg", filename='winv2.jpg')
        embed1.set_image(url='attachment://winv2.jpg')
        await message.channel.send(file=winFile, embed=embed1)

    if message.content.startswith('!2월'):
        embed2 = discord.Embed(title='2월 교내대회일정', description='2월의 교내대회일정이에요. 많이 참가해주실거죠?', color=0x000000)
        embed2.add_field(name='2월 대회 일정', value=printer(2))
        winFile = discord.File("./img/winv2.jpg", filename='winv2.jpg')
        embed2.set_image(url='attachment://winv2.jpg')
        await message.channel.send(file=winFile, embed=embed2)

    if message.content.startswith('!3월'):
        embed3 = discord.Embed(title='3월 교내대회일정', description='3월의 교내대회일정이에요. 많이 참가해주실거죠?', color=0x000000)
        embed3.add_field(name='3월 대회 일정', value=printer(3))
        winFile = discord.File("./img/winv2.jpg", filename='winv2.jpg')
        embed3.set_image(url='attachment://winv2.jpg')
        await message.channel.send(file=winFile, embed=embed3)

    if message.content.startswith('!4월'):
        embed4 = discord.Embed(title='4월 교내대회일정', description='4월의 교내대회일정이에요. 많이 참가해주실거죠?', color=0x000000)
        embed4.add_field(name='4월 대회 일정', value=printer(4))
        winFile = discord.File("./img/winv2.jpg", filename='winv2.jpg')
        embed4.set_image(url='attachment://winv2.jpg')
        await message.channel.send(file=winFile, embed=embed4)

    if message.content.startswith('!5월'):
        embed5 = discord.Embed(title='5월 교내대회일정', description='5월의 교내대회일정이에요. 많이 참가해주실거죠?', color=0x000000)
        embed5.add_field(name='5월 대회 일정', value=printer(5))
        winFile = discord.File("./img/winv2.jpg", filename='winv2.jpg')
        embed5.set_image(url='attachment://winv2.jpg')
        await message.channel.send(file=winFile, embed=embed5)

    if message.content.startswith('!6월'):
        embed6 = discord.Embed(title='6월 교내대회일정', description='6월의 교내대회일정이에요. 많이 참가해주실거죠?', color=0x000000)
        embed6.add_field(name='6월 대회 일정', value=printer(6))
        winFile = discord.File("./img/winv2.jpg", filename='winv2.jpg')
        embed6.set_image(url='attachment://winv2.jpg')
        await message.channel.send(file=winFile, embed=embed6)

    if message.content.startswith('!7월'):
        embed7 = discord.Embed(title='7월 교내대회일정', description='7월의 교내대회일정이에요. 많이 참가해주실거죠?', color=0x000000)
        embed7.add_field(name='7월 대회 일정', value=printer(7))
        winFile = discord.File("./img/winv2.jpg", filename='winv2.jpg')
        embed7.set_image(url='attachment://winv2.jpg')
        await message.channel.send(file=winFile, embed=embed7)

    if message.content.startswith('!8월'):
        embed8 = discord.Embed(title='8월 교내대회일정', description='8월의 교내대회일정이에요. 많이 참가해주실거죠?', color=0x000000)
        embed8.add_field(name='8월 대회 일정', value=printer(8))
        winFile = discord.File("./img/winv2.jpg", filename='winv2.jpg')
        embed8.set_image(url='attachment://winv2.jpg')
        await message.channel.send(file=winFile, embed=embed8)

    if message.content.startswith('!9월'):
        embed9 = discord.Embed(title='9월 교내대회일정', description='9월의 교내대회일정이에요. 많이 참가해주실거죠?', color=0x000000)
        embed9.add_field(name='9월 대회 일정', value=printer(9))
        winFile = discord.File("./img/winv2.jpg", filename='winv2.jpg')
        embed9.set_image(url='attachment://winv2.jpg')
        await message.channel.send(file=winFile, embed=embed9)

    if message.content.startswith('!10월'):
        embed10 = discord.Embed(title='10월 교내대회일정', description='10월의 교내대회일정이에요. 많이 참가해주실거죠?', color=0x000000)
        embed10.add_field(name='10월 대회 일정', value=printer(10))
        winFile = discord.File("./img/winv2.jpg", filename='winv2.jpg')
        embed10.set_image(url='attachment://winv2.jpg')
        await message.channel.send(file=winFile, embed=embed10)

    if message.content.startswith('!11월'):
        embed11 = discord.Embed(title='11월 교내대회일정', description='11월의 교내대회일정이에요. 많이 참가해주실거죠?', color=0x000000)
        embed11.add_field(name='1월 대회 일정', value=printer(11))
        winFile = discord.File("./img/winv2.jpg", filename='winv2.jpg')
        embed11.set_image(url='attachment://winv2.jpg')
        await message.channel.send(file=winFile, embed=embed11)

    if message.content.startswith('!12월'):
        embed12 = discord.Embed(title='12월 교내대회일정', description='12월의 교내대회일정이에요. 많이 참가해주실거죠?', color=0x000000)
        embed12.add_field(name='12월 대회 일정', value=printer(12))
        winFile = discord.File("./img/winv2.jpg", filename='winv2.jpg')
        embed12.set_image(url='attachment://winv2.jpg')
        await message.channel.send(file=winFile, embed=embed12)

client.run(cred.tokenLoader())