import requests
from bs4 import BeautifulSoup

header = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'}

def book_spider(max_pages): 
    page = 1
    while page <= max_pages:
        url = 'https://www.barnesandnoble.com/b/books/_/N-1fZ29Z8q8?Nrpp=20&page=' + str(page)
        source_code = requests.get(url,headers=header)
        plain_text = source_code.content
        soup = BeautifulSoup(plain_text,features="html.parser")
        for product_header in soup.findAll('h3',{'class':'product-info-title'}):
            print(product_header.get_text()) 
        page = page + 1 

book_spider(1)

