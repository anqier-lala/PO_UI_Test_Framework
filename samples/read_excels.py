#coding=gbk
import os
import xlrd

current_path=os.path.dirname(__file__)
excel_path=os.path.join(current_path,'../element_info_datas/element_infos.xlsx')

workbook = xlrd.open_workbook(excel_path)
sheet = workbook.sheet_by_name('login_page')
element_infos={}
for i in range(1,sheet.nrows):
    element_info={}
    element_info['element_name']=sheet.cell_value(i,1)
    element_info['locator_type']=sheet.cell_value(i,2)
    element_info['locator_value']=sheet.cell_value(i,3)
    element_info['timeout']=sheet.cell_value(i,4)
    element_infos[sheet.cell_value(i,0)]=element_info

print(element_infos)


