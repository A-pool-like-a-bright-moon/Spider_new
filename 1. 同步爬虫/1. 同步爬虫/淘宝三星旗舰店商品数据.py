import requests
from lxml import etree
from bs4 import BeautifulSoup as bs
import time
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "cookie":"cna=zpEZGgp383cCAWXlXGTuWQTT; _m_h5_tk=8bc60c7b2b23959eb4cccdff0a1ed699_1641229590204; _m_h5_tk_enc=8375908004023cc8beebc1c6f4523a1f; xlly_s=1; cookie2=18436eb2143b7e55edec69080c4cfb33; t=0d0b4b67a9c0866f74c11eada2e2c909; _tb_token_=ef767ef175b33; _samesite_flag_=true; sgcookie=E100ui%2FIZwtWkTsNdE3r4g42M8S3S%2FEjmDlh2AQDRgTWKPvWOGjrqhN7RrYdKIkjgR61hHkUh6%2Bci3sB6mrRZ4qSnoB7rPZ73YBpeWk1BE0Iktcc%2FBwNrtjJtRixqPsE7pfe; unb=2994727198; uc3=lg2=W5iHLLyFOGW7aA%3D%3D&vt3=F8dCvUs130iAADb4Dec%3D&id2=UUGrctUUhrFxmw%3D%3D&nk2=oBK%2FjQe3Bg%2FsexAn; csg=c40edddc; lgc=%5Cu732B%5Cu732B%5Cu53EA%5Cu4F1A%5Cu55B5%5Cu55B5; cancelledSubSites=empty; cookie17=UUGrctUUhrFxmw%3D%3D; dnk=%5Cu732B%5Cu732B%5Cu53EA%5Cu4F1A%5Cu55B5%5Cu55B5; skt=01dd86d8a3cd9901; existShop=MTY0MTIyMTQ3OA%3D%3D; uc4=nk4=0%40okBekWNXKzMxmCLgf4pfssh1An9OAGU%3D&id4=0%40U2OcQgtplLwjw7OZpXL6q4%2BzS5a2; tracknick=%5Cu732B%5Cu732B%5Cu53EA%5Cu4F1A%5Cu55B5%5Cu55B5; _cc_=UIHiLt3xSw%3D%3D; _l_g_=Ug%3D%3D; sg=%E5%96%B580; _nk_=%5Cu732B%5Cu732B%5Cu53EA%5Cu4F1A%5Cu55B5%5Cu55B5; cookie1=AiPL8aNPeShabJ1SnYUvyRGsfs4Jx0lmOLACE1H36qM%3D; hng=CN%7Czh-CN%7CCNY%7C156; mt=ci=115_1; uc1=cookie21=W5iHLLyFe3xm&cookie14=UoewAecnEF%2FFEw%3D%3D&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&existShop=false&pas=0; thw=cn; JSESSIONID=240B76E3CFAD6D26FAB49DCF8D380CBB; isg=BBMTQqpedulc8zrNR1tJj135opc9yKeKlKooXsUyEjJKRDHmTZiS2DmcerQqZP-C; l=eBIcdHBeg-Vf1azBBO5Zourza77O6QAbzsPzaNbMiInca1rh1FJi5NCpnp82Rdtjgt5F8etP6yJJodewJDz_WKT5tfSeRs5mpX9w8e1..; tfstk=cziGBnXRfVz1DlanPhZsKSrxXfRRanTa1moEY0wibPZ8FFiUQsjc8ar9JpV9NC7f.; enc=AX4gbV4cMzHdAAAAAGXlWOoB%2FQX9Mv39dbX9%2Ff0Bc1bfmzPxnf%2B3p5zdkzEJwXRtMfGY16FFV3RBFeCIwiZ6",
    "referer":"https://samsung.tmall.com/category.htm?spm=a1z10.5-b-s.w4011-14649061345.36.1c2d63530Yi2TW&search=y&orderType="
}
t = int(round(time.time() * 1000))
data = {
    "_ksTS": str(t) + '_177',
    "mid": "w-14649061345-0",
    "wid": "14649061345"
}
url = "https://samsung.tmall.com/i/asynSearch.htm?_ksTS=1641311389935_177&callback=jsonp178&mid=w-14649061345-0&wid=14649061345&path=/category.htm&spm=a1z10.5-b-s.w4011-14649061345.36.1c2d63530Yi2TW&search=y&orderType=null"
page = requests.get(url=url,headers=headers).text
tree = etree.HTML(page)
div_list = tree.xpath('/html/body/div[1]/div[3]/div')[1:13]
for dl in div_list:
    dl = dl.xpath("./dl")
    for i in dl:
        title = i.xpath("./dd[2]/a/text()")[0]
        price = i.xpath("./dd[2]/div/div[1]/span[2]/text()")[0]
        print(title,price)
# for h in list_all:
#     phone_list = h.xpath('./dl')
#     for i in phone_list:
#         phone_name = i.xpath('./dd[1]/a/text()')[0]
#         phone_price = i.xpath('./dd[1]div[0]/div[0]/span[1]/text()')[0]
#         print(phone_name,phone_price)
