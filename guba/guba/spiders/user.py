# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import UserItem

user_pool = set([])


class UserSpider(scrapy.Spider):
    name = 'user'
    start_urls = ['http://iguba.eastmoney.com/2381134614145238/tafollow']

    def parse(self, response):
        followers_str = response.xpath('/html/body/script[2]/text()').extract_first()
        start_index = followers_str.find('{')
        end_index = followers_str.find(';\r\n\t\t$')
        data = json.loads(followers_str[start_index: end_index])
        res = data['re']
        count = data['count']
        
        print(count, len(res))

        for u in res:
            if u['user_id'] in user_pool:
                continue
            user_pool.add(u['user_id'])
            item = UserItem()
            item['user_id'] = u['user_id']
            item['name'] = u['user_nickname']
            item['guba_age'] = u['user_age']
            item['following_count'] = u['user_following_count']
            item['follower_count'] = u['user_fans_count']
            item['post_count'] = u['user_post_count']
            item['intro'] = u['user_introduce']
            item['stock_count'] = u['user_select_stock_count']
            item['is_majia'] = u['user_is_majia']
            item['level'] = u['user_level']
            url = 'http://iguba.eastmoney.com/' + u['user_id']
            next_url = url + '/tafollow'
            yield response.follow(next_url, callback=self.parse_follow, meta=item)


    def parse_follow(self, response):
        item = response.meta
        followers_str = response.xpath('/html/body/script[2]/text()').extract_first()
        start_index = followers_str.find('{')
        end_index = followers_str.find(';\r\n\t\t$')
        data = json.loads(followers_str[start_index: end_index])
        res = data['re']
        count = data['count']
        print('用户池大小', len(user_pool))
        item['following_list'] = [u['user_id'] for u in res]

        with open('data/follow.txt', 'a') as f:
            f.write(json.dumps(dict(item), ensure_ascii=False) + '\n')

        for u in res:
            if u['user_id'] in user_pool:
                continue
            user_pool.add(u['user_id'])
            follow_item = UserItem()
            follow_item['user_id'] = u['user_id']
            follow_item['name'] = u['user_nickname']
            follow_item['guba_age'] = u['user_age']
            follow_item['following_count'] = u['user_following_count']
            follow_item['follower_count'] = u['user_fans_count']
            follow_item['post_count'] = u['user_post_count']
            follow_item['intro'] = u['user_introduce']
            follow_item['stock_count'] = u['user_select_stock_count']
            follow_item['is_majia'] = u['user_is_majia']
            follow_item['level'] = u['user_level']
            url = 'http://iguba.eastmoney.com/' + u['user_id']
            next_url = url + '/tafollow'
            yield response.follow(next_url, callback=self.parse, meta=follow_item)