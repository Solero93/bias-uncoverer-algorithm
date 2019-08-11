from abc import abstractmethod, ABC
from typing import Generator

from src.domain.AnalysisQuery import AnalysisQuery


class AnalysisQueryRepository(ABC):
    @abstractmethod
    def wait_and_get(self) -> Generator[AnalysisQuery, None, None]:
        pass
