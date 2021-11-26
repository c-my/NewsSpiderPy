from abc import ABC, abstractmethod
from typing import Optional

import requests
from bs4 import BeautifulSoup
from requests import TooManyRedirects

from model.news import News


class PageExtractor(ABC):
    request_headers = {"User-Agent":
                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                           "Chrome/94.0.4606.61 Safari/537.36"}

    def __init__(self, url: str):
        self._soup = self.get_soup(url)

    def get_soup(self, url: str):
        try:
            r = requests.get(url, headers=self.request_headers)
        except TooManyRedirects as e:
            print(f"exception: {e} url: {url}")
            return None

        # 防止乱码
        # 原理：如果requests没有在header中推测出编码，则按照协议，使用ISO-8859-1编码，这就是容易出现乱码的情形
        # 因此使用get_encodings_from_content方法，从响应中探测编码（如html head中的meta中）
        if r.encoding == 'ISO-8859-1':
            encodings = requests.utils.get_encodings_from_content(r.text)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = r.apparent_encoding
            encode_content = r.content.decode(encoding, 'ignore')  # .encode('utf-8', 'ignore')
        else:
            encode_content = r.text
        soup = BeautifulSoup(encode_content, features="lxml")
        # soup = BeautifulSoup(r.text, features="lxml")
        return soup

    def get_news(self) -> Optional[News]:
        title = self.get_title()
        content = self.get_content()
        source = self.get_source()
        time = self.get_time()
        if title == "" and content == "" and source == "" and time == "":
            return None
        return News(title, content, source, time)

    @abstractmethod
    def get_title(self) -> str:
        ...

    @abstractmethod
    def get_source(self) -> str:
        ...

    @abstractmethod
    def get_time(self) -> str:
        ...

    @abstractmethod
    def get_content(self) -> str:
        ...
