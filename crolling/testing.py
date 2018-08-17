import requests 
from bs4 import BeautifulSoup 

def spider(max_pages):
    page =1
    while page <max_pages:
        url = 'https://search.shopping.naver.com/search/all.nhn?origQuery=%EB%B8%94%EB%9D%BC%EC%9A%B0%EC%8A%A4&spec=M10013402%7CM10614295&pagingIndex=1&pagingSize=40&viewType=list&sort=rel&cat_id=50000804&frm=NVSHATT&query=%EB%B8%94%EB%9D%BC%EC%9A%B0%EC%8A%A4'+str(page)
        source_code = requests.get(url)
        plain_text =source_code.text