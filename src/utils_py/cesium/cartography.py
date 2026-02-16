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
    
    def get_tile_count(self,level) -> list[int,int]:
        x = 2**(level+1)
        y = 2**(level)
        return x,y
    
    def get_tile_dvision(self,level) -> list[float,float]:
        l_x,l_y = self.get_tile_count(level)
        x = float(360/l_x)
        y = float(180/l_y)
        return x,y

    def from_degrres(self,longitude,latitude,level):
        l_x,l_y = self.get_tile_count(level)

        long = longitude + 180
        lat = latitude -90

        x = np.floor(abs((long*l_x)/360))
        y = np.floor(abs((lat*l_y)/180))

        return TileCoord(x,y)
    
    def to_degrees(self,level) -> "Degrees":
        d_x,d_y = self.get_tile_dvision(level)

        

class Degrees:
    def __init__(self,longitude:float,latitude:float):
        self.longitude:float = longitude
        self.latitude:float = latitude
    
    def zero(self):
        return Degrees(0.0,0.0)


class Rect:
    def __init__(self,point_1 = Degrees().zero(),point_2 = Degrees().zero()):
        self.point_1:Degrees = point_1
        self.point_2:Degrees = point_2
    
    def from_tile(self,tile_1:TileCoord,tile_2:TileCoord):
        pass