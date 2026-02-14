# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from src.gui.build_ui.windows_tool_bar import ToolBar
from src.gui.build_ui.windows_entity_container import WindowsEntityContainer
from src.gui.build_ui.windows_web_view import WebView

import gettext
_ = gettext.gettext

###########################################################################
## Class Windows
###########################################################################

class Windows ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Cesium Fantasy"), pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        Base_Vbox = wx.BoxSizer( wx.VERTICAL )

        self.windows_tool_bar = ToolBar(self)
        Base_Vbox.Add( self.windows_tool_bar, 0, wx.ALL|wx.EXPAND, 2 )

        base_HBox = wx.BoxSizer( wx.HORIZONTAL )

        self.windows_entity_container = WindowsEntityContainer(self)
        base_HBox.Add( self.windows_entity_container, 0, wx.ALL|wx.EXPAND, 2 )

        self.windows_web_view = WebView(self)
        base_HBox.Add( self.windows_web_view.browser, 1, wx.EXPAND, 2 )


        Base_Vbox.Add( base_HBox, 1, wx.EXPAND, 5 )


        self.SetSizer( Base_Vbox )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_ACTIVATE, self.OnActive )
        self.Bind( wx.EVT_ACTIVATE_APP, self.OnActiveApp )
        self.Bind( wx.EVT_CLOSE, self.OnClose )
        self.Bind( wx.EVT_HIBERNATE, self.OnHibernate )
        self.Bind( wx.EVT_ICONIZE, self.OnIconize )
        self.Bind( wx.EVT_IDLE, self.OnIdle )
        self.Bind( wx.EVT_MAXIMIZE, self.OnMaximize )
        self.Bind( wx.EVT_SHOW, self.OnShow )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnActive( self, event ):
        event.Skip()

    def OnActiveApp( self, event ):
        event.Skip()

    def OnClose( self, event ):
        event.Skip()

    def OnHibernate( self, event ):
        event.Skip()

    def OnIconize( self, event ):
        event.Skip()

    def OnIdle( self, event ):
        event.Skip()

    def OnMaximize( self, event ):
        event.Skip()

    def OnShow( self, event ):
        event.Skip()


