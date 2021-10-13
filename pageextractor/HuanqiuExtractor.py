from pageextractor.PageExtractor import PageExtractor


class HuanqiuExtractor(PageExtractor):
    def get_title(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("div.t-container-title>h3")
        return t.text.strip() if t is not None else ""

    def get_source(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("div.metadata-info span.source")
        return t.text.strip() if t is not None else ""

    def get_time(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("div.metadata-info p.time")
        return t.text.strip() if t is not None else ""

    def get_content(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("div.b-container div.l-con")
        return t.text.strip() if t is not None else ""
