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
                item = json.loads(line.strip())
                url = item['url']
                yield scrapy.Request(url=url, callback=self.parse, dont_filter=True, meta=item)

    def parse(self, response):
        item = response.meta
        user_url = response.css('#zwconttbn strong a::attr(href)').extract_first()
        item['user_url'] = user_url
        try:
            uid = user_url.split('/')[-1]
            item['uid'] = uid
        except:
            # print('用户URL无法获取。', item['url'])
            item['uid'] = '-1'
        try:
            del item['_id']
            del item['download_timeout']
            del item['download_slot']
            del item['download_latency']
            del item['redirect_times']
            del item['redirect_ttl']
            del item['redirect_urls']
        except:
            pass
        tweet = TweetFromUrlItem(item)
        