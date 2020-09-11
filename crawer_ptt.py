import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/movie/index9214.html"
base_url = "https://www.ptt.cc"

headers = {"cookie" : "cookie:_ga=GA1.2.1103462469.1594382117; __cfduid=d374f878aa1e7357310ec36e82a9bc3341597593729; _gid=GA1.2.18023345.1599660415; __cf_bm=3f1bd46b7f0030d3e998792d9233edfc3f2f2dce-1599729767-1800-Ae0qEkLnVeaOJK3DV3iEZSUmn1osm1VgQCVOSCG53CAq1pDCcsFQs9tSNkob4vrwmlf2Bzcbpzu7drSGVL6UGEk="}

res = requests.get(url , headers = headers)

bs4 = BeautifulSoup(res.text , 'lxml')

chosen = bs4.select('div.r-ent')

#抓取網址#---------------------------------------------------------------------------
url_list = []

for url_list in chosen :
    try :
        url_list = url_list.select("a")[0]["href"]
        combined = base_url + url_list
        print(combined)
    except IndexError :    #被刪除文章    解決方法1
        print("文章被刪除")

 #---------------------------------------------------------------------------

url_list = []
for url_list in chosen :
        url_list = url_list.select("a")
        if url_list :
            url_list = url_list[0]["href"]       #被刪除文章    解決方法2
            combined = base_url + url_list
            print(combined)
        else :
            pass

#---------------------------------------------------------------------------

url_list = []
for url_list in chosen :
        url_list = url_list.select("a")
        if not url_list :       #被刪除文章    解決方法3
            continue
        url_list = url_list[0]["href"]
        combined = base_url + url_list
        print(combined)
#---------------------------------------------------------------------------


    
        #抓取網址title 
for title in chosen :
    title_url = title.select(".title")
    if not title_url :
        continue
    title_url = title_url[0].text
    print(title_url.strip()) # \n Del