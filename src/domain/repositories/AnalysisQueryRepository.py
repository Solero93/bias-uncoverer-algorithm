from abc import abstractmethod, ABC

from src.domain.AnalysisQuery import AnalysisQuery


class AnalysisQueryRepository(ABC):
    @abstractmethod
    def get_query(self) -> AnalysisQuery:
        pass
