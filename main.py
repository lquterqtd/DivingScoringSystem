__author__ = 'Administrator'
#coding:utf-8
import wx
from mydialog import AddMatchDialog, OpenMatchDialog
from calculate_score import calculate_score
from ObjectListView import ObjectListView, ColumnDefn
from controller import get_player_by_id, get_referee_by_id, get_player_all_rounds_score_list, get_player_total_round, add_player_score
import sys


class ResultColumnData(object):
    def __init__(self, id, name, s_1, s_2, s_3, s_4, s_5, s_6, s_total):
        self.id = id
        self.name = name
        self.s_1 = s_1
        self.s_2 = s_2
        self.s_3 = s_3
        self.s_4 = s_4
        self.s_5 = s_5
        self.s_6 = s_6
        self.s_total = s_total

def get_show_score(score):
    if score == None:
        return ""
    else:
        return "%.1f" % score

class MainPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, id=wx.ID_ANY,
            title=u"跳水打分系统", size=(800,600))
        self.panel = MainPanel(self)
        self.icon = wx.Icon('diving.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        self.SetMaxSize(wx.Size(800, 600))
        self.SetMinSize(wx.Size(800, 600))

        menuBar = wx.MenuBar()
        start_menu = wx.Menu()
        new_match = start_menu.Append(-1, u"开始一场新的比赛\tCtrl-N")
        self.Bind(wx.EVT_MENU, self.OnNewMatch, new_match)
        open_match = start_menu.Append(-1, u"打开已经有比赛\tCtrl-O")
        self.Bind(wx.EVT_MENU, self.OnOpenMatch, open_match)
        menuBar.Append(start_menu, u"开始")
        help_menu = wx.Menu()
        about = help_menu.Append(-1, u"关于")
        menuBar.Append(help_menu, u"帮助")
        self.Bind(wx.EVT_MENU, self.OnAbout, about)
        self.SetMenuBar(menuBar)

        acceltbl = wx.AcceleratorTable(
            [
                (
                    wx.ACCEL_CTRL, ord('N'), new_match.GetId()
                ),
                (
                    wx.ACCEL_CTRL, ord('O'), open_match.GetId()
                ),
            ]
        )
        self.SetAcceleratorTable(acceltbl)

        select_player_box = wx.StaticBox(self.panel, -1, u"选择出场选手", size=(150, 70), pos=(10, 10))
        self.select_player = wx.Choice(self.panel, -1, choices=[], pos=(25, 40))

        difficulty_box = wx.StaticBox(self.panel, -1, u"指定难度系数", size=(150, 70), pos=(10, 90))
        self.difficulty_text = wx.TextCtrl(self.panel, -1, pos=(25, 120))

        scores_box = wx.StaticBox(self.panel, -1, u"各裁判给分", size=(600, 150), pos=(170, 10))
        x_offset = 180
        y_offset = 50
        count = 0
        self.s_text_list = []
        self.s_label_list = []
        for i in xrange(0, 7):
            referee_name = wx.StaticText(self.panel, -1, u"", size=(50 , 20), pos=(x_offset + 90 * count, y_offset), style=wx.ALIGN_CENTER)
            self.s_label_list.append(referee_name)
            scores_text = wx.TextCtrl(self.panel, -1, size=(45, 20), pos=(x_offset + 90 * count, 80))
            self.s_text_list.append(scores_text)
            count += 1

        calc_btn = wx.Button(self.panel, -1, u"计算此跳得分", pos=(200, 120))
        self.Bind(wx.EVT_BUTTON, self.CalcScore, calc_btn)

        font = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.round_score = wx.StaticText(self.panel, -1, u"", size=(200, 30), pos=(350, 115))
        self.round_score.SetFont(font)

        result_box = wx.StaticBox(self.panel, -1, u"计分板", size=(760, 350), pos=(10, 170))

        self.result_data = []
        self.result_data_listview = wx.ListView(self.panel, -1, style=wx.LC_REPORT, size=(730, 300), pos=(25, 195))
        self.result_data_listview.InsertColumn(0, u'姓名', width=80, format=wx.LIST_FORMAT_CENTRE)
        self.result_data_listview.InsertColumn(1, u'第一跳得分', width=90, format=wx.LIST_FORMAT_CENTRE)
        self.result_data_listview.InsertColumn(2, u'第二跳得分', width=90, format=wx.LIST_FORMAT_CENTRE)
        self.result_data_listview.InsertColumn(3, u'第三跳得分', width=90, format=wx.LIST_FORMAT_CENTRE)
        self.result_data_listview.InsertColumn(4, u'第四跳得分', width=90, format=wx.LIST_FORMAT_CENTRE)
        self.result_data_listview.InsertColumn(5, u'第五跳得分', width=90, format=wx.LIST_FORMAT_CENTRE)
        self.result_data_listview.InsertColumn(6, u'第六跳得分', width=90, format=wx.LIST_FORMAT_CENTRE)
        self.result_data_listview.InsertColumn(7, u'总分', width=90, format=wx.LIST_FORMAT_CENTRE)

    def OnNewMatch(self, event):
        #wx.MessageBox(u"开始一场新的比赛")
        dlg = AddMatchDialog(self)
        dlg.ShowModal()
        dlg.Destroy()

    def OnOpenMatch(self, event):
        dlg = OpenMatchDialog(self)
        dlg.ShowModal()
        dlg.Destroy()

    def OnAbout(self, event):
        wx.MessageBox(u"这是一个跳水打分系统的Demo版本")

    def SetMatchId(self, match_id):
        self.match_id = match_id

    def SetPlayerList(self, player_list):
        self.player_list = player_list

    def SetRefereeList(self, referee_list):
        self.referee_list = referee_list

    def StartMatch(self):
        pass
    def CalcScore(self, event):
        index = self.select_player.GetSelection()
        if index == wx.NOT_FOUND:
            wx.MessageBox(u"请选择一名选手")
            return
        player_id = self.select_player.GetClientData(self.select_player.GetSelection())
        which_round = get_player_total_round(self.match_id, player_id)
        if which_round == 6:
            wx.MessageBox(u"%s的比赛已经结束" % self.select_player.GetStringSelection())
            return
        difficulty =self.difficulty_text.GetValue().strip()
        if difficulty == "":
            wx.MessageBox(u"请指定此跳的难度系数")
            return
        try:
            difficulty = float(difficulty)
        except:
            wx.MessageBox(u"请输入正确的难度系数")
            return
        else:
            if difficulty < 1.0 or difficulty > 4.8:
                wx.MessageBox(u"难度系数应该在2.0~3.6之前")
                return
        score_list = []
        for i in self.s_text_list:
            temp_score = i.GetValue().strip()
            if temp_score == "":
                wx.MessageBox(u"七名裁判必须都给出打分")
                return
            else:
                try:
                    temp_score = float(temp_score)
                except:
                    wx.MessageBox(u"七名裁判必须都给出正确打分")
                    return
                else:
                    if temp_score < 0.0 and temp_score > 10.0:
                        wx.MessageBox(u"得分只能在0.0~10.0之间")
                        return
                    score_list.append(temp_score)
        if len(score_list) == 7:
            res = calculate_score(
                {
                    "score_list":score_list,
                    "difficulty":difficulty,
                }
            )
            self.round_score.SetLabel(res['expression'])

        add_player_score(self.match_id, which_round, player_id, res["final_score"])
        self.fill_list_view()

    def load_show_data(self):
        self.select_player.Clear()
        for p in self.player_list:
            player_info = get_player_by_id(p)
            self.select_player.Append(player_info.name, player_info.id)
        index = 0
        for r in self.referee_list:
            referee_info = get_referee_by_id(r)
            self.s_label_list[index].SetLabel(referee_info.name)
            index += 1
        self.fill_list_view()

    def fill_list_view(self):
        del self.result_data[:]
        self.result_data_listview.DeleteAllItems()
        #开始构造填充listview的数据对象
        for p in self.player_list:
            player_info = get_player_by_id(p)
            score_list_per_round = get_player_all_rounds_score_list(self.match_id, p)
            total_score = 0.0
            for i in score_list_per_round:
                if i != None:
                    total_score += i
            obj = ResultColumnData(
                player_info.id,
                player_info.name,
                get_show_score(score_list_per_round[0]),
                get_show_score(score_list_per_round[1]),
                get_show_score(score_list_per_round[2]),
                get_show_score(score_list_per_round[3]),
                get_show_score(score_list_per_round[4]),
                get_show_score(score_list_per_round[5]),
                get_show_score(total_score)
            )
            self.result_data.append(obj)
        self.result_data = sorted(self.result_data, key=lambda ResultColumnData:float(ResultColumnData.s_total))
        self.result_data.reverse()
        for obj in self.result_data:
            index = self.result_data_listview.InsertStringItem(sys.maxint, obj.name)
            self.result_data_listview.SetStringItem(index, 1, obj.s_1)
            self.result_data_listview.SetStringItem(index, 2, obj.s_2)
            self.result_data_listview.SetStringItem(index, 3, obj.s_3)
            self.result_data_listview.SetStringItem(index, 4, obj.s_4)
            self.result_data_listview.SetStringItem(index, 5, obj.s_5)
            self.result_data_listview.SetStringItem(index, 6, obj.s_6)
            self.result_data_listview.SetStringItem(index, 7, obj.s_total)

class GenApp(wx.App):
        def __init__(self, redirect=False, filename=None):
            wx.App.__init__(self, redirect, filename)

        def OnInit(self):
            # create frame here
            frame = MainFrame()
            frame.Show()
            return True

def main():
    """
    Run the demo
    """
    app = GenApp()
    app.MainLoop()

if __name__ == "__main__":
    main()