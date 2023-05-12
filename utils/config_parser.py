import json
from utils.work_dir import get_absolute_path


class ConfigParser:
    config = None

    def __init__(self, path):
        self.path = path

    def open_config(self):
        with open(get_absolute_path(self.path), 'r', encoding="utf8") as fd:
            self.config = json.load(fd)

    def get_config(self):
        if self.config is None:
            self.open_config()
        return self.config

    def write_config(self, data: dict):
        data_for_write = json.dumps(data)
        with open(get_absolute_path(self.path), "w", encoding="utf8") as file:
            file.write(data_for_write)
