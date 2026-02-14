# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class WindowsEntityContainer
###########################################################################

class WindowsEntityContainer ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_panel1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_notebook1.AddPage( self.m_panel1, _(u"entidades"), True )
        self.m_panel2 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_notebook1.AddPage( self.m_panel2, _(u"capas"), False )
        self.m_panel3 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )


        self.m_panel3.SetSizer( bSizer2 )
        self.m_panel3.Layout()
        bSizer2.Fit( self.m_panel3 )
        self.m_notebook1.AddPage( self.m_panel3, _(u"Herramientas"), False )

        bSizer3.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer3 )
        self.Layout()

        # Connect Events
        self.m_notebook1.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnNoteBookPageChanged )
        self.m_notebook1.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGING, self.OnNoteBookPageChangin )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnNoteBookPageChanged( self, event ):
        event.Skip()

    def OnNoteBookPageChangin( self, event ):
        event.Skip()


