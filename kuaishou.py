import requests
import re


headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36'
    }

headers1 = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en,zh-CN;q=0.9,zh;q=0.8,de;q=0.7",
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}
#获取快手无水印视频
share_url = 'https://v.kuaishou.com/5KV6BI'
share_res = requests.get(share_url, headers=headers1)
html = str(share_res.content)
print(html)
url = re.findall(r'(?<="srcNoMark":")(.*?)(?=&)', html)
print(url)
