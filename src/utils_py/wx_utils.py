import wx
import wx.svg


def svg_to_bitmap(svg_path: str, size: tuple[int, int],scale:float=1):
    svg:wx.svg.SVGimage = wx.svg.SVGimage.CreateFromFile(svg_path)
    # Opción A - la más estable en la mayoría de versiones
    bmp = svg.ConvertToBitmap(0,0,width=size[0], height=size[1],scale=scale)
    
    # Opción B - más explícita (a veces evita el bug en Windows)
    # bmp = svg.ConvertToBitmap(scale=1.0, width=size[0], height=size[1])
    
    return bmp
