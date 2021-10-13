from pageextractor.PageExtractor import PageExtractor


class ChinanewsExtractor(PageExtractor):

    def get_title(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("div.content>h1")
        return t.text.strip() if t is not None else ""

    def get_source(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("div.content>div.left-time>div.left-t")
        if t is None:
            return ""
        left_text = t.text
        left_split = left_text.split("来源：")
        if len(left_split) <= 1:
            return ""
        source = left_split[1].split("参与互动")[0]
        return source.strip()

    def get_time(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("div.content>div.left-time>div.left-t")
        if t is None:
            return ""
        left_text = t.text
        return left_text.split("来源")[0].strip()

    def get_content(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("div.content>div.left_zw")
        return t.text.strip() if t is not None else ""
