import pandas as panda

class CsvOpener:

    def __init__(self):
        pass

    def read_csv_file(self, file_path: str):

        data = panda.read_csv(file_path, delimiter=";")
        return data