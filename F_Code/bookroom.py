import urllib2
import cookielib

'''
floor = 8
room = 3

bdate = "2015-01-19"
btime = "14"

bdate = "2015-01-19"
btime = "16"

bdt = bdate + " " + btime + ':00';
edt = bdate + " " + etime + ':00';
remark = "TujiYingxiongQA"


query_str = 'floor='+ urllib.quote(floor)
query_str = query_str +'&room=' + urllib.quote(room)
query_str = query_str + '&bdt=' + urllib.quote(bdt)
query_str = query_str + '&edt=' + urllib.quote(edt)
query_str = query_str + '&ext=' + urllib.quote(ext)
query_str = query_str + '&remark=' + eurllib.quote(remark)
query_str = query_str + '&next_url='+'/hzroom/action/adminbookroom/'
'''



req = urllib2.urlopen(bookroomloginurl)
html = req.read()
print html.decode("utf-8")

