import multiprocessing
import webview
import time
import sys
from pathlib import Path


def run_webview():
    html_path = Path("src/server/index.html").resolve()
    """Esta función se ejecuta en el proceso hijo"""
    
    class Api:
        def saludar(self):
            return "¡Hola desde el proceso de la ventana!"
        
        def cerrar(self):
            webview.windows[0].destroy()  # Cierra la ventana
            return "Cerrando..."

    # Crear la ventana dentro del proceso separado
    window = webview.create_window(
        title="Ventana en Proceso Separado",
        url=str(html_path),           # puedes poner una URL o un archivo HTML
        # html="<h1>Hola desde pywebview en proceso aparte</h1>",  # alternativa
        width=1000,
        height=700,
        js_api=Api(),                           # exponemos funciones a JavaScript
        resizable=True,
        min_size=(800, 600)
    )

    # Iniciamos el loop de la GUI (esto bloquea este proceso)
    webview.start(debug=True)

if __name__ == "__main__":
    # Protegemos el punto de entrada (obligatorio en Windows con multiprocessing)
    multiprocessing.freeze_support()   # importante si luego haces exe con pyinstaller

    print("Iniciando proceso de la ventana...")

    # Creamos el proceso separado
    p = multiprocessing.Process(
        target=run_webview,
        name="PyWebView_Process",
        daemon=False          # Pon True si quieres que se cierre automáticamente al terminar el script principal
    )

    p.start()

    print(f"Ventana iniciada en proceso PID: {p.pid}")

    # Aquí puedes seguir ejecutando código en el proceso principal
    try:
        while p.is_alive():
            print("El proceso de la ventana sigue vivo...")
            time.sleep(5)
    except KeyboardInterrupt:
        print("Cerrando todo...")
        if p.is_alive():
            p.terminate()
            p.join()

    print("Programa terminado.")