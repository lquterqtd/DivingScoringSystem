__author__ = 'Administrator'
#coding:utf-8
import wx
from mydialog import AddMatchDialog


class MainPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, id=wx.ID_ANY,
                          title=u"跳水打分系统", size=(800,600))
        panel = MainPanel(self)
        self.icon = wx.Icon('diving.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
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
    def OnNewMatch(self, event):
        #wx.MessageBox(u"开始一场新的比赛")
        dlg = AddMatchDialog(self)
        dlg.ShowModal()
        dlg.Destroy()

    def OnOpenMatch(self, event):
        wx.MessageBox(u"打开已有的比赛")

    def OnAbout(self, event):
        wx.MessageBox(u"这是一个跳水打分系统的Demo版本")

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