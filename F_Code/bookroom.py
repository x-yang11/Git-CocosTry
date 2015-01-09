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

bookroomloginurl = "https://login.netease.com/openid/?openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.realm=http%3A%2F%2Fbr.oa.netease.com%2Fhzroom%2F&openid.sreg.required=email&openid.assoc_handle=&openid.return_to=http%3A%2F%2Fbr.oa.netease.com%2Fhzroom%2Faction%2Flogin_check%2F&openid.ns.sreg=http%3A%2F%2Fopenid.net%2Fextensions%2Fsreg%2F1.1&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select"
req = urllib2.urlopen(bookroomloginurl)
html = req.read()
print html.decode("utf-8")

