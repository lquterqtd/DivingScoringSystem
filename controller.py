__author__ = 'Administrator'
#coding:utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Match, Player, Referee, Score
from sqlalchemy import desc, asc

def add_test_data():
    """
    添加测试用的数据
    此数据不一定准确，仅做测试用
    """
    session = connectToDatabase()

    match = Match()
    match.name = u"第14届世界杯跳水赛男子单人10米跳台"
    session.add(match)

    match = Match()
    match.name = u"全国跳水冠军赛男子10米跳台"
    session.add(match)

    match = Match()
    match.name = u"雅典奥运会男子10米跳台"
    session.add(match)

    player = Player()
    player.name = u"田亮"
    player.sex = u"Male"
    player.age = int(25)
    player.desc = u"中国重庆人，跳水运动员，演员。前陕西跳水队注册运动员。在2000年悉尼奥运会，获得男子10米跳台跳水冠军；2004年雅典奥运会，和杨景辉一起获得男子双人10米跳台跳水冠军，同时还获得个人季军。"
    session.add(player)

    player = Player()
    player.name = u"胡佳"
    player.sex = u"Male"
    player.age = int(24)
    player.desc = u"湖北武汉人，中国跳水运动员（代表广东汕头）。2004雅典奥运会获得男子10米跳台跳水冠军。"
    session.add(player)

    player = Player()
    player.name = u"孟非"
    player.sex = u"Male"
    player.age = int(35)
    player.desc = u"江苏卫视著名主持人，主持过的节目《南京零距离》、《绝对唱响》、《名师高徒》、《非诚勿扰》"
    session.add(player)


    player = Player()
    player.name = u"秦凯"
    player.sex = u"Male"
    player.age = int(25)
    player.desc = u"中国男子跳水运动员，陕西西安人。"
    session.add(player)

    player = Player()
    player.name = u"郭德纲"
    player.sex = u"Male"
    player.age = int(33)
    player.desc = u"相声"
    session.add(player)

    referee = Referee()
    referee.name = u"乐嘉"
    referee.sex = u"Male"
    referee.age = int(36)
    referee.desc = u"中国性格色彩研究中心创办人，FPA(Four-colors Personality Analysis) 性格色彩创始人，培训师，电视节目主持人。"
    session.add(referee)

    referee = Referee()
    referee.name = u"黄函"
    referee.sex = u"Female"
    referee.age = int(47)
    referee.desc = u"出生于1966年，南京大学。主要著作有《走进震撼的精神世界》、《现代领导方略》、《管理者成功心理学》、《沟通协调能力》等。"
    session.add(referee)

    referee = Referee()
    referee.name = u"八哥"
    referee.sex = u"Male"
    referee.age = int(22)
    referee.desc = u"黑客"
    session.add(referee)

    referee = Referee()
    referee.name = u"球球"
    referee.sex = u"Male"
    referee.age = int(23)
    referee.desc = u"NC"
    session.add(referee)

    referee = Referee()
    referee.name = u"孙翔"
    referee.sex = u"Male"
    referee.age = int(22)
    referee.desc = u"船长"
    session.add(referee)

    referee = Referee()
    referee.name = u"建州"
    referee.sex = u"Male"
    referee.age = int(24)
    referee.desc = u"倒贴型选手"
    session.add(referee)

    referee = Referee()
    referee.name = u"晓敏"
    referee.sex = u"Male"
    referee.age = int(22)
    referee.desc = u"肾不够用了"
    session.add(referee)

    referee = Referee()
    referee.name = u"建模"
    referee.sex = u"Male"
    referee.age = int(23)
    referee.desc = u"投手"
    session.add(referee)

    referee = Referee()
    referee.name = u"YOYO"
    referee.sex = u"Male"
    referee.age = int(22)
    referee.desc = u"校长"
    session.add(referee)

    session.commit()
    session.close()


def connectToDatabase():
    """
    Connect to our SQLite database and return a Session object
    """
    engine = create_engine("sqlite:///mydata.db", echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def add_match(match_name):
    session = connectToDatabase()
    match = Match()
    match.name = match_name
    session.add(match)
    session.commit()
    session.close()

def get_all_matches():
    session = connectToDatabase()
    qry = session.query(Match).order_by(Match.create_time).all()
    session.close()
    return qry

def get_all_players():
    session = connectToDatabase()
    qry = session.query(Player).order_by(Player.name).all()
    session.close()
    return qry

def get_all_referees():
    session = connectToDatabase()
    qry = session.query(Referee).order_by(Referee.name).all()
    session.close()
    return qry