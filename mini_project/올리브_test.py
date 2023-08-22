import json
from bs4 import BeautifulSoup as BS
import requests as req

def all_page(page_idx):
     url = f"https://www.oliveyoung.co.kr/store/goods/getGdasNewListJson.do?goodsNo=A000000165598&gdasSort=05&itemNo=all_search&pageIdx={page_idx}&colData=&keywordGdasSeqs=&type=&point=&hashTag=&optionValue=&cTypeLength=0"
     res = req.get(url, headers={
          "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
          "X-Requested-With" : "XMLHttpRequest"
     })

     # JSON 데이터 디코딩
     data = json.loads(res.text)
     gdas_list = data["gdasList"]

     # gdasList의 gdasScrVal(별점), gdasCont 값(리뷰)을 추출
     for i in gdas_list:
          review_point = i["gdasScrVal"]
          review_raw = i["gdasCont"]
          review_text = review_raw.replace("<br/>", " ")
          print(review_point, review_text)
          print('\n')


num_pages = 2  # 추출할 페이지 수

for page_idx in range(1, num_pages):
     all_page(page_idx)

