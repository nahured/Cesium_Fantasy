import inspect
import json
import sys
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec

#region declaration
class ResourceManager:
    """clase generica para manejar recursos"""

    def save(self,path:Path | None):
        self.resource_path = str(Path(inspect.getfile(self.__class__)).relative_to(Path.cwd()))
        self.class_name = self.__class__.__name__
        data = self.__dict__
        for key in data:
            if isinstance(data[key],ResourceManager):
                data[key] = data[key].save(None)
        if path == None:
            return data
        else:
            ResourceManager.save_resource(path,data)

    @staticmethod
    def open_resource(path:Path):
        with open(path,'r',encoding='utf-8') as file:
            data:dict = json.load(file)
        
        if "resource_path" in data.keys(): 
            obj = ResourceManager.get_class(data)        
            return obj
        else:
            return data
    
    @staticmethod
    def save_resource(path:Path,data:dict):
        with open(path,"w",encoding="utf-8") as archivo:
            json.dump(data, archivo, indent=4, ensure_ascii=False)
    
    @staticmethod
    def get_class(data:dict):
            spec = spec_from_file_location(data["class_name"],Path(data["resource_path"]).resolve()) #WARNING este puede ser un posible punto para poder ejecutar codigo malisioso cambiar por un diccionario 
            module = module_from_spec(spec)
            sys.modules[data["class_name"]] = module
            spec.loader.exec_module(module)
            new_class = getattr(module, data["class_name"])
            obj = ResourceManager.build_resource(new_class,data)
            return obj
            
    
    @staticmethod
    def build_resource(new_class:object,data:dict):
        data.pop('resource_path')
        data.pop('class_name')
        for key in data:
            if isinstance(data[key],dict) and "resource_path" in data[key].keys():
                data[key] = ResourceManager.get_class(data[key]) 
        obj = new_class(**data)
        return obj


class ConfigurationResource(ResourceManager):
    def __init__(self,lang:str):
        self.lang:str = lang

#endregion declaration

