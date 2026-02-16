import wx
from pubsub import pub
import wx.html2
import numpy as np

import src.gui.modules.widgets.get_tile_tool as get_tile_tool
import src.utils_py.wx_utils as wx_utils

class GetTileTool(get_tile_tool.GetTileTool):
    def __init__(self, parent):
        super().__init__(parent)
        
        # >----------- ASIGNAMOS EL ICONO DE DROP_FILE -----------<
        self.Drop_file.SetBitmap(wx_utils.svg_to_bitmap("src/gui/resources/icons/drop_file_icon.svg",(300,300)))
        self.Drop_file.SetSize(100,100)

        self.point_selected = 0
        self.set_max_spin_value()
        pub.subscribe(self.ready,'ui-finish')
    
    def ready(self):
        self.browser:wx.html2.WebView = wx.GetApp().web_browser
        pub.unsubscribe(self.ready,'ui-finish')

    def spin_level_OnSpinCtrl(self, event):
        self.set_max_spin_value()
        return super().spin_level_OnSpinCtrl(event)
    
    def Drop_file_OnDropFile(self, event:wx.DropFilesEvent):
        """
        esta funcion optiene la ruta del archivo que se dropeo
        """
        print(event.GetFiles())
    
    def degrees_to_tile(self,data):
        degrees = data['data']['degrees']
        p_x = (360)/2**(self.spin_level.GetValue()+1)
        p_y = 180/2**self.spin_level.GetValue()
        # ya que las coordenadas del planeta no van de x:0->360 y:0->180 sino que x:-180->180 y:-90->90
        # se tiene que ajustar el desface creado
        x = int(np.floor(abs((degrees['longitude']+180) / p_x)))
        y = int(np.floor(abs((degrees['latitude']-90) / p_y)))
        if self.point_selected == 1:
            self.set_point_1_value([x,y])
        elif self.point_selected == 2:
            self.set_point_2_value([x,y])
        self.point_selected = 0 
 
        pub.unsubscribe(self.degrees_to_tile,'mouse_click_signal')

    # >------------- seteamos nuevos valores -------------< #
    def set_point_1_value(self,vector_new_value):
        self.set_spin_point_1_x_value(vector_new_value[0])
        self.set_spin_point_1_y_value(vector_new_value[1])
    
    def set_point_2_value(self,vector_new_value):
        self.set_spin_point_2_x_value(vector_new_value[0])
        self.set_spin_point_2_y_value(vector_new_value[1])
    
    def set_spin_point_1_x_value(self,new_value):
        self.spin_point_1_x.SetValue(new_value)

    def set_spin_point_1_y_value(self,new_value):
        self.spin_point_1_y.SetValue(new_value)

    def set_spin_point_2_x_value(self,new_value):
        self.spin_point_2_x.SetValue(new_value)

    def set_spin_point_2_y_value(self,new_value):
        self.spin_point_2_y.SetValue(new_value)

    
    def set_max_spin_value(self):
        """
        esta funcion delimitara el tamaño maximo de la grid por el nivel de zoom seleccionado, para impedir que nos salgamos de la grid
        """
        x_max = (2**(self.spin_level.Value+1))-1
        y_max = (2**self.spin_level.Value)-1
        self.spin_point_1_x.Max = x_max
        self.spin_point_1_y.Max = y_max
        self.spin_point_2_x.Max = x_max
        self.spin_point_2_y.Max = y_max
    
    def button_generate_collage_OnButtonClick(self,event):
        print("get iamge")
        img = {
            "mode":"simple",
            "point_1": [self.spin_point_1_x.GetValue(),self.spin_point_1_y.GetValue()],
            "point_2": [self.spin_point_2_x.GetValue(),self.spin_point_2_y.GetValue()]
        }
        
        pub.sendMessage("generate_image",img=img)
    
    def button_pick_point_1_OnButtonClick(self,event):
        self.point_selected = 1
        pub.subscribe(self.degrees_to_tile,'mouse_click_signal')
        self.browser.RunScript('get_mouse_world_location()')
    
    def button_pick_point_2_OnButtonClick(self,event):
        self.point_selected = 2
        pub.subscribe(self.degrees_to_tile,'mouse_click_signal')
        self.browser.RunScript('get_mouse_world_location()')