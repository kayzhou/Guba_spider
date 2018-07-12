# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import os
import scrapy
from ..items import GubaItem
from tqdm import tqdm


class GubaSpider(scrapy.Spider):
    name = "guba"

    def get_stock_ids(self):
        print(os.getcwd())
        stock_ids = [line.strip().split(',')[0] for line in open('guba/_id.txt')]
        stock_ids = stock_ids[1:1800]
        return stock_ids

    def start_requests(self):
        stock_ids = self.get_stock_ids()

        for stock_id in tqdm(stock_ids):
            for page in range(2, 2000):
                print('stock ->', stock_id, 'page ->', page)
                url = 'http://guba.eastmoney.com/list,{}_{}.html'.format(stock_id, page)
                yield scrapy.Request(url=url, callback=self.parse, dont_filter=True, meta={'stock_id': stock_id})

    def parse(self, response):
        for item in response.xpath('/html/body/div[6]/div[2]/div[3]/div'):
            li_info = item.xpath('span')

            if li_info[0].xpath('text()'):
                read_count = li_info[0].xpath('text()').extract_first()
                comment_count = li_info[1].xpath('text()').extract_first()
                l3 = li_info[2].xpath('a')
                title = l3.xpath('@title').extract_first()
                url = 'http://guba.eastmoney.com' + str(l3.xpath('@href').extract_first())
                author = li_info[3].xpath('a/text()').extract_first()
                if title:
                    item = GubaItem()
                    item['stock_id'] = response.meta['stock_id']
                    item['read_count'] = read_count
                    item['comment_count'] = comment_count
                    item['title'] = title
                    item['url'] = url
                    item['author'] = author
                    # item['_id'] = str(l3.xpath('@href').extract_first())[1:-5]
                    yield response.follow(url, callback=self.parse_content, meta=item)

    def parse_content(self, response):
        item = response.meta
        main = response.css('html body.hlbody div.gbbody div#mainbody div#zwcontent')
        info_publish = main.css('div#zwcontt div#zwconttb div.zwfbtime::text').extract_first()
        list_info = info_publish.split(' ')
        dt_publish = list_info[1] + ' ' + list_info[2]
        source = list_info[3]
        user_url = response.css('#zwconttbn strong a::attr(href)').extract_first()
        uid = user_url.split('/')[-1]
        try:
            content = main.css('div.zwcontentmain div#zwconbody div.stockcodec').xpath('string(.)').extract_first().strip()
            item['content'] = content
        except:
            print('缺少内容。')

        item['dt_publish'] = dt_publish
        item['source'] = source
        item['user_url'] = user_url
        item['uid'] = uid
        yield item

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        path = "guba/data/{}.txt" .format(item['stock_id'])
        return path
