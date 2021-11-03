import xlrd
from xlwt import *
from xlutils.copy import copy

xlsfile = 'G:/8.python/pytest_testApi/data/test.xls'
book = xlrd.open_workbook(xlsfile)

sheet_name = book.sheet_names()
print(sheet_name)

sheet = book.sheet_by_index(0)
nrows = sheet.nrows
ncols = sheet.ncols
print(nrows)
print(ncols)

row_data = sheet.row_values(0)
col_data = sheet.col_values(0)
print(row_data)
print(col_data)

cell_value = sheet.cell_value(3,0)
print(cell_value)
cell_value2 = sheet.cell(3,0)
print(cell_value2)

sheet.put_cell(1,2,1,"test",0)
cell_value2 = sheet.cell(1,1)
print(cell_value2)

#保存xlsfile
wb = copy(book)
wb.save(xlsfile)