# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (adapted style)
## http://www.wxformbuilder.org/
##
## Custom WebView widget that inherits from wx.html2.WebView
## PLEASE DO *NOT* EDIT THIS FILE DIRECTLY IF GENERATED!
###########################################################################

import wx
import wx.html2

###########################################################################
## Class CustomWebView
###########################################################################

class WebView():

    def __init__(self,parent):
        self.browser = wx.html2.WebView.New(parent)
        self.url = "https://www.google.com"
        self.browser.LoadURL(self.url)