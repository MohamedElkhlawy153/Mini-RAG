from .BaseController import BaseController
from .ProcessController import ProcessController
import os

class ProcessController(BaseController):
    def __init__(self, project_id: str):
        super().__init__()
        self.project_id = project_id
        self.project_path = ProjectController().get_project_path(project_id=project_id)

    def get_file_extension(self, file_id: str):
        file_path = os.path.join(self.project_path, file_id)
        file_extension = os.path.splitext(file_path)[1]
        return file_extension

