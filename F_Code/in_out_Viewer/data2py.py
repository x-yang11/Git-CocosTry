#coding:utf-8
money_type  = {"1":u"金钱", "2":u"军需券"}

class inOutViewer():
	category_dic = {}
	def getCategoryDic(self):
		category_file = open("inout_category.txt",'r')
		categorylines = category_file.readlines()

		for line in categorylines:
			catedic = line.split()
			if catedic[0] != "id":
				self.category_dic[catedic[0]] = catedic[1].decode("utf-8")
				#self.category_dic.append({"id": catedic[0], "value": catedic[1]})
		category_file.close()

		#print self.category_dic["-1"]

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
				inoutDataUnit["category"] = self.category_dic.get(m[3], u"未录入")
				inoutDataUnit["amount"] = m[4]
				self.inout_data.append(inoutDataUnit)
		inout_file.close()

	def topy(self, filename, dateid):
		txtfile = open(filename, "w")
#		linestowrite = []
		txtfile.write("\"item_lists\":\n")
		txtfile.write("\t[\n")
		for i in range(0,len(self.inout_data)):
#			print i
			mywriteline = "\t\t{\"data\": \"" + self.inout_data[i]["dateid"] + " \""
			mywriteline = mywriteline + ",\"money_type\": \"" + self.inout_data[i]["money_type"] + " \""
			mywriteline = mywriteline + ",\"type\": \"" + self.inout_data[i]["type"] + " \""
			#print self.inout_data[i]["category"].decode("utf-8")
			mywriteline = mywriteline + ",\"category\": \"" + self.inout_data[i]["category"] + " \""
			mywriteline = mywriteline + ",\"amount\": \"" + self.inout_data[i]["amount"] + " \""
			mywriteline = mywriteline + "}"
			if i != len(self.inout_data) - 1:
				mywriteline = mywriteline + ",\n"
			else:
				mywriteline = mywriteline + "\n"
		#	print mywriteline
			txtfile.write(mywriteline.encode("utf-8"))
		txtfile.write("\t]\n")
		txtfile.close()

if __name__ == '__main__':
	m = inOutViewer()
	m.getCategoryDic()
	m.generateData("inout_1201", "20141201")
	m.topy("outpy.py", "20141201")
