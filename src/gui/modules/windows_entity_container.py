# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from src.gui.modules.widgets.get_tile_tool import GetTileTool

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
        self.tab_entity = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        self.tree_entity = wx.TreeCtrl( self.tab_entity, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
        bSizer4.Add( self.tree_entity, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_panel5 = wx.Panel( self.tab_entity, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText1 = wx.StaticText( self.m_panel5, wx.ID_ANY, _(u"entidad"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        bSizer6.Add( self.m_staticText1, 0, wx.ALL, 5 )

        self.entity_selected_name = wx.StaticText( self.m_panel5, wx.ID_ANY, _(u"temp_item"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.entity_selected_name.Wrap( -1 )

        bSizer6.Add( self.entity_selected_name, 0, wx.ALL, 5 )

        self.button_entity_edit = wx.Button( self.m_panel5, wx.ID_ANY, _(u"editar"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.button_entity_edit, 0, wx.ALL, 5 )


        self.m_panel5.SetSizer( bSizer6 )
        self.m_panel5.Layout()
        bSizer6.Fit( self.m_panel5 )
        bSizer4.Add( self.m_panel5, 0, wx.EXPAND |wx.ALL, 5 )


        self.tab_entity.SetSizer( bSizer4 )
        self.tab_entity.Layout()
        bSizer4.Fit( self.tab_entity )
        self.m_notebook1.AddPage( self.tab_entity, _(u"entidades"), True )
        self.tab_layer = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer7 = wx.BoxSizer( wx.VERTICAL )

        self.m_scrolledWindow1 = wx.ScrolledWindow( self.tab_layer, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
        self.m_scrolledWindow1.SetScrollRate( 5, 5 )
        bSizer7.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel6 = wx.Panel( self.tab_layer, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer8 = wx.BoxSizer( wx.VERTICAL )


        self.m_panel6.SetSizer( bSizer8 )
        self.m_panel6.Layout()
        bSizer8.Fit( self.m_panel6 )
        bSizer7.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )


        self.tab_layer.SetSizer( bSizer7 )
        self.tab_layer.Layout()
        bSizer7.Fit( self.tab_layer )
        self.m_notebook1.AddPage( self.tab_layer, _(u"capas"), False )
        self.tab_tool = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.panel_get_tiles = wx.Panel( self.tab_tool, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer31 = wx.BoxSizer( wx.VERTICAL )

        self.Get_tile_tool = GetTileTool(self.panel_get_tiles)
        bSizer31.Add( self.Get_tile_tool, 1, wx.ALL|wx.EXPAND, 5 )


        self.panel_get_tiles.SetSizer( bSizer31 )
        self.panel_get_tiles.Layout()
        bSizer31.Fit( self.panel_get_tiles )
        bSizer2.Add( self.panel_get_tiles, 1, wx.EXPAND |wx.ALL, 5 )


        self.tab_tool.SetSizer( bSizer2 )
        self.tab_tool.Layout()
        bSizer2.Fit( self.tab_tool )
        self.m_notebook1.AddPage( self.tab_tool, _(u"Herramientas"), False )

        bSizer3.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer3 )
        self.Layout()

        # Connect Events
        self.m_notebook1.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnNoteBookPageChanged )
        self.m_notebook1.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGING, self.OnNoteBookPageChangin )
        self.tree_entity.Bind( wx.EVT_TREE_GET_INFO, self.tree_entity_OnTreeGetInfo )
        self.tree_entity.Bind( wx.EVT_TREE_ITEM_ACTIVATED, self.tree_entity_OnItemActived )
        self.tree_entity.Bind( wx.EVT_TREE_ITEM_GETTOOLTIP, self.tree_entity_OnTreeItemGetToolTip )
        self.tree_entity.Bind( wx.EVT_TREE_ITEM_RIGHT_CLICK, self.tree_entity_OnTreeItemRigthClick )
        self.tree_entity.Bind( wx.EVT_TREE_SET_INFO, self.tree_entity_onTreeSetInfo )
        self.tree_entity.Bind( wx.EVT_TREE_STATE_IMAGE_CLICK, self.tree_entity_OnTreeStateImageClick )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnNoteBookPageChanged( self, event ):
        event.Skip()

    def OnNoteBookPageChangin( self, event ):
        event.Skip()

    def tree_entity_OnTreeGetInfo( self, event ):
        event.Skip()

    def tree_entity_OnItemActived( self, event ):
        event.Skip()

    def tree_entity_OnTreeItemGetToolTip( self, event ):
        event.Skip()

    def tree_entity_OnTreeItemRigthClick( self, event ):
        event.Skip()

    def tree_entity_onTreeSetInfo( self, event ):
        event.Skip()

    def tree_entity_OnTreeStateImageClick( self, event ):
        event.Skip()


