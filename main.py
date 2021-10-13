# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import Protocol, List

from pageextractor.ChinanewsExtractor import ChinanewsExtractor
from pageextractor.HuanqiuExtractor import HuanqiuExtractor
from pageextractor.IFengExtractor import IFengExtractor
from pageextractor.NeteaseExtractor import NeteaseExtractor
from pageextractor.SinaExtractor import SinaExtractor
from pageextractor.SohuExtractor import SohuExtractor
from pageextractor.TecentExtractor import TecentExtractor
from pageextractor.XinhuaExtractor import XinhuaExtractor
from pageextractor.YouthExtractor import YouthExtractor
from pageextractor.ZhonghuaExtractor import ZhonghuaExtractor
from pageextractor.util import get_extractor
from searchpageextractor.SinaSearchPageExtractor import SinaSearchPageExtractor
from searchpageextractor.SogouSearchPageExtractor import SogouSearchPageExtractor


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def test_page_extractor():
    pe = get_extractor("https://www.chinanews.com/gn/2021/09-27/9574765.shtml")
    n_chinanews = pe.get_news()
    pe = get_extractor("https://world.huanqiu.com/article/44j5MGsP4Cv")
    n_huanqiu = pe.get_news()
    pe = get_extractor("https://news.ifeng.com/c/89sSRm9IoyG")
    n_ifeng = pe.get_news()
    pe = get_extractor("https://www.163.com/news/article/GM4BUFRI0001899O.html?clickfrom=w_yw")
    n_netease = pe.get_news()
    pe = get_extractor("https://news.sina.com.cn/c/2021-10-12/doc-iktzqtyu1002491.shtml")
    n_Sina = pe.get_news()
    pe = get_extractor(
        "https://www.sohu.com/a/494447997_114731?code=9d318a16a855848297532ebce9face3d&spm=smpc.home.top-news1.10.1634037047160aqOPOtD&_f=index_cpc_5")
    n_sohu = pe.get_news()
    pe = get_extractor("https://new.qq.com/omn/20210927/20210927A05QTU00.html")
    n_tecent = pe.get_news()
    pe = get_extractor("http://www.news.cn/mil/2021-09/16/c_1211371426.htm")
    n_xinhua = pe.get_news()
    pe = get_extractor("https://news.youth.cn/jsxw/202109/t20210916_13222690.htm")
    n_youth = pe.get_news()
    print(n_youth)
    pe = get_extractor("https://news.china.com/domestic/945/20210809/39853554.html")
    n_zhonghua = pe.get_news()


def test_search_extractor():
    spe = SinaSearchPageExtractor()
    spe.search_by_keyword("冲突", 10)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    spe = SogouSearchPageExtractor()
    r = spe.search_by_keyword("冲突", 10)
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
