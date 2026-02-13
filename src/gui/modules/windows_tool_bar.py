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
## Class ToolBar
###########################################################################

class ToolBar ( wx.ToolBar ):

    def __init__( self, parent ):
        wx.ToolBar.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.TB_HORIZONTAL )

        m_choice1Choices = [ _(u"Nuevo"), _(u"Abrir"), _(u"Eliminar"), _(u"Administrar") ]
        self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
        self.m_choice1.SetSelection( 0 )
        self.AddControl( self.m_choice1 )
        m_choice2Choices = []
        self.m_choice2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
        self.m_choice2.SetSelection( 0 )
        self.AddControl( self.m_choice2 )

        self.Realize()

    def __del__( self ):
        pass


