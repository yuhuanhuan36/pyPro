import os

from self import self


class global_value():
    def get_project_dir(self):
        try:
            project_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            print("the project_dir is :",project_dir)
            return project_dir
        except:
            print("Cannot find the project directory")

    PROJECT_DIR = get_project_dir()