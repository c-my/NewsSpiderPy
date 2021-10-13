from pageextractor.PageExtractor import PageExtractor


class ZhonghuaExtractor(PageExtractor):
    def get_title(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("h1.article_title")
        return t.text.strip() if t is not None else ""

    def get_source(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("span.source")
        return t.text.strip() if t is not None else ""

    def get_time(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("span.time")
        return t.text.strip() if t is not None else ""

    def get_content(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("#js_article_content")
        return t.text.strip() if t is not None else ""
