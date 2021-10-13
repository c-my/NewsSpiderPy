from pageextractor.PageExtractor import PageExtractor


class SohuExtractor(PageExtractor):
    def get_title(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("div.text-title h1")
        if t is None:
            t = self._soup.select_one("h3.article-title")
        return t.text.strip() if t is not None else ""

    def get_source(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("div.article-info span[data-role='original-link']")
        return t.text.strip() if t is not None else ""

    def get_time(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("div.article-info span.time")
        if t is None:
            t = self._soup.select_one("p.article-info span.time")
        return t.text.strip() if t is not None else ""

    def get_content(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("article.article")
        if t is None:
            t = self._soup.select_one("article.article-text")
        return t.text.strip() if t is not None else ""
