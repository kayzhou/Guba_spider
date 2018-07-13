# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import os
import json
import scrapy
from ..items import TweetFromUrlItem
from tqdm import tqdm


class TweetSpider(scrapy.Spider):
    name = "tweet_from_url"

    def start_requests(self):
        in_dir = "/home/kayzhou/Project/Guba_analysis/data/origin/tweet"
        for in_name in tqdm(os.listdir(in_dir)):
            for line in open(os.path.join(in_dir, in_name)):
                d = json.loads(line.strip())
                url = d['url']
                yield scrapy.Request(url=url, callback=self.parse, dont_filter=True, meta=d)

    def parse(self, response):
        d = response.meta
        user_url = response.css('#zwconttbn strong a::attr(href)').extract_first()
        item = TweetFromUrlItem({
            'url': d['url'],
            'dt_publish': d['dt_publish'],
            'source': d['source'],
            'content': d['content'],
            'read_count': d['read_count'],
            'comment_count': d['comment_count'],
            'title': d['title'],
            'user_name': d['author'],
            'stock_id': d['stock_id'],
            'user_url': user_url
        })

        try:
            uid = user_url.split('/')[-1]
            item['uid'] = uid
        except:
            # print('用户URL无法获取。', item['url'])
            item['uid'] = '-1'

        yield item
