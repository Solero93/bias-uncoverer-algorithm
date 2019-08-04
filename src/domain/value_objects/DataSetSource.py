from dataclasses import dataclass


@dataclass
class DataSetSource:
    path: str

    def isCSV(self):
        return self.path.lower().endswith('.csv')
