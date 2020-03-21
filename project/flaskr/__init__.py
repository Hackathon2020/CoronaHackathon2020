import os
import pathlib

project_dir = pathlib.Path(os.path.abspath(os.path.dirname(__file__)))
static_folder = pathlib.Path(project_dir, "static")
template_folder = pathlib.Path(project_dir, "templates")