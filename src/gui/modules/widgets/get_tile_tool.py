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
## Class GetTileTool
###########################################################################

class GetTileTool ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,400 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        self.Label_title = wx.StaticText( self, wx.ID_ANY, _(u"Herramienta para Generar Tiles"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.Label_title.Wrap( -1 )

        self.Label_title.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer4.Add( self.Label_title, 0, wx.EXPAND, 5 )

        m_listBox2Choices = []
        self.m_listBox2 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox2Choices, wx.LB_HSCROLL|wx.LB_MULTIPLE|wx.LB_SINGLE )
        bSizer4.Add( self.m_listBox2, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer4.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

        bSizer41 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, _(u"zoom L"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        bSizer41.Add( self.m_staticText1, 0, wx.ALL, 5 )

        self.m_spinCtrl5 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
        bSizer41.Add( self.m_spinCtrl5, 1, wx.ALL, 5 )


        bSizer4.Add( bSizer41, 0, wx.EXPAND, 5 )

        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.label_point_1_x = wx.StaticText( self, wx.ID_ANY, _(u"X:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_point_1_x.Wrap( -1 )

        bSizer5.Add( self.label_point_1_x, 0, wx.ALL, 5 )

        self.spin_point_1_x = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
        bSizer5.Add( self.spin_point_1_x, 1, wx.ALL, 5 )

        self.label_point_1_y = wx.StaticText( self, wx.ID_ANY, _(u"Y:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_point_1_y.Wrap( -1 )

        bSizer5.Add( self.label_point_1_y, 0, wx.ALL, 5 )

        self.spin_point_1_y = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
        bSizer5.Add( self.spin_point_1_y, 1, wx.ALL, 5 )

        self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
        bSizer5.Add( self.m_staticline2, 0, wx.ALL|wx.EXPAND, 5 )

        self.button_pick_point_1 = wx.Button( self, wx.ID_ANY, _(u"seleccionar punto 1"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.button_pick_point_1, 0, wx.ALL, 5 )


        bSizer4.Add( bSizer5, 0, wx.EXPAND, 5 )

        bSizer51 = wx.BoxSizer( wx.HORIZONTAL )

        self.label_point_2_x = wx.StaticText( self, wx.ID_ANY, _(u"X:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_point_2_x.Wrap( -1 )

        bSizer51.Add( self.label_point_2_x, 0, wx.ALL, 5 )

        self.spin_point_2_x = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
        bSizer51.Add( self.spin_point_2_x, 1, wx.ALL, 5 )

        self.label_point_2_y = wx.StaticText( self, wx.ID_ANY, _(u"Y:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_point_2_y.Wrap( -1 )

        bSizer51.Add( self.label_point_2_y, 0, wx.ALL, 5 )

        self.spin_point_2_y = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
        bSizer51.Add( self.spin_point_2_y, 1, wx.ALL, 5 )

        self.m_staticline21 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
        bSizer51.Add( self.m_staticline21, 0, wx.ALL|wx.EXPAND, 5 )

        self.button_pick_point_2 = wx.Button( self, wx.ID_ANY, _(u"seleccionar punto 2"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer51.Add( self.button_pick_point_2, 0, wx.ALL, 5 )


        bSizer4.Add( bSizer51, 0, wx.EXPAND, 5 )

        self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer4.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

        self.button_generate_collage = wx.Button( self, wx.ID_ANY, _(u"crear Imagen"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.button_generate_collage, 0, wx.ALL|wx.EXPAND, 5 )

        bSizer52 = wx.BoxSizer( wx.HORIZONTAL )

        self.Drop_file = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
        bSizer52.Add( self.Drop_file, 0, 0, 5 )

        self.file_picker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, _(u"seleccionar archivo ctile"), _(u"*.ctile*"), wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        bSizer52.Add( self.file_picker, 0, wx.ALL, 5 )


        bSizer4.Add( bSizer52, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizer4 )
        self.Layout()

        # Connect Events
        self.spin_point_1_x.Bind( wx.EVT_SPINCTRL, self.spin_point_1_x_OnSpinCtrl )
        self.spin_point_1_x.Bind( wx.EVT_TEXT, self.spin_point_1_x_OnSpinCtrlText )
        self.spin_point_1_x.Bind( wx.EVT_TEXT_ENTER, self.spin_point_2_x_OnTextEnter )
        self.spin_point_1_y.Bind( wx.EVT_SPINCTRL, self.spin_point_1_y_OnSpinCtrl )
        self.spin_point_1_y.Bind( wx.EVT_TEXT, self.spin_point_1_y_OnSpinCtrlText )
        self.spin_point_1_y.Bind( wx.EVT_TEXT_ENTER, self.spin_point_1_y_OnTextEnter )
        self.button_pick_point_1.Bind( wx.EVT_BUTTON, self.button_pick_point_1_OnButtonClick )
        self.spin_point_2_x.Bind( wx.EVT_SPINCTRL, self.spin_point_2_x_OnSpinCtrl )
        self.spin_point_2_x.Bind( wx.EVT_TEXT, self.spin_point_2_x_OnSpinCtrlText )
        self.spin_point_2_x.Bind( wx.EVT_TEXT_ENTER, self.spin_point_2_x_OnTextEnter )
        self.spin_point_2_y.Bind( wx.EVT_SPINCTRL, self.spin_point_2_y_OnSpinCtrl )
        self.spin_point_2_y.Bind( wx.EVT_TEXT, self.spin_point_2_y_OnSpinCtrlText )
        self.spin_point_2_y.Bind( wx.EVT_TEXT_ENTER, self.spin_point_2_y_OnTextEnter )
        self.button_pick_point_2.Bind( wx.EVT_BUTTON, self.button_pick_point_2_OnButtonClick )
        self.button_generate_collage.Bind( wx.EVT_BUTTON, self.button_generate_collage_OnButtonClick )
        self.file_picker.Bind( wx.EVT_FILEPICKER_CHANGED, self.file_picker_OnFileChanged )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def spin_point_1_x_OnSpinCtrl( self, event ):
        event.Skip()

    def spin_point_1_x_OnSpinCtrlText( self, event ):
        event.Skip()

    def spin_point_2_x_OnTextEnter( self, event ):
        event.Skip()

    def spin_point_1_y_OnSpinCtrl( self, event ):
        event.Skip()

    def spin_point_1_y_OnSpinCtrlText( self, event ):
        event.Skip()

    def spin_point_1_y_OnTextEnter( self, event ):
        event.Skip()

    def button_pick_point_1_OnButtonClick( self, event ):
        event.Skip()

    def spin_point_2_x_OnSpinCtrl( self, event ):
        event.Skip()

    def spin_point_2_x_OnSpinCtrlText( self, event ):
        event.Skip()


    def spin_point_2_y_OnSpinCtrl( self, event ):
        event.Skip()

    def spin_point_2_y_OnSpinCtrlText( self, event ):
        event.Skip()

    def spin_point_2_y_OnTextEnter( self, event ):
        event.Skip()

    def button_pick_point_2_OnButtonClick( self, event ):
        event.Skip()

    def button_generate_collage_OnButtonClick( self, event ):
        event.Skip()

    def file_picker_OnFileChanged( self, event ):
        event.Skip()


