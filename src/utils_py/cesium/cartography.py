import numpy as np



#
#
#
#
#
#
#
#


class TileCoord:
    def __init__(self,x:int=0,y:int=0):
        self.x:int = x
        self.y:int = y
        self.invert_y:bool = True
    
    def get_tile_count(self,level) -> list[int,int]:
        """
        retorna la cantidad de tiles por nivel
        """
        x = 2**(level+1)
        y = 2**(level)
        return x,y
    
    def get_tile_dvision(self,level) -> list[float,float]:
        """
        retorna la division de cuanto grados mide un tile
        """
        l_x,l_y = self.get_tile_count(level)
        x = float(360/l_x)
        y = float(180/l_y)
        return x,y

    def from_degrres(self,degrees:"Degrees",level) -> "TileCoord":
        """
        esta funcion te devuelve un TileCoord a partir de un Degrees
        """
        l_x,l_y = self.get_tile_count(level)
        long = degrees.longitude + 180
        if self.invert_y:
            lat = degrees.latitude -90
        else:
            lat = degrees.latitude +90


        x = np.floor(abs((long*l_x)/360))
        y = np.floor(abs((lat*l_y)/180))

        return TileCoord(x,y)
    
    def to_degrees(self,h:float,v:float,level) -> "Degrees":
        """
        esta funcion te devuelve un Degrees a partir del tileCoord
        """
        d_x,d_y = self.get_tile_dvision(level)
        x = float((self.x+h)*d_x-180)
        if self.invert_y:
            y = float((self.y+v)*d_y+90)
        else:
            y = float((self.y+v)*d_y-90)
        
        return Degrees(x,y)

        

class Degrees:
    def __init__(self,longitude:float,latitude:float):
        self.longitude:float = longitude
        self.latitude:float = latitude
    
    def zero(self) -> "Degrees":
        return Degrees(0.0,0.0)
    
    def from_tile_coord(self,tile:"TileCoord",h:float=0.0,v:float=0.0) -> "TileCoord":
        """
        trucazo
        """
        return tile.to_degrees(h,v)


class Rect:
    def __init__(self,point_1:Degrees = Degrees().zero(),point_2:Degrees = Degrees().zero()):
        self.point_1:Degrees = point_1
        self.point_2:Degrees = point_2
    
    def from_tile(self,tile_1:"TileCoord",tile_2:"TileCoord") -> "Rect":
        point_1 = tile_1.to_degrees()
        point_2 = tile_1.to_degrees(1,1)
        return Rect(point_1,point_2)
    
    def get_rect(self) -> dict:
        rect = {
        "Oeste" : self.point_1.latitude,
        "Este" : self.point_2.latitude,
        "Norte" : self.point_2.longitude,
        "Sur" : self.point_1.longitude
        }
        return rect
