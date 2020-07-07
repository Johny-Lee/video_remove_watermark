import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36'
    }
share_url = 'https://share.huoshan.com/hotsoon/s/g2rklpkHL98/'
respone = requests.get(share_url, headers=headers)
split = str(respone.url)
item_id = re.findall(r"(?<=item_id=)\d+(?=\&)", split)[0]
info_url = "https://share.huoshan.com/api/item/info?item_id=" + item_id
json = requests.get(info_url)
video_id = re.findall(r'(?<=video_id\=)\w+(?=\&)', json.text)[0]
link = "https://api.huoshan.com/hotsoon/item/video/_source/?video_id=" + video_id + "&line=0&app_id=0&vquality=normal"
print(link)