import json
import os
import re
import requests
import jsonpath

class sgdsm(object):
    ''''
    <<电力需求侧管理>>
    http://www.sgdsm.com/ch/index.aspx
    '''
    def __init__(self,title,filepath='./'):
        self.title = title
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        }
        self.path = filepath

    def get_all_info(self):
        url = 'http://www.sgdsm.com/ch/reader/key_query.aspx?field=title&key=' + self.title
        resp = requests.get(url, headers=self.headers)
        file_path = self.path + 'article_info.json'
        with open(file_path, 'w') as f:
            f.write(resp.text.encode("gbk", 'ignore').decode("gbk", "ignore"))
        return file_path

if __name__ == '__main__':
    sgdsm = sgdsm('用户')
    sgdsm.get_all_info()