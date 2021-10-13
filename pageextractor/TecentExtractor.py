from pageextractor.PageExtractor import PageExtractor


class TecentExtractor(PageExtractor):
    def get_title(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("div.LEFT h1")
        return t.text.strip() if t is not None else ""

    def get_source(self) -> str:
        return ""

    def get_time(self) -> str:
        return ""

    def get_content(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("div.content-article")
        return t.text.strip() if t is not None else ""
