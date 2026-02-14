import wx
import src.gui.modules.widgets.get_tile_tool as get_tile_tool
import src.utils_py.wx_utils as wx_utils

class GetTileTool(get_tile_tool.GetTileTool):
    def __init__(self, parent):
        super().__init__(parent)
        
        # >----------- ASIGNAMOS EL ICONO DE DROP_FILE -----------<
        self.Drop_file.SetBitmap(wx_utils.svg_to_bitmap("src/gui/resources/icons/drop_file_icon.svg",(300,300)))
        self.Drop_file.SetSize(100,100)

        self.set_max_spin_value()
    
    def spin_level_OnSpinCtrl(self, event):
        self.set_max_spin_value()
        return super().spin_level_OnSpinCtrl(event)
    
    def Drop_file_OnDropFile(self, event:wx.DropFilesEvent):
        """
        esta funcion optiene la ruta del archivo que se dropeo
        """
        print(event.GetFiles())
    
    def set_max_spin_value(self):
        """
        esta funcion delimitara el tamaño maximo de la grid por el nivel de zoom seleccionado, para impedir que nos salgamos de la grid
        """
        x_max = 2**(self.spin_level.Value+1)
        y_max = 2**self.spin_level.Value
        self.spin_point_1_x.Max = x_max
        self.spin_point_1_y.Max = y_max
        self.spin_point_2_x.Max = x_max
        self.spin_point_2_y.Max = y_max