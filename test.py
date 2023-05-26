# -*- coding: utf-8 -*-
import xlsxwriter as xw
import time

system_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
system_time = system_time.replace(":", "_")
system_time = system_time.replace(" ", "_")

fileName = system_time + '_测试1.xlsx'
workbook = xw.Workbook(fileName)  # 创建工作簿
worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
worksheet1.activate()  # 激活表
title = ['序号', '毛重(kg）', '皮重(kg)','净重(kg）']  # 设置表头
worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
i = 2  # 从第二行开始写入数据
worksheet1.write('A' + str(i), 20.5)  # 写入数据，其中row为行，col为列，data为数据，bold为字体加粗
# i = 2  # 从第二行开始写入数据
# for j in range(len(data)):
#     insertData = [data[j]["id"], data[j]["name"], data[j]["price"]]
#     row = 'A' + str(i)
#     worksheet1.write_row(row, insertData)
#     i += 1
workbook.close()  # 关闭表

