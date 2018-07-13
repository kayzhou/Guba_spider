# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import os
import json
import requests
from tqdm import tqdm

in_dir = "/home/kayzhou/Project/Guba_analysis/data/origin/tweet"
out_dir = "/home/kayzhou/Project/data"


'''
for in_name in tqdm(os.listdir(in_dir)):
    in_file = os.path.join(in_dir, in_name)
    with open(os.path.join(out_dir, in_name), 'w') as f:
        for line in open(in_file):
            d = json.loads(line.strip())
            url = d['url']
            html = requests.get(url).text
            soup = BeautifulSoup(html, 'lxml')
            user_url = soup.select_one("#zwconttbn > strong > a")["href"]
            uid = user_url.split('/')[-1]
            d['uid'] = uid
            print(uid)
            d['user_url'] = user_url
            f.write(json.dumps(d, ensure_ascii=False) + '\n')
'''
