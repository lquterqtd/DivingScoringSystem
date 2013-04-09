__author__ = 'Administrator'
#coding:utf-8
import wx
from controller import get_all_referees, get_all_players, get_all_matches
from ObjectListView import ObjectListView, ColumnDefn
from controller import add_match, add_match_participator, add_match_participator_list
from model import MatchParticipator

class RefereesColumnData(object):
    def __init__(self, id, name, sex, age):
        self.id = id
        self.name = name
        self.sex = sex
        self.age = age

class PlayersColumnData(object):
    def __init__(self, id, name, sex, age):
        self.id = id
        self.name = name
        self.sex = sex
        self.age = age

class MatchInfoColumnData(object):
    def __init__(self, id, name, c_time):
        self.id = id
        self.name = name
        self.c_time = c_time.strftime('%Y-%m-%d %H:%M:%S')

class AddMatchDialog(wx.Dialog):
    def __init__(self, main_frame):
        wx.Dialog.__init__(self, None, -1, u"创建一场新的比赛", size=(540, 400))
        self.main_frame = main_frame

        box = wx.StaticBox(self, -1, u"请指定比赛名称", size=(515, 60), pos=(10, 10))
        self.match_name = wx.TextCtrl(self, -1, u"", size=(200, 20), pos=(35, 35))

        self.referees_data = []
        for i in get_all_referees():
            self.referees_data.append(RefereesColumnData(i.id, i.name, i.get_sex(), i.age))
        self.referee_resultsOlv = ObjectListView(self, style=wx.LC_REPORT|wx.SUNKEN_BORDER, size=(145, 210), sortable=False, pos=(35, 100))
        self.setRefereeResults()

        box = wx.StaticBox(self, -1, u"请选择7名裁判", size=(195, 250), pos=(10, 75))

        self.players_data = []
        for i in get_all_players():
            self.players_data.append(PlayersColumnData(i.id, i.name, i.get_sex(), i.age))
        self.player_resultsOlv = ObjectListView(self, style=wx.LC_REPORT|wx.SUNKEN_BORDER, size=(245, 210), sortable=False, pos=(250, 100))
        self.setPlayerResults()

        box = wx.StaticBox(self, -1, u"请选择参赛选手", size=(295, 250), pos=(225, 75))

        add_btn = wx.Button(self, -1, u"创建", pos=(235, 340))
        self.Bind(wx.EVT_BUTTON, self.OnAddMatch, add_btn)
    def setRefereeResults(self):
        """"""
        self.referee_resultsOlv.SetColumns(
            [
                ColumnDefn(u"姓名", 'centre', 100, "name"),
            ]
        )
        self.referee_resultsOlv.CreateCheckStateColumn()
        self.referee_resultsOlv.SetObjects(self.referees_data)
    def setPlayerResults(self):
        self.player_resultsOlv.SetColumns(
            [
                ColumnDefn(u"姓名", 'centre', 100, "name"),
                ColumnDefn(u"性别", 'centre', 50, "sex"),
                ColumnDefn(u"年龄", 'centre', 50, "age"),
            ]
        )
        self.player_resultsOlv.CreateCheckStateColumn()
        self.player_resultsOlv.SetObjects(self.players_data)
    def OnAddMatch(self, event):
        match_name = self.match_name.GetValue().strip()
        if match_name == "":
            wx.MessageBox(u"比赛的名称不可以为空")
            return
        referee_list = []
        for obj in self.referee_resultsOlv.GetObjects():
            if self.referee_resultsOlv.IsChecked(obj):
                referee_list.append(obj.id)
        if len(referee_list) != 7:
            wx.MessageBox(u"你必须选择7名裁判")
            return
        player_list = []
        for obj in self.player_resultsOlv.GetObjects():
            if self.player_resultsOlv.IsChecked(obj):
                player_list.append(obj.id)
        if len(player_list) == 0:
            wx.MessageBox(u"你需要至少选择一位选手")
            return

        match_id = add_match(match_name)
        self.main_frame.SetMatchId(match_id)

        p_list = []
        for r_id in referee_list:
            mp = MatchParticipator()
            mp.match_id = self.main_frame.match_id
            mp.participator_id = r_id
            mp.participator_type = u'referee'
            p_list.append(mp)
        add_match_participator_list(p_list)

        for p_id in player_list:
            mp = MatchParticipator()
            mp.match_id = self.main_frame.match_id
            mp.participator_id = p_id
            mp.participator_type = u'player'
            p_list.append(mp)
        add_match_participator_list(p_list)

        self.main_frame.SetRefereeList(referee_list)
        self.main_frame.SetPlayerList(player_list)
        self.main_frame.load_show_data()
        self.Destroy()


class OpenMatchDialog(wx.Dialog):
    def __init__(self, main_frame):
        wx.Dialog.__init__(self, None, -1, u"打开一场已有的比赛", size=(540, 400))
        self.main_frame = main_frame

        self.all_match = get_all_matches()
        self.match_list_data = []
        for i in self.all_match:
            self.match_list_data.append(MatchInfoColumnData(i.id, i.name, i.create_time))
        self.match_list_data.reverse()
        wx.StaticBox(self, -1, u"请选择要打开的比赛", size=(510, 350), pos=(10, 10))
        self.match_list = ObjectListView(self, style=wx.LC_REPORT|wx.SUNKEN_BORDER, size=(480, 270), pos=(25, 35))
        self.match_list.SetColumns(
            [
                ColumnDefn(u"比赛名称", 'centre', 240, "name"),
                ColumnDefn(u"创建时间", 'centre', 195, "c_time"),
            ]
        )
        self.match_list.CreateCheckStateColumn()
        self.match_list.SetObjects(self.match_list_data)

        self.open_btn = wx.Button(self, -1, u"打开", pos=(225, 320))
        self.Bind(wx.EVT_BUTTON, self.OnOpenMatch, self.open_btn)

    def OnOpenMatch(self, event):
        selected_list = []
        for obj in self.match_list.GetObjects():
            if self.match_list.IsChecked(obj):
                selected_list.append(obj)
        if len(selected_list) == 0:
            wx.MessageBox(u"你需要选择一场比赛")
            return
        elif len(selected_list) != 1:
            wx.MessageBox(u"你只能选择一场比赛")
            return
        self.main_frame.match_id = selected_list[0].id
        from controller import get_all_player_id_list, get_all_referee_id_list, get_participator_by_match
        self.main_frame.SetPlayerList(get_participator_by_match(self.main_frame.match_id, u'player'))
        self.main_frame.SetRefereeList(get_participator_by_match(self.main_frame.match_id, u'referee'))
        self.main_frame.load_show_data()
        self.Destroy()