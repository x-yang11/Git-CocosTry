#-*-coding:utf-8-*-
'''
Created on 2014年1月10日
@author: hhdys
'''
import urllib.request,http.cookiejar,re
class Baidu:
    def login(self):
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36')]
        resp=opener.open('http://weigou.baidu.com/')
        for c in cj:
            print(c.name,"====",c.value)
        getapiUrl = "https://passport.baidu.com/v2/api/?getapi&class=login&tpl=mn&tangram=true"
        resp2=opener.open(getapiUrl)
        getapiRespHtml = resp2.read().decode("utf-8")
        foundTokenVal = re.search("bdPass\.api\.params\.login_token='(?P<tokenVal>\w+)';", getapiRespHtml)
        if foundTokenVal :
            tokenVal = foundTokenVal.group("tokenVal")
            print(tokenVal)

            staticpage = "http://zhixin.baidu.com/Jump/index?module=onesite"
            baiduMainLoginUrl = "https://passport.baidu.com/v2/api/?login"
            postDict = {
                        'charset':"utf-8",
                        'token':tokenVal,
                        'isPhone':"false",
                        'index':"0",
                        'staticpage': staticpage,
                        'loginType': "1",
                        'tpl': "mn",
                        'callback': "parent.bd__pcbs__n1a3bg",
                        'username':"x_yang11@163.com",   #用户名
                        'password':"1q@W3e$R5t",   #密码
                        'mem_pass':"off",
                        "apiver":"v3",
                        "logintype":"basicLogin"
                        }
            postData = urllib.parse.urlencode(postDict);
            postData = postData.encode('utf-8')
            resp3=opener.open(baiduMainLoginUrl,data=postData)
            for c in cj:
                print(c.name,"="*6,c.value)

    
if __name__=="__main__":
    print("="*10,"开始")
    bd=Baidu()
    bd.login()