from pageextractor.PageExtractor import PageExtractor


class YouthExtractor(PageExtractor):
    def get_title(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("div.page_title>h1")
        return t.text.strip() if t is not None else ""

    def get_source(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("#source_baidu")
        return t.text.strip() if t is not None else ""

    def get_time(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("#page_right")
        return t.text.strip() if t is not None else ""

    def get_content(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("div.page_left>div.page_k2")
        return t.text.strip() if t is not None else ""
