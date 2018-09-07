# -*- coding: UTF-8 -*-
from scrapy import cmdline
# cmdline.execute('spider crawl douban_spider'.split())
cmdline.execute('spider crawl douban_spider -o test.csv'.split())
