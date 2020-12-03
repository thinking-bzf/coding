import requests
from lxml import etree
from bs4 import BeautifulSoup

target = 'https://www.biqukan.com/38_38836/497783246.html'
# # requests的get方法必须设置一个url 所谓目标的网址url
# req = requests.get(url=target)
# html = req.text
# bf = BeautifulSoup(html, features="html.parser")
# texts = bf.find_all('div', class_='showtxt')
# print(texts[0].text.replace('\u00A0' * 2, '\n\n'))
# server = 'https://www.biqukan.com/'
# target = 'https://movie.douban.com/subject/30444960/?from=showing'
# requests的get方法必须设置一个url 所谓目标的网址url

html = """
<div>
    <ul>
        <li><p class ="text1">这是第一个li</p></li>
        <li class="text4"><p class ="text2">这是第二个li</p></li>
        <li class="text2"><p class ="text4">这是第三个li</p></li>
    </ul>
    这是div
</div>
"""

html_obj = etree.HTML(html)
# 获取所有的li元素对象
li_list = html_obj.xpath("//div/ul/li")
for x in li_list:
    print(x)

print("--------------------------------------")

# 获取第一个li元素的内容
p_content = html_obj.xpath("//div/ul/li[1]/p/text()")
print("获取第一个li中的内容:", p_content)

print("--------------------------------------")

# 按class属性获取p元素对象
p_element = html_obj.xpath("//div/ul/li/p[@class='text1']")
print(p_element)

print("--------------------------------------")

# 获取所有class='text'的元素
x_element = html_obj.xpath("//div/ul/*[@class='text4']")
print(x_element)

print("--------------------------------------")

# 获取元素的属性
li_list_attr = html_obj.xpath("//div/ul/*[@class]")
for i in li_list_attr:
    print("class属性值: ", i.attrib["class"])

print("--------------------------------------")

# 获取当前层级和子层级的内容
print("获取当前层级")

cur_content = html_obj.xpath("//div/text()")
print(cur_content)
print("--------------------------------------")

# 获取当前与所有子级
all_content = html_obj.xpath("string(//div)")
print(all_content)