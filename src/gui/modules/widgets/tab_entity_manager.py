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
## Class EntityManager
###########################################################################

class EntityManager ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        self.tree_entity = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
        bSizer9.Add( self.tree_entity, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

        self.button_new = wx.Button( self.m_panel7, wx.ID_ANY, _(u"añadir"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.button_new, 0, wx.ALL, 5 )

        self.m_staticline1 = wx.StaticLine( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
        bSizer10.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText3 = wx.StaticText( self.m_panel7, wx.ID_ANY, _(u"entidad:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        bSizer10.Add( self.m_staticText3, 0, wx.ALL, 5 )

        self.labelEntity_selected = wx.StaticText( self.m_panel7, wx.ID_ANY, _(u"entitySelected"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.labelEntity_selected.Wrap( -1 )

        bSizer10.Add( self.labelEntity_selected, 0, wx.ALL, 5 )

        self.button_edit = wx.Button( self.m_panel7, wx.ID_ANY, _(u"editar"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.button_edit, 0, wx.ALL, 5 )


        self.m_panel7.SetSizer( bSizer10 )
        self.m_panel7.Layout()
        bSizer10.Fit( self.m_panel7 )
        bSizer9.Add( self.m_panel7, 0, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer9 )
        self.Layout()

        # Connect Events
        self.tree_entity.Bind( wx.EVT_TREE_ITEM_ACTIVATED, self.tree_entity_OnTreeItemActived )
        self.tree_entity.Bind( wx.EVT_TREE_ITEM_RIGHT_CLICK, self.tree_entity_OnTreeItemRightClick )
        self.button_new.Bind( wx.EVT_BUTTON, self.button_new_OnButtonClick )
        self.button_edit.Bind( wx.EVT_BUTTON, self.button_edit_OnButtonClick )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def tree_entity_OnTreeItemActived( self, event ):
        event.Skip()

    def tree_entity_OnTreeItemRightClick( self, event ):
        event.Skip()

    def button_new_OnButtonClick( self, event ):
        event.Skip()

    def button_edit_OnButtonClick( self, event ):
        event.Skip()


