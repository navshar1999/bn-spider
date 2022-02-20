from re import A
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
            title = product_header.get_text()
            for link in product_header('a'): 
                href = "https://www.barnesandnoble.com/" + link.get('href')
                get_single_item_data(href)
            print(title)
            print(href)
        page = page + 1 


def get_single_item_data(item_url): 
    source_code = requests.get(item_url,headers=header)
    plain_text = source_code.content
    soup = BeautifulSoup(plain_text,features="html.parser")
    for item_price in soup.findAll('span', {'class', 'price current-price ml-0'}):
        print(item_price.get_text())
    
book_spider(1)


