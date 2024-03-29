__author__ = 'Administrator'
#coding:utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Match, Player, Referee, Score, MatchParticipator
from sqlalchemy import desc, asc
from sqlalchemy import func

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
    engine = create_engine(u"sqlite:///mydata.db", echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def add_match(match_name):
    """
    增加一场比赛
    match_name : 比赛名称，暂时未限定长度，不允许重复
    """
    session = connectToDatabase()
    match = Match()
    match.name = match_name
    session.add(match)
    session.commit()
    match_id = match.id
    session.close()
    return match_id

def add_player(player_name, player_sex, player_age, player_desc):
    session = connectToDatabase()
    player = Player()
    player.name = player_name
    player.sex = player_sex
    player.age = player_age
    player.desc = player_desc
    session.add(player)
    session.commit()
    session.close()

def add_referee(referee_name, referee_sex, referee_age, referee_desc):
    session = connectToDatabase()
    referee = Referee()
    referee.name = referee_name
    referee.sex = referee_sex
    referee.age = referee_age
    referee.desc = referee_desc
    session.add(referee)
    session.commit()
    session.close()

def add_match_participator(match_id, p_id, p_type):
    session = connectToDatabase()
    p = MatchParticipator()
    p.match_id = match_id
    p.participator_id = p_id
    p.participator_type = p_type
    session.add(p)
    session.commit()
    session.close()

def add_match_participator_list(participator_list):
    session = connectToDatabase()
    for p in participator_list:
        session.add(p)
    session.commit()
    session.close()

def get_all_matches():
    """
    获取所有比赛列表
    """
    session = connectToDatabase()
    qry = session.query(Match).order_by(Match.create_time).all()
    session.close()
    return qry

def get_all_players():
    """
    获取所有选手列表
    """
    session = connectToDatabase()
    qry = session.query(Player).order_by(Player.name).all()
    session.close()
    return qry

def get_all_player_id_list():
    players_list = get_all_players()
    all_player_id_list = []
    for i in players_list:
        all_player_id_list.append(i.id)
    return all_player_id_list

def get_all_referees():
    """
    获取所有裁判列表
    """
    session = connectToDatabase()
    qry = session.query(Referee).order_by(Referee.name).all()
    session.close()
    return qry

def get_all_referee_id_list():
    referees_list = get_all_referees()
    all_referee_id_list = []
    for i in referees_list:
        all_referee_id_list.append(i.id)
    return all_referee_id_list


def get_single_round_score(match_id, player_id, round):
    """
    获取某名选手在某场比赛某轮的得分
    """
    session = connectToDatabase()
    qry = session.query(Score).filter(Score.match_id == match_id).filter(Score.player_id == player_id).filter(Score.round == round).one()
    session.close()
    return qry.r_score

def get_single_match_score(match_id, player_id):
    """
    获取某个选手在某场比赛中的总得分（计算已经获得的分数）
    """
    session = connectToDatabase()
    qry = session.query(Score).filter(Score.match_id == match_id).filter(Score.player_id == player_id)
    session.close()
    score_sum = 0.0
    for i in qry:
        score_sum += i.r_score
    return score_sum

def get_player_all_rounds_score_list(match_id, player_id):
    """
    获取某个选手在某场比赛中的得分列表（按轮次顺序排序的）,没有成绩的填充None
    """
    session = connectToDatabase()
    qry = session.query(Score).filter(Score.match_id == match_id).filter(Score.player_id == player_id).order_by(asc(Score.round))
    session.close()
    score_list = []
    for i in qry:
        score_list.append(i.r_score)
    for i in xrange(6 - len(score_list)):
        score_list.append(None)
    return score_list

def get_player_total_round(match_id, player_id):
    """
    获取选手在某场比赛中已经进行了几跳
    """
    session = connectToDatabase()
    qry = session.query(Score).filter(Score.match_id == match_id).filter(Score.player_id == player_id)
    session.close()
    count = 0
    for i in qry:
        count += 1
    return count

def get_player_by_id(player_id):
    session = connectToDatabase()
    qry = session.query(Player).filter(Player.id == player_id).one()
    session.close()
    return qry

def get_referee_by_id(referee_id):
    session = connectToDatabase()
    qry = session.query(Referee).filter(Referee.id == referee_id).one()
    session.close()
    return qry

def add_player_score(match_id, c_round, player_id, r_score):
    session = connectToDatabase()
    player_score = Score()
    player_score.match_id = match_id
    player_score.round = c_round
    player_score.player_id = player_id
    player_score.r_score = r_score
    session.add(player_score)
    session.commit()
    session.close()

def get_participator_by_match(match_id, p_type):
    session = connectToDatabase()
    qry = session.query(MatchParticipator).filter(MatchParticipator.match_id == match_id).filter(MatchParticipator.participator_type == p_type).all()
    p_list = []
    for i in qry:
        p_list.append(i.participator_id)
    session.close()
    return p_list

if __name__ == '__main__':
    add_test_data()