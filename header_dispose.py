# coding=utf-8
class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict



def transHeaders():
    headers_str = '''Accept: image/avif,image/webp,image/apng,image/*,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Cookie: ASP.NET_SessionId=y2r4lqu4c53mko2ywcutqvq5; route=309dc8d5124575d958c063972bd66aa0; UM_distinctid=175f3a922291ef-05dd24e362784f-c781f38-1fa400-175f3a9222a772; CNZZDATA1000373664=1370905573-1606105987-%7C1606105987; Hm_lvt_59c4ac1df66ae9bdb2ce804f09084ea1=1606110749; Hm_lpvt_59c4ac1df66ae9bdb2ce804f09084ea1=1606110749
Host: www.muniao.com
Referer: https://www.muniao.com/
Sec-Fetch-Dest: image
Sec-Fetch-Mode: no-cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'''

    h_list = {i.split(': ')[0].strip(' ') :i.split(': ')[1].strip(' ') for i in headers_str.split('\n')}
    #print(h_list)
    print('{')
    for i in h_list:
        print("'%s': '%s',"%(i,h_list[i]))
    print('}')



if __name__ == "__main__":
    # cookie = r'SINAGLOBAL=5460900123374.248.1520572554848; UOR=,,docs.qq.com; _s_tentry=docs.qq.com; Apache=7050483468715.683.1583744246226; ULV=1583744246275:96:2:1:7050483468715.683.1583744246226:1583481575955; Ugrow-G0=5c7144e56a57a456abed1d1511ad79e8; YF-V5-G0=2583080cfb7221db1341f7a137b6762e; WBtopGlobal_register_version=3d5b6de7399dfbdb; SCF=AgiB1M589G-1bIuaOz1r9UqmL1totZGTRxw1UcFcMTRJHlvLEiVi6ts7InlX8aBiOS13oUSvJo9h7rxEoyUZgFs.; SUB=_2A25zYmJFDeRhGeVG4lcT9SfKwzSIHXVQFtSNrDV8PUNbmtAfLRWhkW9NT5Bi5ot2FjWHx035UksjE-uf46WiBxiv; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhTfsDpCgedKo7fTGEbIT725JpX5K2hUgL.FoeR1K-ESK.c1hn2dJLoIXnLxKMLB.2LBKqLxKMLBKML1-qLxKBLBonLBKnLxK-L1K5L1hnLxKMLBKML1-qLxKqL1h.LB.-LxK-LB--LBKBLxK-L12qL12zt; SUHB=0G0eg_e5jxBCG2; ALF=1584352412; SSOLoginState=1583747613; un=13817005025; wb_view_log_3895259688=1920*10801; YF-Page-G0=2f0b518c8f18c7993f214275690d6fdf|1583747638|1583747613; webim_unReadCount=%7B%22time%22%3A1583747640552%2C%22dm_pub_total%22%3A72%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A82%2C%22msgbox%22%3A0%7D'
    # trans = transCookie(cookie)
    # print trans.stringToDict()


    transHeaders()
