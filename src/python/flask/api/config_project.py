import json
from pathlib import Path

class Project:
    conf_path = "src/data/config.json"

    def get_config(self):
        return self.leer_json(self.conf_path)

    def save_config(self,conf):
        self.guardar_json(conf)

    def leer_json(self,ruta: str):
        try:
            with open(ruta, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            return None
        except json.JSONDecodeError:
            return None
        except Exception as e:
            return None
    
    def guardar_json(self,datos, indent: int = 4):
        try:
            # Crear la carpeta si no existe
            Path(self.conf_path).parent.mkdir(parents=True, exist_ok=True)
            
            with open(self.conf_path, 'w', encoding='utf-8') as archivo:
                json.dump(datos, archivo, ensure_ascii=False, indent=indent)
            
            print(f" Archivo guardado correctamente en: {self.conf_path}")
        except Exception as e:
            print(f" Error al guardar el JSON: {e}")
    
    def load_project(self,path):
        path = Path(path[0])
        list_file = [f.name for f in path.iterdir()]
        return list_file