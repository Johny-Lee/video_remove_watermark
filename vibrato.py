import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36'
    }

url ='https://v.douyin.com/JLq1DnU/'
respone = requests.get(url, headers=headers)
split = str(respone.url)
itemId = str(split[0:split.find("?")]).replace("https://www.iesdouyin.com/share/video/","").replace("/","")
item_url = 'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=%s'
res_json = requests.get(item_url % itemId,headers=headers)
item_list = json.loads(res_json.text)['item_list']
if len(item_list)>0:
    playUrl = item_list[0]['video']['play_addr']['url_list'][0]
    playUrl = str(playUrl).replace("playwm", "play")
    print(playUrl)
    resPlay = requests.get(playUrl, headers=headers)
    print(resPlay.url)
else:
    print("视频找不到了！")
