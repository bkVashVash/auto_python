# todo 使用正则从日志文件里提取想要的信息

import datetime,os,re
import pprint
'''
#1,信息为空                ["{'errCode': 10005, 'errMsg': '文章信息不能为空'}",
#2  采集成功               "{'errCode': 10000, 'errMsg': '长江商报2018年12月第20181225期文章采集成功'}"]
# 3，报错 spider ,error    ['ERROR: Spider error processing <GET http://www.changjiangtimes.com/> (referer: None)
#4, 数据重传               ERROR: Scraper close failure
'''

# todo 从log里第一次读取数据

with open(os.path.abspath('../') + 'log' +'\\{}.log'.format(datetime.datetime.now().strftime('%Y-%m-%d')),'r',encoding='UTF-8') as f:
    text = f.read()
cc1 = re.compile("{'errCode'.*?}")
cc2 = re.compile("ERROR.*?\)")
vv1 = cc1.findall(text)
vv2 = cc2.findall(text)
pprint.pprint(vv1)
pprint.pprint(vv2)


# todo 进一步提取报名和时间
cc = {}
for i in vv1:
    try:
        # {'errCode': 10000, 'errMsg': '每日商报2018年12月第20181229期文章采集成功'}
        cc3 = re.compile("\'errMsg\': \'(.*?报).*?第(.*?)期")
        cc4 = re.compile("\'errMsg\': \'(.*?刊).*?第(.*?)期")

        ll1 = cc3.search(i).group(1)
        ll2 = cc3.search(i).group(2)
        cc[ll1] = ll2

        # todo 结尾为刊的需手动添加
        # ll3 = cc4.search(i).group(1)
        # ll4 = cc4.search(i).group(2)
        # cc[ll3] = ll4

    except AttributeError:
        pass
pprint.pprint(cc)