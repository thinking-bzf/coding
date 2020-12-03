import requests

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
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language':
    'zh-CN,zh;q=0.9,zh-TW;q=0.8',
    'Cookie':
    'Hm_lvt_73789ec364fb6d113b43644da8be6d14=1599815213; Hm_lpvt_73789ec364fb6d113b43644da8be6d14=1599815222'
}
url = "http://www.wenzizhan.com/article/217{}.html"
urls = [url.format(x) for x in range(1, 15)]
html_tags = [
    '</div>', '<div class="mainContent">', '<br />', '<p>', '</p', '&nbsp;'
]

for link in urls:
    response = requests.request("GET", link, headers=headers, data=payload)
    html = response.text
    title = html[html.find('<h1>') + 4:html.find('</h1>')]
    content_start = html.find('<div class="mainContent">')
    content_end = html.find('<div class="shareDiv">')
    content = html[content_start:content_end]
    for x in html_tags:
        content = content.replace(x, '')
    print(link)
    print(title)
    print('-' * 20)
    print(content)
    print('-' * 100)
