# -*- coding:utf-8 -*- 
'''
此程序为游戏资源导表程序
Excel: ./Tables/游戏图片表.xlsx
Lua  : ./Program/src/cdata/resource_gameResource_table.lua
表名：gameResource_table
数据结构如下:
	name:文件名称
	width:文件宽度
	height:文件高度
	xStart:起始横坐标
	yStart:起始纵坐标
	xEnd:结束横坐标
	yEnd:结束纵坐标
'''  
import xlrd

luaFileName = "resource_gameResource_table.lua"
excelFileName = u"游戏图片表.xlsx"
excelPath = "../Tables/"
luaPath = "../Program/src/cdata/"
cdataName = "gameResource_table"

cdata = open(luaPath + luaFileName, "w")
table = xlrd.open_workbook(excelPath + excelFileName)
dataSheet = table.sheets()[0]

cdata.writelines(cdataName + "={}\n")
sheetLength = dataSheet.nrows

for i in range(2,sheetLength - 1):
	dataLine = dataSheet.row_values(i)
	cdata.writelines("%s[\"%s\"] = {\n\twidth = %d,\n\theight = %d,\n\txStartx = %d,\n\tyStart = %d,\n\txEnd = %d,\n\tyEnd = %d\n\t}\n" %(cdataName, dataLine[0], dataLine[1], dataLine[2], dataLine[4], dataLine[6], dataLine[8], dataLine[10]))
cdata.close()
