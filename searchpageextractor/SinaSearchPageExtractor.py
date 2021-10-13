import concurrent.futures
import re
from typing import List, Optional

import requests
from bs4 import BeautifulSoup

from model.news import News
from pageextractor.SinaExtractor import SinaExtractor
from searchpageextractor.SearchPageExtractor import SearchPageExtractor


class SinaSearchPageExtractor(SearchPageExtractor):
    _search_base_url = "https://search.sina.com.cn/news?q={}&c=news&sort=time"
    _request_headers = {"User-Agent":
                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                           "Chrome/94.0.4606.61 Safari/537.36"}

    def search_by_keyword(self, keyword: str, max_page: int) -> List[News]:
        all_item_links = self._get_all_item_links(keyword, max_page)
        search_result = []

        with concurrent.futures.ThreadPoolExecutor() as executor:

            futures = [executor.submit(SinaExtractor(link).get_news) for link in all_item_links]
            for future in concurrent.futures.as_completed(futures):
                r = future.result()
                if r is not None:
                    search_result.append(r)
        return search_result

    def _get_all_item_links(self, keyword: str, max_page: int) -> List[str]:
        url_list = []
        current_page = 1
        search_page = self._get_search_page(keyword)
        item_urls = self._get_item_urls(search_page)
        url_list.extend(item_urls)
        next_page_url = self._get_next_page_url(search_page)

        while next_page_url is not None and current_page < max_page:
            search_page = self._get_search_page_by_url(next_page_url)
            item_urls = self._get_item_urls(search_page)
            url_list.extend(item_urls)
            next_page_url = self._get_next_page_url(search_page)
            current_page += 1
        return url_list

    def _get_search_page(self, keyword: str) -> BeautifulSoup:
        search_url = self._get_search_url(keyword)
        return self._get_search_page_by_url(search_url)

    def _get_item_urls(self, soup: BeautifulSoup) -> List[str]:
        selector = "div.box-result h2>a"
        item_links = soup.select(selector)
        result_links = [link["href"] for link in item_links]
        return result_links

    def _get_search_url(self, keyword: str) -> str:
        return self._search_base_url.format(keyword)

    def _get_search_page_by_url(self, url: str) -> BeautifulSoup:
        r = requests.get(url, headers=self._request_headers)

        if r.encoding == 'ISO-8859-1':
            encodings = requests.utils.get_encodings_from_content(r.text)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = r.apparent_encoding
            encode_content = r.content.decode(encoding, 'ignore')
        else:
            encode_content = r.text
        soup = BeautifulSoup(encode_content, features="lxml")
        return soup

    def _get_next_page_url(self, soup: BeautifulSoup) -> Optional[str]:
        selector = "div.pagebox a[title='下一页']"
        next_page_tag = soup.select_one(selector)
        if next_page_tag is None:
            return None
        next_page_link_text = next_page_tag["href"]
        pattern = re.compile("javascript:linkPost\\('(.*)','(.*)'\\)")
        result = re.search(pattern, next_page_link_text)
        if result is None:
            return None
        return "https://search.sina.com.cn" + result.group(1) + result.group(2)
