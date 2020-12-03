import requests

url = "https://space.bilibili.com/335842602"

payload = {}
headers = {
    'authority':
    'space.bilibili.com',
    'pragma':
    'no-cache',
    'cache-control':
    'no-cache',
    'upgrade-insecure-requests':
    '1',
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site':
    'same-site',
    'sec-fetch-mode':
    'navigate',
    'sec-fetch-user':
    '?1',
    'sec-fetch-dest':
    'document',
    'referer':
    'https://www.bilibili.com/',
    'accept-language':
    'zh-CN,zh;q=0.9,zh-TW;q=0.8',
    'cookie':
    '_uuid=650F4FDF-6E20-808A-8FD3-CD011B18CE4572405infoc; buvid3=D4B5EE2B-B023-46E5-BE22-2C92039195FE143083infoc; sid=9o9e1al4; DedeUserID=335842602; DedeUserID__ckMd5=d4fd5d4916cb1325; SESSDATA=a1cc49f7%2C1611742790%2Cca064*71; bili_jct=c81d85a9b50c220256c0672996f48eda; CURRENT_FNVAL=16; rpdid=|(u|u)u~)lmJ0J\'ulmYum|)kJ; LIVE_BUVID=AUTO1115962034960676; blackside_state=1; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1599191242; CURRENT_QUALITY=112; bp_video_offset_335842602=432224244288523892; bp_t_offset_335842602=432225803365855662; PVID=2; finger=-166317360'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
