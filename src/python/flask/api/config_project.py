import json
from enum import Enum
from pathlib import Path
from typing import Literal,List

from PIL import Image
from pydantic import BaseModel, field_validator,Field

## <----------------------- CLASES DE DATOS -----------------------> ##

# -------------------PROJECT------------------- #

class ColorSelect(str,Enum):
    RedBlue:str = "0"
    Transparent:str = "1"
    Grid:str = "2"

class GlobeData(BaseModel):
    x:int|None = None
    y:int|None = None
    z:int|None = None

class ProjectData(BaseModel):
    Name:str = "world"
    layers:list[str] = [""]
    globe:GlobeData|None = None
    rotation:float|None = None
    sun_distance:int|None = None

# -------------------PROGRAM------------------- #

locations_def = Literal["ab","aa","af","ak","sq","am","ar","an","hy","as","av","ae","ay","az","bm","ba","eu","be","bn","bh","bi","bs","br","bg","my","ca","ch","ce","ny","zh","cv","kw","co","cr","hr","cs","da","dv","nl","dz","en","eo","et","ee","fo","fj","fi","fr","ff","gl","ka","de","el","gn","gu","ht","ha","he","hz","hi","ho","hu","ia","id","ie","ga","ig","ik","io","is","it","iu","ja","jv","kl","kn","kr","ks","kk","km","ki","rw","ky","kv","kg","ko","ku","kj","la","lb","lg","li","ln","lo","lt","lu","lv","gv","mk","mg","ms","ml","mt","mi","mr","mh","mn","na","nv","nb","nd","ne","ng","nn","no","ii","nr","oc","oj","cu","om","or","os","pa","pi","fa","pl","ps","pt","qu","rm","rn","ro","ru","sa","sc","sd","se","sm","sg","sr","gd","sn","si","sk","sl","so","st","es","su","sw","ss","sv","ta","te","tg","th","ti","bo","tk","tl","tn","to","tr","ts","tt","tw","ty","ug","uk","ur","uz","ve","vi","vo","wa","cy","wo","fy","xh","yi","yo","za","zu",]

class ThemeData(int,Enum):
    default:int = 0

class ProjectPath(BaseModel):
    name:str
    path:str

    @field_validator("path")
    @classmethod
    def path_validator(cls,v:str):
        path = Path(v)
        project_file = path / "project.json"
        if project_file.is_file():
            file = open_json(project_file)
            if ProjectData.model_validate(file):
                pass
            else:
                raise ValueError(f"archivo no valido {path}")
        else:
            raise ValueError(f"el archivo no existe {path}")

class ConfigData(BaseModel):
    lang:List[locations_def] = Field(default="es")
    theme:ThemeData = Field(default=ThemeData.default)
    projects:List[ProjectPath]

## <-------------------------- CLASE API --------------------------> ##

class Project:
    def __init__(self):
        self.conf_path = "src/data/config.json"
        self.conf_data:ConfigData = None#ConfigData.model_validate(open_json(self.conf_path))

    def get_config(self):
        return open_json(self.conf_path)

    def save_config(self,conf):
        data = ConfigData.model_validate(conf)
        save_json(self.conf_path,data.model_dump())

 
    def load_project(self,path):
        path = Path(path[0])
        list_file = [f.name for f in path.iterdir()]
        return list_file
    
    def get_projects(self):
        projects = self.conf_data.projects
        data = []
        for project in projects:
            data.append(project.name)
        return data

    def new_project(self,data):
        path = Path(data["folder_label"])
        path.mkdir()
        # CREAR LAYERS
        self.new_layer(data)
        
        # CREAR CONFIGURACION
        project = ProjectData.model_validate(data["project"])
        save_json(path,project.model_dump())
    
    def new_layer(self,data):
        # CREAR LAS CARPETAS
        path:Path = Path(data["folder_label"]) / "layers" / data["name"] / "0"
        path.mkdir(parents=True,exist_ok=True)
        path_0 = path / "0"
        path_0.mkdir(parents=True,exist_ok=True)
        path_1 = path / "1"
        path_1.mkdir(parents=True,exist_ok=True)
        # CREAR LAS IAMGENES
        img_0:Image = make_image(data["size"],data["color"])
        img_1:Image = make_image(data["size"],data["color"])
        # GUARDAR LAS IMAGENES
        img0 = path_0 / "0.png"
        img1 = path_1 / "0.png"
        img_0.save(img0)
        img_1.save(img1)


def make_image(size,color) -> Image:
    size = (int(size),int(size))
    color = ColorSelect(color)
    img = Image.new(size=size,color=color)
    return img

def open_json(ruta: str):
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None
    except Exception as e:
        return None

def save_json(path,datos, indent: int = 4):
    try:
        # Crear la carpeta si no existe
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=indent)
        
        print(f" Archivo guardado correctamente en: {path}")
    except Exception as e:
        print(f" Error al guardar el JSON: {e}")
