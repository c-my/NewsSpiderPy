from pageextractor.PageExtractor import PageExtractor


class NeteaseExtractor(PageExtractor):
    def get_title(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("h1.post_title")
        return t.text.strip() if t is not None else ""

    def get_source(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("div.post_info")
        if t is None:
            return ""
        t_split = t.text.split("来源")
        if len(t_split) <= 1:
            return ""
        return t.text.split("来源")[1].strip() if t is not None else ""

    def get_time(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("div.post_info")
        return t.text.split("来源")[0].strip() if t is not None else ""

    def get_content(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("div.post_content>div.post_body")
        return t.text.strip() if t is not None else ""
