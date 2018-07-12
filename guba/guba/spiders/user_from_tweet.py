# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import os
import json
import requests
from tqdm import tqdm

in_dir = "/home/kayzhou/Project/Guba_spider/guba/data"
out_dir = "/home/kayzhou/Project/Guba_spider/guba/user_data"


for in_name in tqdm(os.listdir(in_dir)):
    in_name = os.path.join(in_dir, in_name)
    with open(os.path.join(out_dir, in_name), 'w') as f:
        for line in open(in_name):
            d = json.loads(line.strip())
            url = d['url']
            html = requests.get(url).text
            soup = BeautifulSoup(html, "lxml")
            user_url = soup.select_one("#zwconttbn > strong > a")["href"]
            uid = user_url.split('/')[-1]
            print(uid)
            del d["download_latency"]
            del d["download_slot"]
            del d["download_timeout"]
            d['uid'] = uid
            d['user_url'] = user_url
            f.write(json.dumps(d, ensure_ascii=False) + '\n')
