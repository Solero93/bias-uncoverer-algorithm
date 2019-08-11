from abc import abstractmethod, ABC

from src.domain.AnalysisResult import AnalysisResult


class AnalysisResultRepository(ABC):
    @abstractmethod
    def store(self, analysis_result: AnalysisResult) -> None:
        pass
