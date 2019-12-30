import requests
from lxml import etree
import re
import json
def get_url():
    m = {
        '北京': "010000",
        '成都': "090200",
        '上海': "020000",
        '广州': "030200",
        '深圳': "040000", }
    for x in m:
        city=x
        city_id=m[x]
        data_gz_list = []
        for i in range(1,16):
            print('正在爬取' + city+"第"+str(i)+'页')
            url="https://search.51job.com/list/"+str(city_id)+",000000,0000,00,9,99,java%25E5%25BC%2580%25E5%258F%2591,2,"+str(i)+".html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
            }
            res=requests.get(url,headers=headers)
            res.encoding = res.apparent_encoding
            data = res.text

            get_data(data,data_gz_list)
        sava_data(data_gz_list,city)
def get_data(data,data_gz_list):
    cc = etree.HTML(data)
    data_list = cc.xpath('//span[@class="t4"]//text()')

    try:
        for data in data_list[1:]:
            if "月" in data:
                if "万" in data:
                    m = data.split("-")
                    data_such = float(m[0]) * 10
                if "千" in data:
                    m = data.split("-")
                    data_such = float(m[0])
            if "年" in data:
                if "万" in data:
                    m = data.split("-")
                    data_such = float(m[0]) * 10
                    data_such=data_such*0.12
                if "千" in data:
                    m = data.split("-")
                    data_such = float(m[0])
                    data_such = data_such * 0.12
            data_gz_list.append(int(data_such))
    except:
        pass
def sava_data(data,city):
    print(data)
    data1=[]
    num1=0
    num2 = 0
    num3 = 0
    num4=0
    num5=0
    data_num=[]
    for x in data:
        if 0<x <3:
            num1 = num1+1
        if 3<x<5:
            num2 = num2 + 1
        if 5<x<8:
            num3 = num3+1
        if 8<x<12:
            num4 = num4 + 1
        if 12<x:
            num5 = num5+1
    data_num.append(num1)
    data_num.append(num2)
    data_num.append(num3)
    data_num.append(num4)
    data_num.append(num5)
    data_list = {
        "city":city,
        "salary":data_num
    }
    with open("数据.txt",mode="a+",encoding="utf-8") as file:
        file.write(json.dumps(data_list))
        file.write('\n')
    print(city+"数据写入成功")
get_url()