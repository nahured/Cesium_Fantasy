import wx

from src.gui.modules.main import Windows


def star_windows():
    app = wx.App()
    windows = Windows(None)
    windows.Show()

    app.MainLoop()