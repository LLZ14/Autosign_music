# 个人用于网站自动签到
import requests
import time
#先导入time模块
def music_login():
	#填写网址签到页
    url = 'XXXX'
	#填写cookie形式
    cookie = {
    "xxxxxxxxxxxxxxx":"xxxxxxxxxxxxxxx",
    "xxxxxxxxxxxxxxx":"xxxxxxxxxxxxxxx",
    "xxxxxxxxxxxxxxx":"xxxxxxxxxxxxxxx",
   

    }

    # cookie='lnfidmlusername=u9036672; lnfidmluserid=2266348; lnfidmlgroupid=1; lnfidmlrnd=VLBj0JK1TJQfiAhKAaa6; lnfidmlauth=3fdb65dd61ac3ace9f3a4cf225e0cd60'
    headers = {
        
       #'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        # 'Cookie': cookie
    }
	
    #下面用来过滤信息，不懂自行网上查
    # dic={}
    # params = {
    #     'myMessage': 'message'
    # }

	#

    # 发送请求
    # res = requests.post(url=url,headers=headers,cookies=cookie,params=params ).content.decode()//解码
    res = requests.post(url=url,headers=headers,cookies=cookie).content.decode()
    # re_name = //*[@id="nav"]/ul[2]/li[5]/a/text()
    #打印结果
    print("==>",res)
    # print(">>>>",re_name)

#调用
music_login()



print("------------自动签到成功----------")
print("----------3s后自动关闭程序---------")
#输出123

#3秒后关闭程序
time.sleep(3)
