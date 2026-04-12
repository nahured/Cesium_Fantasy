

export async function await_for_pywebview(){
    return new Promise((resolve) => {
        if (window.pywebview && window.pywebview.api) {
            resolve();
            return;
        }
        window.addEventListener('pywebviewready', resolve, { once: true });
    });
}



export async function open_file_dialog() {
    try {
        // Esperamos a que pywebview esté listo
        await await_for_pywebview();
        
        const files = await pywebview.api.file_dialog_api.open_file_dialog();
        
        // Aquí puedes procesar los archivos si quieres
        return files
    } catch (err) {
        console.error("Error al abrir el diálogo de archivos:", err);
    }
}