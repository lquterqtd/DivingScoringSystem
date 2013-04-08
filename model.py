__author__ = 'Administrator'
#coding:utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Enum, Float
from datetime import datetime

engine = create_engine('sqlite:///mydata.db', echo=True)
Base = declarative_base()

class Match(Base):
    """"""
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    create_time = Column(DateTime, default=datetime.now())

class Player(Base):
    """"""
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    sex = Column(Enum(u'Male', u'Female'))
    age = Column(Integer)
    desc = Column(String)

    def get_sex(self):
        if self.sex == u'Male':
            return u'男'
        elif self.sex == u'Female':
            return u'女'

class Referee(Base):
    """"""
    __tablename__ = "referees"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    sex = Column(Enum(u'Male', u'Female'))
    age = Column(Integer)
    desc = Column(String)

    def get_sex(self):
        if self.sex == u'Male':
            return u'男'
        elif self.sex == u'Female':
            return u'女'

class Score(Base):
    """
    此表用来记录选手的每轮得分
    """
    __tablename__ = "scores"
    id = Column(Integer, primary_key=True)
    match_id = Column(Integer, ForeignKey("matches.id"))
    match = relationship("Match", backref=backref("scores", order_by=id))
    round = Column(Integer)
    player_id = Column(Integer, ForeignKey("players.id"))
    player = relationship("Player", backref=backref("scores", order_by=id))
    r_score = Column(Float(precision=1))

class MatchParticipator(Base):
    """
    此表用来记录每场比赛的参与人员，包括选手与裁判
    """
    __tablename__ = "matchparticipators"
    id = Column(Integer, primary_key=True)
    match_id = Column(Integer, ForeignKey("matches.id"))
    match = relationship("Match", backref=backref("matchparticipators", order_by=id))
    participator_id = Column(Integer)
    participator_type = Column(Enum(u'player', u'referee'))

Base.metadata.create_all(engine)