from pageextractor.PageExtractor import PageExtractor


class XinhuaExtractor(PageExtractor):
    def get_title(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("div.head-line span.title")
        return t.text.strip() if t is not None else ""

    def get_source(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("div.source")
        return t.text.strip() if t is not None else ""

    def get_time(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("div.header-time")
        return t.text.strip() if t is not None else ""

    def get_content(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("#detail")
        return t.text.strip() if t is not None else ""
