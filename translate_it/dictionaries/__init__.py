import requests
from lxml import etree

from .youdao import youdao_url
from .youdao.engine import parse

from ..utils import printf


def do_requests(keyword):
    res = requests.get(youdao_url % keyword)
    return etree.HTML(res.text)


def translate(keyword):
    if isinstance(keyword, list):
        keyword = ' '.join(keyword)
    # TODO 优先查询本地的单词本
    response = do_requests(keyword)
    results = parse(response)
    process(results)
    return results


def process(results):
    # TODO 如何保存这次查询的结果
    printf(results)
