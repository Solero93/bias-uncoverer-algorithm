from dataclasses import dataclass


@dataclass
class DataSetSource:
    path: str

    def isCSV(self) -> bool:
        return self.path.lower().endswith('.csv')
