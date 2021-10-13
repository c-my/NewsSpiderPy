from pageextractor.PageExtractor import PageExtractor


class IFengExtractor(PageExtractor):
    def get_title(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("div[class^=artical] h1[class^=topic-]")
        if t is None:
            t = self._soup.select_one("#artical_topic")
        return t.text.strip() if t is not None else ""

    def get_source(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("div[class^=artical] div[class^=info-] p[class^=time]>span[class^=publisher]")
        if t is None:
            t = self._soup.select_one("span[itemprop=publisher]")
        return t.text.strip() if t is not None else ""

    def get_time(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("div[class^=artical] div[class^=info-] p[class^=time]>span")
        if t is None:
            t = self._soup.select_one("span[itemprop=datePublished]")
        return t.text.strip() if t is not None else ""

    def get_content(self) -> str:
        if self._soup is None:
            return ""
        t = self._soup.select_one("div[class^=artical] div[class^=main_content-]")
        if t is None:
            t = self._soup.select_one("div #artical_real")
        return t.text.strip() if t is not None else ""
