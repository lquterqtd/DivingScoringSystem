__author__ = 'Administrator'
#coding:utf-8
import wx
from controller import get_all_referees, get_all_players
from ObjectListView import ObjectListView, ColumnDefn

class RefereesColumnData(object):
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

class AddMatchDialog(wx.Dialog):
    def __init__(self, main_panel):
        wx.Dialog.__init__(self, None, -1, u"创建一场新的比赛", size=(800, 600))
        self.main_panel = main_panel

        self.referees_data = []
        for i in get_all_referees():
            self.referees_data.append(RefereesColumnData(i.name, i.get_sex(), i.age))
        self.resultsOlv = ObjectListView(self, style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.setResults()

        box = wx.StaticBox(wx.Panel(self), -1, u"123")
        sizer = wx.StaticBoxSizer(box, wx.VERTICAL)
        sizer.Add(self.resultsOlv, 0, wx.ALL, 2)
        ms = wx.BoxSizer(wx.HORIZONTAL)
        ms.Add(sizer, 0, wx.ALL, 10)
        wx.Panel(self).SetSizer(ms)
    def setResults(self):
        """"""
        self.resultsOlv.SetColumns(
            [
                ColumnDefn(u"姓名", 'centre', 200, "name"),
            ]
        )
        self.resultsOlv.CreateCheckStateColumn()
        self.resultsOlv.SetObjects(self.referees_data)
