# 个人用于网站自动签到
import requests
import time
#先导入time模块
def music_login():
    url = 'https://www.hifini.com/sg_sign.htm'
    cookie = {
    "bbs_sid":"828mapoefft34us64vi5upvvlm",
    "Hm_lvt_4ab5ca5f7f036f4a4747f1836fffe6f2":"1661625749",
    "bbs_token":"RD8gBfqOTtGdDzurg_2BZMBPw4F_2FjzOAFU_2F1QuZ_2FZLFGSZNNU_2B7SvcaOWaxhrRTFIRVp7Not9cgS_2F3n3EBdFsIYsZn1dM6lqlp",
    "Hm_lpvt_4ab5ca5f7f036f4a4747f1836fffe6f2":"1661625776",

    }
    #bbs_sid=828mapoefft34us64vi5upvvlm; Hm_lvt_4ab5ca5f7f036f4a4747f1836fffe6f2=1661625749; bbs_token=RD8gBfqOTtGdDzurg_2BZMBPw4F_2FjzOAFU_2F1QuZ_2FZLFGSZNNU_2B7SvcaOWaxhrRTFIRVp7Not9cgS_2F3n3EBdFsIYsZn1dM6lqlp; Hm_lpvt_4ab5ca5f7f036f4a4747f1836fffe6f2=1661625776
    # cookie='lnfidmlusername=u9036672; lnfidmluserid=2266348; lnfidmlgroupid=1; lnfidmlrnd=VLBj0JK1TJQfiAhKAaa6; lnfidmlauth=3fdb65dd61ac3ace9f3a4cf225e0cd60'
    headers = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Mobile Safari/537.36 Edg/104.0.1293.63'
       #'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        # 'Cookie': cookie
    }

    # dic={}
    # params = {
    #     'myMessage': 'message'
    # }

	#

    # 发送请求
    # res = requests.post(url=url,headers=headers,cookies=cookie,params=params ).content.decode()
    res = requests.post(url=url,headers=headers,cookies=cookie).content.decode()
    # re_name = //*[@id="nav"]/ul[2]/li[5]/a/text()
    print("==>",res)
    # print(">>>>",re_name)

music_login()



print("------------自动签到成功----------")
print("----------3s后自动关闭程序---------")
#输出123

time.sleep(3)
