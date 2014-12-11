#coding=utf-8

import string
from pyh import *

#filename格式为inout_20141201, dateid格式为20141201
#货币类型
money_type = {"1": u"金钱", "2": u"军需券"}

#投放/回收类型：1为投放（category为正数）2为回收（category为负数）

class inOutViewer():

	category_dic = {}
	inout_data = []

	def _init_(self):
		self.getCatgoryDic()

	#获取category的类型，id为负数表示回收，id为正数表示投放
	def getCatgoryDic(self):

		category_file = open("inout_category.txt","r")
		categorylines = category_file.readlines()

		for line in categorylines:
			catedic = line.split()
			if catedic[0] != "id":
				self.category_dic[catedic[0]] = catedic[1]
				#self.category_dic.append({"id": catedic[0], "value": catedic[1]})
		category_file.close()

#		print self.category_dic

	def generateData(self, filename, dateid):
		self.inout_data = []
		inout_file = open(filename, "r")
		inout_lines = inout_file.readlines()
		for lines in inout_lines:
			m = lines.split()
			if m[0] != "dateid" and m[0] == str(dateid):
				inoutDataUnit = {}
				inoutDataUnit["dateid"] = m[0]
#				inoutDataUnit["type"] = (m[1] == 1)? u"投放" : u"回收"
				inoutDataUnit["type"] = (m[1] == 1 and u"投放" or u"回收")
				inoutDataUnit["money_type"] = money_type.get(m[2], u"未录入")
				inoutDataUnit["category"] = self.category_dic.get(m[3], "未录入")
				inoutDataUnit["amount"] = m[4]
				self.inout_data.append(inoutDataUnit)
		inout_file.close()

	#根据文件名和数据生成html表格
	def generateHtml(self, filename, dateid):
		page = PyH(dateid)
		page << '<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />'
		page <<h1("2014年11月22日危机2015金币军需券投放回收列表",align='center')
		table1 = page << table(border = "1", id = "MyTable")
		headtr = table1 << tr(id='headline')
#		headtr << td(u"日期") << td(u"货币类型") << td(u"投放/回收") << td(u"分类") << td(u"数量")
		headtr << td("Date") << td("money_type") << td("Type") << td("category") << td("Amount")
		#tr1 = table1 << tr(id='line1')
		for i in range(0,16):
#		for i in range(0,len(self.inout_data) - 1):
			print i
			print self.inout_data[i]
			tr1 = table1 << tr(id='line1')
			tr1 << td(self.inout_data[i]["dateid"]) << td((self.inout_data[i]["money_type"]).encode("utf-8")) << td((self.inout_data[i]["type"]).encode("utf-8")) << td((self.inout_data[i]["category"])) << td(self.inout_data[i]["amount"])
#		tr1 << td(self.inout_data[0]["dateid"][4:-1]) << td(self.inout_data[0]["money_type"]) << td(self.inout_data[0]["type"] << td(self.inout_data[0]["amount"])<< td(self.inout_data[0]["amount"])
		'''
		i = 1
		tr1 = table1 << tr(id='line1')
		tr1 << td(self.inout_data[i]["dateid"]) << td((self.inout_data[i]["money_type"]).encode("utf-8")) << td((self.inout_data[i]["type"]).encode("utf-8")) << td((self.inout_data[i]["category"])) << td(self.inout_data[i]["amount"])
		'''
		page.printOut("2014-11-22.html")
	def topy(self, filename, dateid):
		txtfile = open(filename, "w")
		linestowrite = []
		for i in range(0,len(self.inout_data) - 1):
			print i
			mywriteline = "\t\t{\"data\":" + self.inout_data[i]["dateid"]
			mywriteline = mywriteline + ",\"money_type\":" + self.inout_data[i]["money_type"]
			mywriteline = mywriteline + ",\"type\":" + self.inout_data[i]["type"]
			#print self.inout_data[i]["category"].decode("utf-8")
			mywriteline = mywriteline + ",\"category\":" + self.inout_data[i]["category"].decode("utf-8")
			mywriteline = mywriteline + ",\"amount\":" + self.inout_data[i]["amount"]

			mywriteline = mywriteline + "},"
			print mywriteline
#			linestowrite.append(mywriteline)
#		txtfile.writelines(linestowrite)
		txtfile.close()


if __name__ == '__main__':
	m = inOutViewer()
	m.getCatgoryDic()
	m.generateData("inout_1201", "20141201")
	m.topy("outpy.py", "20141201")