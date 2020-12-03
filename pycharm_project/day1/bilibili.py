import requests

url = "https://movie.douban.com/subject/30444960/?from=showing"

payload = {}
headers = {
    'Connection':
    'keep-alive',
    'Pragma':
    'no-cache',
    'Cache-Control':
    'no-cache',
    'Upgrade-Insecure-Requests':
    '1',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site':
    'same-origin',
    'Sec-Fetch-Mode':
    'navigate',
    'Sec-Fetch-User':
    '?1',
    'Sec-Fetch-Dest':
    'document',
    'Referer':
    'https://movie.douban.com/',
    'Accept-Language':
    'zh-CN,zh;q=0.9,zh-TW;q=0.8',
    'Cookie':
    'll="108298"; bid=YIM8c0oC3z8; _vwo_uuid_v2=DA59572CC5515F0AF9A0B787F07363E96|800fa068f4ddbb1f28a7cf944dc33808; __utma=30149280.1259386353.1599489952.1599489952.1599489952.1; __utmc=30149280; __utmz=30149280.1599489952.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; __utmb=30149280.1.10.1599489952; __utma=223695111.319377288.1599489955.1599489955.1599489955.1; __utmb=223695111.0.10.1599489955; __utmc=223695111; __utmz=223695111.1599489955.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1599489955%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; _pk_id.100001.4cf6=c1a04398ac037345.1599446599.3.1599489962.1599454764.'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
