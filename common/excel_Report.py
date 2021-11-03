# -*- coding: utf-8 -*-

import  xlsxwriter
import nose

def get_format(wd, option={}):
    return wd.add_format(option)

# 设置居中
def get_format_center(wd,num=1):
    return wd.add_format({'align': 'center','valign': 'valign','border':num})
def set_border_(wd,num=1):
    return wd.add_format({}).setborder(num)

# 写数据
def _writr_center(worksheet, c1, data, ws):
    return  worksheet.write(c1, data, get_format_center(wd))
workbook = xlsxwriter.Workbook('report.xlsx')
worksheet = workbook.add_worksheet("测试总况")
worksheet2 = workbook.add_worksheet("测试详情")



def init(worksheet):

    # 设置列行的宽高
    worksheet.set_column("A:A", 15)
    worksheet.set_column("B:B", 20)
    worksheet.set_column("C:C", 20)
    worksheet.set_column("D:D", 20)
    worksheet.set_column("E:E", 20)
    worksheet.set_column("F:F", 20)

    worksheet.set_row(1, 30)
    worksheet.set_row(2, 30)
    worksheet.set_row(3, 30)
    worksheet.set_row(4, 30)
    worksheet.set_row(5, 30)

    define_format_H1 = get_format(workbook, {'bold': True, 'font_size': 18})
    define_format_H2 = get_format(workbook, {'bold': True, 'font_size': 14})

    define_format_H1.set_border(1)
    define_format_H2.set_border(1)
    define_format_H1.set_align("center")
    define_format_H2.set_align("center")
    define_format_H2.set_bg_color("blue")
    define_format_H2.set_color("#ffffff")

    worksheet.merge_range('A1:F1', '测试报告总概况', define_format_H1)
    worksheet.merge_range('A2:F2', '测试概括', define_format_H2)
    worksheet.merge_range('A3:A6', '这里放图片', get_format_center(workbook))

    _writr_center(worksheet, "B3", '项目名称', workbook)
    _writr_center(worksheet, "B4", '接口版本', workbook)
    _writr_center(worksheet, "B5", '项目语言', workbook)
    _writr_center(worksheet, "B6", '测试语言', workbook)

    data= {"test_name": "EPSP", "test_version": "V3.0", "test_p1": "java", "test_code": "python"}
    _writr_center(worksheet, "C3", data['test_name'], workbook)
    _writr_center(worksheet, "C4", data['test_version'], workbook)
    _writr_center(worksheet, "C5", data['test_p1'], workbook)
    _writr_center(worksheet, "C6", data['test_code'], workbook)

    _writr_center(worksheet, "D3", '接口总数', workbook)
    _writr_center(worksheet, "D4", '通过总数', workbook)
    _writr_center(worksheet, "D5", '失败总数', workbook)
    _writr_center(worksheet, "D6", '测试日期', workbook)

    date = {"test_sum": 100, "test_success": 80, "test_failed": 20, "test_date": "2020-9-23"}
    _writr_center(worksheet, "E3", data['test_sum'], workbook)
    _writr_center(worksheet, "E4", data['test_success'], workbook)
    _writr_center(worksheet, "E5", data['test_failed'], workbook)
    _writr_center(worksheet, "E6", data['test_date'], workbook)

    _writr_center(workbook, "F3", "分数", workbook)

    worksheet.merge_range('F4:F6', '60', get_format_center(workbook))

    pie(workbook, worksheet)


# 生成饼形图
def pie(workbook, worksheet):
    chart1 = workbook.add_chart({'type': 'pie'})
    chart1.add_series({
        'name': '接口测试统计',
        'categories': '=测试总况!$D$4:$D$5',
        'values': '=测试总况!$E$4:$E$5'
    })
    chart1.set_table({'name': '接口测试统计'})
    chart1.set_style(10)
    worksheet.insert_chart('A9', chart1, {'x_offset': 25, 'y_offset': 10})

def test_detail(worksheet):

    # 设置列行的宽高
    worksheet.set_column("A:A", 30)
    worksheet.set_column("B:B", 20)
    worksheet.set_column("C:C", 20)
    worksheet.set_column("D:D", 20)
    worksheet.set_column("E:E", 20)
    worksheet.set_column("F:F", 20)
    worksheet.set_column("G:G", 20)
    worksheet.set_column("H:H", 20)

    worksheet.set_row(1, 30)
    worksheet.set_row(2, 30)
    worksheet.set_row(3, 30)
    worksheet.set_row(4, 30)
    worksheet.set_row(5, 30)
    worksheet.set_row(6, 30)
    worksheet.set_row(7, 30)

    worksheet.merge_range('A1:H1', '测试详情', get_format(workbook,{'bold': True, 'font_size': 18, 'align': 'center', 'valign': 'vcenter', 'bg_color': 'blue', 'font_color': '#ffffff'}))
    _writr_center(worksheet, "A2", '用例ID', workbook)
    _writr_center(worksheet, "B2", '接口名称', workbook)
    _writr_center(worksheet, "C2", '接口协议', workbook)
    _writr_center(worksheet, "D2", 'URL', workbook)
    _writr_center(worksheet, "E2", '参数', workbook)
    _writr_center(worksheet, "F2", '预期值', workbook)
    _writr_center(worksheet, "G2", '实际值', workbook)
    _writr_center(worksheet, "H2", '测试结果', workbook)

    data = {"info": [{"t_id": "1001", "t_name": "登陆", "t_method": "post", "t_url": "http://XXX?login", "t_param": "{user_name:test,pwd:111111}",
                      "t_hope": "{code:1,msg:登陆成功}", "t_actual": "{code:0,msg:密码错误}", "t_result": "失败"}, {"t_id": "1002", "t_name": "商品列表", "t_method": "get", "t_url": "http://XXX?getFoodList", "t_param": "{}",
                      "t_hope": "{code:1,msg:成功,info:[{name:123,detal:dfadfa,img:product/1.png},{name:456,detal:dfadfa,img:product/1.png}]}", "t_actual": "{code:1,msg:成功,info:[{name:123,detal:dfadfa,img:product/1.png},{name:456,detal:dfadfa,img:product/1.png}]}", "t_result": "成功"}],
            "test_sum": 100,"test_success": 20, "test_failed": 80}
    temp = 4
    for item in data["info"]:
        _writr_center(worksheet, "A"+str(temp), item["t_id"], workbook)
        _writr_center(worksheet, "B"+str(temp), item["t_name"], workbook)
        _writr_center(worksheet, "C"+str(temp), item["t_method"], workbook)
        _writr_center(worksheet, "D"+str(temp), item["t_url"], workbook)
        _writr_center(worksheet, "E"+str(temp), item["t_param"], workbook)
        _writr_center(worksheet, "F"+str(temp), item["t_hope"], workbook)
        _writr_center(worksheet, "G"+str(temp), item["t_actual"], workbook)
        _writr_center(worksheet, "H"+str(temp), item["t_result"], workbook)

init(worksheet)
test_detail(worksheet2)

workbook.close()



