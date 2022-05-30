import requests
import re
import os

url = "http://www.daimg.com/photo/tour/"
# 需要爬取图片的网页地址
# https://www.tooopen.com/img/87_312.aspx可以更改，如果爬取不成功请更改网址
page = requests.get(url).text
# 得到网页源码
# 网站会有反爬取措施，包括UA/IP很正常
print(page)
# 打印成功才会能爬取，服务器返回400/404错误直接放弃
res = re.compile(r'src="(http.+?.jpg)"')
# 运用正则表达式过滤出图片路径地址
# 爬取图片网站代码里显示ipg格式，jpg可以更改
reg = re.findall(res, page)
# 匹配网页进行搜索出图片地址数组
print(reg)
# 循环遍历下载图片
# 可能筛选出几个网址
num = 0
for i in reg:
    a = requests.get(i)
    # 网址可以直接迅雷下载没必要请求
    str1 = "tupian" + str(num) + ".jpg"
    print(str1)
    f = open(str1, 'wb')
    # 以二进制格式写入图片文件夹中
    f.write(a.content)
    f.close()
    print("第%s张图片下载完毕" % num)
    num = num+1
