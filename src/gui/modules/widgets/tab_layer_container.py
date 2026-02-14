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
## Class TabLayer
###########################################################################

class TabLayer ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
        self.m_scrolledWindow1.SetScrollRate( 5, 5 )
        bSizer6.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

        m_choice1Choices = [ _(u"Capa Tierra"), _(u"Capa Mapa Imagen"), _(u"Capa Mapa Imagen Altura"), wx.EmptyString, wx.EmptyString ]
        self.m_choice1 = wx.Choice( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
        self.m_choice1.SetSelection( 0 )
        bSizer7.Add( self.m_choice1, 0, wx.ALL, 5 )

        self.button_add = wx.Button( self.m_panel5, wx.ID_ANY, _(u"añadir"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.button_add, 0, wx.ALL, 5 )

        self.button_edit = wx.Button( self.m_panel5, wx.ID_ANY, _(u"editar"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.button_edit, 0, wx.ALL, 5 )

        self.buton_delete = wx.Button( self.m_panel5, wx.ID_ANY, _(u"eliminar"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.buton_delete, 0, wx.ALL, 5 )


        self.m_panel5.SetSizer( bSizer7 )
        self.m_panel5.Layout()
        bSizer7.Fit( self.m_panel5 )
        bSizer6.Add( self.m_panel5, 0, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer6 )
        self.Layout()

        # Connect Events
        self.button_add.Bind( wx.EVT_BUTTON, self.button_add_OnButtonClick )
        self.button_edit.Bind( wx.EVT_BUTTON, self.button_edit_OnButtonClick )
        self.buton_delete.Bind( wx.EVT_BUTTON, self.buton_delete_OnButtonClick )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def button_add_OnButtonClick( self, event ):
        event.Skip()

    def button_edit_OnButtonClick( self, event ):
        event.Skip()

    def buton_delete_OnButtonClick( self, event ):
        event.Skip()


