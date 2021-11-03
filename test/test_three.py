
import pandas as pd
import xlrd

# class test_write():
# def test_finddata():
#     demo_df = pd.read_excel(r'G:/8.python/pytest_testApi/data/addMerchant.xls')  ##文件路径
#
#     print(demo_df)
#     for indexs in demo_df.index:
#         for i in range(len(demo_df.loc[indexs].values)):
#             if (demo_df.loc[indexs].values[i] == 'actual_resul'):  # 只能传入非列名数据才能获取成功
#                 print('行数：', indexs + 1, '列数：', i + 1)
#                 print('列数：', i + 1)
#                 print(demo_df.loc[indexs].values[i])


def test_getColumnIndex():
    file = 'G:/8.python/pytest_testApi/data/addMerchant.xls'
    data = xlrd.open_workbook(file)
    table = data.sheet_by_name('addMerchant')
    columnIndex = None
    for i in range(table.ncols):
        if(table.cell_value(0, i) == 'actual_result'):
            columnIndex = i
            break
    print(columnIndex)
    return columnIndex

