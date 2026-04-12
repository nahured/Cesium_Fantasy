from python.flask.api.file_dialog import FileDialogApi
from python.flask.api.config_project import Project


class Api:
    def __init__(self):
        self.file_dialog_api = FileDialogApi()
        self.project = Project()