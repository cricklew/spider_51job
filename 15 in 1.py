from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Tab, Pie, Line
from pyecharts.components import Table
import json
import pyecharts
from pyecharts.options import ComponentTitleOpts


def generate_data(data):
    city=[]
    salary = []
    level=['0~3k','3k~5k','5k~8k','8k~12k','12k以上']
    for item in data:
        city.append(item['city'])
        salary.append(item['salary'])
    return city,salary,level

def bar_datazoom_slider(data) -> Bar:
    level = data[2]
    city = data[0]
    title = "北成上广深"
    c = (
        Bar()
        .add_xaxis(level)
        .add_yaxis(city[0], data[1][0])
        .add_yaxis(city[1], data[1][1])
        .add_yaxis(city[2], data[1][2])
        .add_yaxis(city[3], data[1][3])
        .add_yaxis(city[4], data[1][4])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="salary（个数）"),
            datazoom_opts=[opts.DataZoomOpts()],
        )
    )
    return c


def line_markpoint(data) -> Line:
    level = data[2]
    city = data[0]
    # s=data[1]
    # print(s)
    title = "北成上广深折线图-个数"
    c = (
        Line()
        .add_xaxis(level)
        .add_yaxis(city[0], data[1][0],markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]))
        .add_yaxis(city[1], data[1][1],markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]))
        .add_yaxis(city[2], data[1][2],markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min")]))
        .add_yaxis(city[3], data[1][3],markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]))
        .add_yaxis(city[4], data[1][4],markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]))
        .set_global_opts(title_opts=opts.TitleOpts(title="北成上广深-折线图"))
    )
    return c


def pie_rosetype(data) -> Pie:
    c = (
        Pie()
        .add(
            "",
            [list(z) for z in zip(data[2], data[1][0])],
            radius=[30, 70],
            center=[120, 150],
            rosetype="area",

                    )

        .add(
            "",
            [list(z) for z in zip(data[2], data[1][1])],
            radius=[30, 70],
            center=[420, 150],
            rosetype="area",
        )
            .add(
            "",
            [list(z) for z in zip(data[2], data[1][2])],
            radius=[30, 70],
            center=[700, 150],
            rosetype="area",
        )
            .add(
            "",
            [list(z) for z in zip(data[2], data[1][3])],
            radius=[30, 70],
            center=[200, 400],
            rosetype="area",
        )
            .add(
            "",
            [list(z) for z in zip(data[2], data[1][4])],
            radius=[30, 70],
            center=[600, 400],
            rosetype="area",
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="北成上广深依次排序-玫瑰饼图"))

            )

    return c


def table_base(data) -> Table:
    table = Table()
    level = ['较低:0~3k','一般:3k~5k','中等:5k~8k','较高:8k~12k','优秀:12k以上']
    city=['beijing',"shanghai",'guang','shen','cheng']
    table.add(level,data[1]).set_global_opts(
        title_opts=opts.ComponentTitleOpts(title="表格",subtitle="城市")
    )
    return table
def  get_data():
    file = open('数据.txt',"r",encoding="utf-8",errors="ignore")
    list = []
    while True:
        mystr = file.readline()#表示一次读取一行

        if not mystr:
        #读到数据最后跳出，结束循环。数据的最后也就是读不到数据了，mystr为空的时候
            break
        data=json.loads(mystr)
        # print(data)#打印每次读到的内容
        list.append(data)
    data=generate_data(list)
    tab = Tab()
    tab.add(bar_datazoom_slider(data), "北成上广深直方图")
    tab.add(line_markpoint(data), "北成上广深折线图")
    tab.add(pie_rosetype(data), "北成上广深饼状图")
    tab.add(table_base(data), "北成上广深成表格")
    tab.render("北上广深成15 in 1图.html")

if __name__ == "__main__":
    get_data()
