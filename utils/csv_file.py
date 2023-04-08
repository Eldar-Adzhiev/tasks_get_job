import csv
import shutil
from pathlib import Path

from utils.work_dir import get_absolute_path


class FileUtil:
    DIR = "generated_files/"

    def generate_dir_for_files(self):
        path_dir = Path(get_absolute_path(self.DIR))
        if not path_dir.is_dir():
            path_dir.mkdir(exist_ok=True)

    def write_csv(self, filename, data: list):
        self.generate_dir_for_files()
        with open(get_absolute_path(self.DIR + f'{filename}.csv'), 'w') as file:
            writer = csv.DictWriter(file, fieldnames=["Date", "Amount", "Transaction type"])
            writer.writeheader()
            writer.writerows({"Date": i[0], "Amount": i[1], "Transaction type": i[2]} for i in data)
        return file
