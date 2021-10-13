from abc import ABC, abstractmethod
from typing import List

from model.news import News


class SearchPageExtractor(ABC):
    @abstractmethod
    def search_by_keyword(self, keyword: str, max_page: int) -> List[News]:
        ...
