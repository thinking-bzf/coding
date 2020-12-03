# -*- encoding: utf-8 -*-
# here put the import lib
import requests

url = "https://blog.csdn.net/weixin_44493666/article/details/107849463?utm_medium=distribute.pc_feed.none-task-blog-personrec_tag-3.nonecase&depth_1-utm_source=distribute.pc_feed.none-task-blog-personrec_tag-3.nonecase&request_id=5f439263cea070620e93e9dd"

payload = {}
headers = {
    'authority':
    'blog.csdn.net',
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
    'https://www.csdn.net/',
    'accept-language':
    'zh-CN,zh;q=0.9,zh-TW;q=0.8',
    'cookie':
    'uuid_tt_dd=10_35253214760-1596265284169-677258; dc_session_id=10_1596265284169.971579; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_35253214760-1596265284169-677258u00211788*1*PC_VCu00215744*1*qq_45804832; Hm_ct_facf15707d34a73694bf5c0d571a4a72=6525*1*10_35253214760-1596265284169-677258; Hm_lvt_facf15707d34a73694bf5c0d571a4a72=1596437248; Hm_up_facf15707d34a73694bf5c0d571a4a72=%7B%22islogin%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%7D; UserName=qq_45804832; UserInfo=2b765736005e4dd7b0d474adc51f14ce; UserToken=2b765736005e4dd7b0d474adc51f14ce; UserNick=qq_45804832; AU=E62; UN=qq_45804832; BT=1596634729691; p_uid=U000000; Hm_up_e5ef47b9f471504959267fd614d579cd=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%22qq_45804832%22%2C%22scope%22%3A1%7D%7D; Hm_ct_e5ef47b9f471504959267fd614d579cd=5744*1*qq_45804832u00216525*1*10_35253214760-1596265284169-677258; Hm_lvt_c7d8335446b164c71c8e512d2ad484c7=1597155565; Hm_up_c7d8335446b164c71c8e512d2ad484c7=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%22qq_45804832%22%2C%22scope%22%3A1%7D%7D; Hm_ct_c7d8335446b164c71c8e512d2ad484c7=5744*1*qq_45804832u00216525*1*10_35253214760-1596265284169-677258; Hm_lvt_e5ef47b9f471504959267fd614d579cd=1597026062,1597027524,1597027528,1597660226; announcement=%257B%2522isLogin%2522%253Atrue%252C%2522announcementUrl%2522%253A%2522https%253A%252F%252Flive.csdn.net%252Froom%252Fyzkskaka%252F5n5O4pRs%253Futm_source%253D1598583200%2522%252C%2522announcementCount%2522%253A0%257D; searchHistoryArray=%255B%2522tuniuspider%2522%252C%2522scrapytuniuspider%2522%252C%2522scrapy%2520crawl%2520tuniuspider%2522%252C%2522python%2520with%2522%252C%2522%25E7%2588%25AC%25E8%2599%25AB%2520python3%2520%25E8%25B1%2586%25E7%2593%25A3%2522%252C%2522%25E7%2588%25AC%25E8%2599%25AB%2520python3%25E8%25B1%2586%25E7%2593%25A3%2522%252C%2522%25E7%2588%25AC%25E8%2599%25AB%2520python3%2522%252C%2522%25E7%2588%25AC%25E8%2599%25AB%2520python2%2522%252C%2522%25E7%2588%25AC%25E8%2599%25AB%2522%252C%2522djano%2520views%25E6%259B%25B4%25E6%2594%25B9%25E6%2595%25B0%25E6%258D%25AE%25E5%25BA%2593%25E6%259F%2590%25E4%25B8%2580%25E5%25AD%2597%25E6%25AE%25B5%2522%255D; log_Id_pv=293; log_Id_view=611; log_Id_click=498; dc_sid=357ec46d078c280531ea1d5df53a4bab; c_first_ref=default; c_first_page=https%3A//www.csdn.net/; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1599441745,1599442467,1599459241,1599482755; c_adb=1; TY_SESSION_ID=384e5b58-618a-4154-bd01-d8ca86cf5dfd; c_segment=10; c_utm_medium=distribute.pc_feed.none-task-blog-personrec_tag-3.nonecase; c_page_id=default; dc_tos=qgagsn; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1599482760; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac=%7B%22uid_%22%3A%7B%22value%22%3A%22qq_45804832%22%2C%22scope%22%3A1%7D%2C%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%7D'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
