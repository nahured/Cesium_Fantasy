import threading

import wx

from src.gui.build_ui.main import Windows
from src.server.app import run_server

# >------------ LOAD MANAGERS ------------<
import src.utils_py.managers

def star_windows():
    app = wx.App()
    app.DATA_BASE = {
        "cliend" : {
            "config":"NONE"
        }
    }
    windows = Windows(None)
    windows.Show()

    flask_thread = threading.Thread(
        target=run_server,
        daemon=True
    )
    flask_thread.start()

    app.MainLoop()