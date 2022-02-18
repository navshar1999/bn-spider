import requests
from bs4 import BeautifulSoup

header = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.50'}

def book_spider(max_pages): 
    page = 1
    print("page",page)
    while page <= max_pages:
        url = 'https://www.barnesandnoble.com/b/books/_/N-1fZ29Z8q8?Nrpp=20&page=' + str(page)
        source_code = requests.get(url,headers=header)
        plain_text = source_code.content
        soup = BeautifulSoup(plain_text,features="html.parser")
        for link in soup.findAll('a',{ 'class':''}):
            href = link.get('href')
            title = link.string
            print(title)
        page += 1 

book_spider(1)