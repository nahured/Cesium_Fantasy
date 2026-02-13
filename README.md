# Cesium fantasy

> Descripcion: Programa para facilitar la creacion de mapas de fantasia para el motor [Cesiumjs](https://cesium.com/platform/cesiumjs/)

---

> Titulo: Cesium Fantasy
> Autor: Nahured
> Version: 0.0.1

> Python
> Flask: servidor
> WxPython: UI
> Pillow: trabajar con imagenes
> Numpy: para hacer calculos de Vectores


| plataformas  | esta disponible? |
| --- | --- |
| Windows | ✅ |
| Linux | ❌ |
| Mac | ❌ |

---

# Estructura de carpetas

```
cesium_fantasy/
├── src/
│   ├── gui/                        # Responsabilidad única: Interfaz gráfica (wxPython)
│   │   ├── __init__.py
│   │   ├── main_app.py             # Punto de entrada para la app de escritorio
|   |   └── modules/
│   │
│   ├── server/                     # Responsabilidad única: Lógica del servidor web (Flask)
│   │   ├── __init__.py
│   │   ├── app.py                  # Configuración y rutas de Flask (inversión de dependencias: inyecta servicios)
│   │   ├── server_py/              # modulos para el servidor
│   │   ├── templates/              # Plantillas HTML para Flask
│   │   │   └── index.html
│   │   └── static/                 # Archivos estáticos para el servidor
│   │       ├── css/
│   │       └── js/                 # JS para el frontend del servidor (utilidades JS)
│   │           ├─ modules/
│   │           │  └── Cesiumjs/    # Carpeta para colocar CesiumJs "no va incluido en el repositorio"
│   │           └── utils.js        # Ejemplo de utilidades JS
│   │
│   └── utils_py/                   # Utilidades en Python
│       ├── __init__.py
│       ├── data_handler.py         # Manejo de datos
│       └── util.py                 # Logging y utilidades generales
│
├── tests/                          # Pruebas unitarias
│   ├── test_gui.py
│   ├── test_server.py
│   └── test_utils.py
│
├── docs/                           # Documentación del proyecto
│   └── doc.md
│
├── requirements.txt                # Dependencias de python
├── main.py                         # Para ejecutar la app
└── README.md                       # Instrucciones generales
```

# Instalacion

## Crear el entorno virtual

> [!IMPORTANT] 
> la terminal del cmd tiene que estar en el principio del proyecto cesium_fantasy/

``` cmd
:: creamos el entorno virtual de python
python -m venv venv

:: activamos el entorno virtual
venv/Scripts/activate

:: isntalamos lor modulos requeridos
pip install -r requirements.txt
```

## agregar Cesiumjs

> si lo queremos hacer por consola

> [!IMPORTANT] 
> la terminal del cmd tiene que estar en el principio del proyecto cesium_fantasy/

``` cmd
:: descargar zip de cesiumjs desde su repositorio en la version 1.138
curl.exe -L -o cesium.zip https://github.com/CesiumGS/cesium/releases/download/1.138/Cesium-1.138.zip

:: extraer el zip de cesiumjs en la carpeta indicada
tar.exe -xf cesium.zip -C ./src/server/static/js/modules/Cesiumjs
```

> si quieres descargar directamente

https://github.com/CesiumGS/cesium/releases/download/1.138/Cesium-1.138.zip

y se extrae los archivos en la carpeta `./src/server/static/js/modules/Cesiumjs`