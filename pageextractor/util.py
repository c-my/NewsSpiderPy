import re

from pageextractor import PageExtractor
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


def get_extractor(url: str) -> PageExtractor:
    pattern = re.compile("://(.*?)/")
    result = re.search(pattern, url)
    if result is None:
        return None
    domain = result.group(1)
    if domain == "www.sohu.com":
        return SohuExtractor(url)
    elif domain in ["www.163.com", "dy.163.com", "news.163.com"]:
        return NeteaseExtractor(url)
    elif domain == "new.qq.com":
        return TecentExtractor(url)
    elif domain in ["news.ifeng.com", "i.ifeng.com", "mil.ifeng.com"]:
        return IFengExtractor(url)
    elif domain == "www.chinanews.com":
        return ChinanewsExtractor(url)
    elif domain == "news.youth.cn":
        return YouthExtractor(url)
    elif domain in ["www.news.cn", "xinhuanet.com", "www.xinhuanet.com"]:
        return XinhuaExtractor(url)
    elif domain in ["world.huanqiu.com", "mil.huanqiu.com", "china.huanqiu.com"]:
        return HuanqiuExtractor(url)
    elif domain == "news.china.com":
        return ZhonghuaExtractor(url)
    elif domain == "news.sina.com.cn":
        return SinaExtractor(url)
    else:
        return None
