import requests
import os
from tqdm import tqdm
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
    'Accept-Language':
    'zh-CN,zh;q=0.9,zh-TW;q=0.8',
    'Cookie':
    'll="108298"; bid=YIM8c0oC3z8; _vwo_uuid_v2=DA59572CC5515F0AF9A0B787F07363E96|800fa068f4ddbb1f28a7cf944dc33808; __yadk_uid=2TENzogWpAYdmfaBRwFXDDe8Vgb9iG8T; dbcl2="223067959:xIw7GTJifiw"; ck=Xfzi; push_noty_num=0; push_doumail_num=0; __utmc=30149280; __utmv=30149280.22306; __utmc=223695111; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1599561500%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1259386353.1599489952.1599555333.1599561501.3; __utmb=30149280.0.10.1599561501; __utmz=30149280.1599561501.3.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.319377288.1599489955.1599555342.1599561501.3; __utmb=223695111.0.10.1599561501; __utmz=223695111.1599561501.3.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_id.100001.4cf6=c1a04398ac037345.1599446599.11.1599561677.1599556556.'
}
url = "http://nswytpic.hdu.edu.cn/studentPdf/2106842.pdf"  #网络文件地址
# get方式请求网页
pdf_list = []
root_path = r'./pdf/normal_python'
if not os.path.exists(root_path):
    os.makedirs(root_path)

with open("pdflist.txt", "r") as f:
    for line in tqdm(f.readlines()):
        pdf_list.append(line.replace('\n', ''))
        pdf_url = line.replace('\n', '')
        pdf_name = pdf_url.split('/')[-1]
        r = requests.get(url)

        with open(os.path.join(root_path, pdf_name),
                  "wb") as f:  #wb：以二进制方式写入文件
            f.write(r.content)  #r.content：以二进制方式读取文件
