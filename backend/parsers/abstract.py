# -*- coding: utf-8 -*-
import os
from pathlib import PurePath

class AbstractRouter:
    def __init__(self, project_path: str,  file_extension: str) -> None:
        self.project_path = project_path
        self.file_extension = file_extension

    def router(self,) -> dict:
        file_paths = {self.file_extension: []}
        for root, dirs, files in os.walk(self.project_path, topdown=False):
            for file_name in files:
                if file_name.endswith(self.file_extension):
                    file_path = PurePath(
                        root.replace(self.project_path, ''),
                        file_name
                    )
                    file_paths[self.file_extension].append(file_path)

        return file_paths
