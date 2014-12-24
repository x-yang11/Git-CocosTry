#coding:utf-8
import sqlite3

money_type  = {"1":u"金钱", "2":u"军需券"}
DB_SQLITE_NAME = "inout.db"

   

class inOutViewer():
	category_dic = {}
	
	
	def sqliteHandler(self):
		try:
			self.conn = sqlite3.connect(DB_SQLITE_NAME)
		except sqlite3.Error,e:  
			print("Connection to sqlite db error", "\n", e.args[0])  
			return  
		self.sqlite_cursor = self.conn.cursor()
		print "done"
		
		#如果存在表先删除  
		sql_del="DROP TABLE IF EXISTS inout;"  
		try:  
			self.sqlite_cursor.execute(sql_del)  
		except sqlite3.Error,e:  
			print "Delete table error", "\n", e.args[0]  
			return  
		self.conn.commit()


		sql_add = "CREATE TABLE inout(date VARCHAR(8), type VARCHAR(128), money_type VARCHAR(128), category VARCHAR(128),amount INTEGER );" 
		try:  
			self.sqlite_cursor.execute(sql_add)  
		except sqlite3.Error,e:  
			print "创建数据库表失败！", "\n", e.args[0]  
			return  
		self.conn.commit()  
		
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
			print lines
			m = lines.split()
#			if m[0] != "dateid" and m[0] == str(dateid):
			if m[0] != "dateid":
				inoutDataUnit = {}
				inoutDataUnit["dateid"] = m[0]
#				inoutDataUnit["type"] = (m[1] == 1)? u"投放" : u"回收"
				inoutDataUnit["type"] = (m[1] == 1 and u"投放" or u"回收")
				inoutDataUnit["money_type"] = money_type.get(m[2], u"未录入")
				inoutDataUnit["category"] = self.category_dic.get(m[3], u"未录入")
				inoutDataUnit["amount"] = m[4]
				self.inout_data.append(inoutDataUnit)
				#添加一条记录  
				#sql_insert="INSERT INTO inout values("+ inoutDataUnit["dateid"] + ", " + str(m[1]) + ", " + str(m[2]) + ", " + str(m[3]) + ", " + str(m[4]) + ");"
				sql_insert="INSERT INTO inout values("+ inoutDataUnit["dateid"] + ", \"" + inoutDataUnit["type"] + "\", \"" + inoutDataUnit["money_type"] + "\", \"" + inoutDataUnit["category"] + "\", " + str(m[4]) + ");"
				print sql_insert  
				try:  
					self.sqlite_cursor.execute(sql_insert)  
				except sqlite3.Error,e:  
					print "添加数据失败！", "\n", e.args[0]  			  
		inout_file.close()
		self.conn.commit()

	def topy(self, filename, dateid):
		txtfile = open(filename, "w")
#		linestowrite = []
		txtfile.write("\"item_lists\":\n")
		txtfile.write("\t[\n")
		for i in range(0,len(self.inout_data)):
#			print i
			mywriteline = "\t\t{\"date\": \"" + self.inout_data[i]["dateid"] + " \""
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
	m.sqliteHandler()
	m.getCategoryDic()
	m.generateData("inout.txt", "20141122")
	m.topy("outpy.py", "20141201")
