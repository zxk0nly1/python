import requests

url="https://www.baidu.com/s?"
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
         "Cookie":"BIDUPSID=CD95780DF85977224311D897985F2B27; PSTM=1560181566; BD_UPN=12314753; BAIDUID=CD95780DF85977224311D897985F2B27:SL=0:NR=10:FG=1; sug=3; sugstore=1; bdime=0; BDUSS=1GNlctb2dBeE80ajlCMmlsNTZ0cXVPSW1HYVotRnMteWNTZ3J1cWNkM3VOTUpkRVFBQUFBJCQAAAAAAAAAAAEAAAD-9M9JcG9pas7eu9oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO6nml3up5pdSW; H_WISE_SIDS=133106_114552_136646_136749_136626_128064_134982_136435_120144_132909_136456_136619_131246_136722_132378_131518_118881_118862_118838_118821_118805_107319_132783_136800_136429_133352_136864_136812_137009_129648_136195_132250_135307_133847_132552_134047_129645_131423_134489_134317_136165_136558_110085_127969_131951_135624_136614_135458_127416_136636_134846_134352_132467_136537; ORIGIN=2; ISSW=1; ISSW=1; BD_HOME=1; H_PS_PSSID=1453_21118_30210; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BD_CK_SAM=1; PSINO=7; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_645EC=ee52Y5Gp8Gs98sFcH9kBEA00P%2Fx2XJR16jK8oR%2BdT5PBs6P%2B3e4EWgZCHOeJVSfujKnD"}
for page in range(1,5):
    pn=(page-1)*10 #构造翻页参数的值
    params={
        "wd":"篮球",
        "pn":str(pn)
    }
    res=requests.get(url,headers=headers,params=params)
    res.encoding="utf-8"
    html=res.text
    print(res.url)#返回真实url地址
    print(html)
    print("----------------------------------------------------------------------")