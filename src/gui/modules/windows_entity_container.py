# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from  src.gui.build_ui.widgets.tab_entity_manager import EntityManager
from src.gui.build_ui.widgets.tab_layer_container import TabLayer
from src.gui.build_ui.widgets.get_tile_tool import GetTileTool

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

        self.TabEntity = EntityManager(self.tab_entity)
        bSizer4.Add( self.TabEntity, 1, wx.ALL|wx.EXPAND, 5 )


        self.tab_entity.SetSizer( bSizer4 )
        self.tab_entity.Layout()
        bSizer4.Fit( self.tab_entity )
        self.m_notebook1.AddPage( self.tab_entity, _(u"entidades"), True )
        self.tab_layer = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer7 = wx.BoxSizer( wx.VERTICAL )

        self.tab_layer_container = TabLayer(self.tab_layer)
        bSizer7.Add( self.tab_layer_container, 1, wx.ALL|wx.EXPAND, 5 )


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

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnNoteBookPageChanged( self, event ):
        event.Skip()

    def OnNoteBookPageChangin( self, event ):
        event.Skip()


