import webview

class FileDialogApi:
    def __init__(self):
        self.window = None
    
    def open_file_dialog(self):
        file_types = (
            'Image Files (*.bmp;*.jpg;*.jpeg;*.png;*.gif)',
            'All files (*.*)'
        )

        try:
            window = window = webview.windows[0]
            result = window.create_file_dialog(
                webview.OPEN_DIALOG,        # Mejor usar esto en vez de webview.FileDialog.OPEN
                allow_multiple=True,
                file_types=file_types
            )
            list_path = []
            for i in range(len(result)):
                list_path.append(result[i].replace("\\","/"))
                
            return list_path or []
        except Exception as e:
            print("Error en file dialog:", e)
            return {"error": str(e)}
    
    def open_folder_dialog(self):
        try:
            window = webview.windows[0]
            result = window.create_file_dialog(
                webview.FOLDER_DIALOG,
                allow_multiple=True
            )
            a = []
            for i in range(len(result)):
                a.append(result[i].replace("\\","/"))
            return a or []
        except Exception as e:
            print("Error en file dialog:", e)
            return {"error": str(e)}
    
    def test(self):
        return "test de la api de FileDialogApi"