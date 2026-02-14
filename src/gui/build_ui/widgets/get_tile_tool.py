import wx
import src.gui.modules.widgets.get_tile_tool as get_tile_tool
import src.utils_py.wx_utils as wx_utils

class GetTileTool(get_tile_tool.GetTileTool):
    def __init__(self, parent):
        super().__init__(parent)
        self.Drop_file.SetBitmap(wx_utils.svg_to_bitmap("src/gui/resources/icons/drop_file_icon.svg",(300,300)))
        self.Drop_file.SetSize(100,100)
        #self.Drop_file.Refresh()