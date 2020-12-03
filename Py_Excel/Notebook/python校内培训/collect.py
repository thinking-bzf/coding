from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from pyquery import PyQuery as pq
import math
import os,sys
import re
import time
import traceback
import pandas as pd
import numpy as np
import random
import tools

option = webdriver.ChromeOptions()
prefs = {}
option.experimental_options["prefs"] = prefs
prefs["profile.default_content_settings"] = {"images": 2}
prefs["profile.managed_default_content_settings"] = {"images": 2}
browser = webdriver.Chrome(
    "D:/Program Files/Google/Chrome/chromedriver.exe", options=option)
browser.implicitly_wait(10)
browser.set_page_load_timeout(10)

furl = ""
fid = 0
fpn = 0
log_path = "final_state.log"

csv_path = "data.csv"

wait = 1

if os.path.isfile(csv_path):
    print("Warn: File existed. Use another file name.")
    sys.exit(-1)
else:
    df = pd.DataFrame(columns=["概述", "厂商",
                               "级别", "车龄", "里程",
                                           "排量",  "排放标准", "自动挡", "商业险", "异常数", "健康度", "新车价", "价格", "URL"])


pf_dicts = {"国一": 1, "国二": 2, "国三": 3, "国四": 4, "国五": 5, "国六": 6}


def get_UrlList(pn, origin='https://www.guazi.com/www/buy/', host='https://www.guazi.com'):
    url_list = []
    try:
        url = origin+'o'+str(pn)+'c-1/#bread'
        global furl
        global fpn
        fpn = pn
        furl = url
        time.sleep(wait)
        browser.get(url)
        nts = True
        while nts:
            source = browser.page_source
            doc = pq(source)
            if doc.text().find("警告") != -1:
                time.sleep(5)
                browser.refresh()
            else:
                nts = False
        car_list = doc('.list.retina .list-wrap.js-post ul li').items()
        for car in car_list:
            car_url = car('a').attr.href
            is_url = False
            if type(car_url) == str and re.match('.*fr_no=\d+$', car_url) != None:
                is_url = True
            if is_url:
                url_list.append(host+car_url)
    except TimeoutException:
        browser.execute_script("window.stop();")
    finally:
        pass
    if len(url_list) == 0:
        print("Warn: Empty list on %s" % url)
    return url_list


def url_gen(start_p, start_i):
    u_list = []
    p = start_p
    i = start_i
    k = 0
    u_list = get_UrlList(start_p)
    count = len(u_list)
    global fid
    while i > count:
        i -= count
        k += 1
        u_list = get_UrlList(start_p+k)
    for j in range(1, i):
        u_list.pop(0)
        fid += 1
    while True:
        try:
            ct = len(u_list)
            if ct != 0:
                fid += 1
                yield u_list[0]
                u_list.pop(0)
            else:
                k += 1
                u_list = get_UrlList(start_p+k)
        except Exception:
            print(traceback.format_exc())


def data_gather(url):
    try:
        time.sleep(wait)
        browser.get(url)
        nts = True
        while nts:
            source = browser.page_source
            doc = pq(source)
            if doc.text().find("警告") != -1:
                time.sleep(5)
                browser.refresh()
            else:
                nts = False

        # 新车价
        xc = doc('.detail .center.js-center.detail .infor-main.clearfix.service-open .product-textbox .pricebox.js-disprice .newcarprice').text()
        # 缺失维度直接丢弃
        if re.match('^.*新', xc) == None:
            return None
        xc = int(tools.get_num_float(xc) * 10000)

        # 概述
        gsd = doc(
            '.detail .center.js-center.detail .infor-main.clearfix.service-open .product-textbox h2')
        gs = gsd.text().replace(gsd.find('span').text(), "").strip()

        # 厂商
        cs = doc(
            '.detail .center.js-center.detail .basic-infor.js-basic-infor.js-top .detailcontent.clearfix.js-detailcontent.active .param-table.one tbody tr:nth-child(3) .td2').text().split(" ")[0]

        # 级别
        jb = doc(
            '.detail .center.js-center.detail .basic-infor.js-basic-infor.js-top .detailcontent.clearfix.js-detailcontent.active .param-table.one tbody tr:nth-child(4) .td2').text().split(" ")[0]

        # 上牌时间
        cl = doc('.detail .center.js-center.detail .infor-main.clearfix.service-open .product-textbox .assort.clearfix .one span').text()
        cl = tools.get_age(cl)

        # 里程数
        lc = doc('.detail .center.js-center.detail .infor-main.clearfix.service-open .product-textbox .assort.clearfix .two span').text()
        lc = int(tools.get_num_float(lc)*10000)

        # 排量
        pl = doc(
            '.detail .center.js-center.detail .basic-infor.js-basic-infor.js-top ul .six div').text()
        pl = float(pl)

        # 排放标准
        pf = doc(
            '.detail .center.js-center.detail .basic-infor.js-basic-infor.js-top ul .four div').text().split(" ")[0]
        pf = pf_dicts[pf]

        # 异常数/健康度
        jkd = doc('.detail .center.js-center.detail .guazi-renzheng .bgbox ul li div .c-number .icon-yellow-error.js-yellow-error .fc-org-text')
        yc = 0
        for it in jkd.items():
            yc += tools.get_num_int(it.text())
        jk = 1.0-float(yc)/259

        # 自动挡
        zd = doc('.detail .center.js-center.detail .infor-main.clearfix.service-open .product-textbox .assort.clearfix .last span').text()
        if re.match('^手动', zd) != None:
            zd = 0
        else:
            zd = 1

        # 商业险
        bx = doc(
            '.detail .center.js-center.detail .basic-infor.js-basic-infor.js-top ul .last div').text().split(" ")[0]
        if re.match('^已过期', bx) != None:
            bx = 0
        else:
            bx = 1
        # 价格
        jg = doc('.detail .center.js-center.detail .infor-main.clearfix.service-open .product-textbox .pricebox.js-disprice .pricestype').text()
        jg = int(tools.get_num_float(jg)*10000)

        data = {"概述": gs, "厂商": cs,
                "级别": jb, "车龄": cl, "里程": lc,
                "排量": pl,  "排放标准": pf, "自动挡": zd, "商业险": bx, "异常数": yc,  "健康度": jk, "新车价": xc, "价格": jg, "URL": url
                }
        return data
    except TimeoutException:
        browser.execute_script("window.stop();")
    except:
        print("Data Error:" + url)
    finally:
        pass


def data_gen(start_p, start_i, num):
    urls = url_gen(start_p, start_i)
    i = 0
    while i < num:
        url = next(urls)
        # 调试输出
        #print("%s" % (url))
        data = data_gather(url)
        if data != None:
            i += 1
            yield data


ans = data_gen(2, 7, 5)
j = 0
try:
    for i in ans:
        j += 1
        print("Data[%d]:" % (j))
        print(i)
        df = df.append(i, ignore_index=True)
        if j % 10 == 0:
            df.to_csv(csv_path, mode='w')
            if os.path.exists("break"):
                os.remove("break")
                break
        if j % 99 == 0:
            browser.delete_all_cookies()
            time.sleep(random.randint(10, 30))
except Exception:
    print(traceback.format_exc())
else:
    df.to_csv(csv_path, mode='w')
finally:
    with open(log_path, mode='w') as f:
        f.write(furl+"\n"+str(fpn)+"\n"+str(fid))
    browser.close()
    pass
