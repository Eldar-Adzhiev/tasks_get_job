from pathlib import Path


def get_absolute_path(path: str):
    filename = str(Path(path))
    root_dir_project = str(Path(__file__)).replace(str(Path("utils/work_dir.py")), "")
    return root_dir_project + filename
