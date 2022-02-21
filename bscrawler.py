import pandas as pd 
import requests
from bs4 import BeautifulSoup


header = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'}

def book_spider(max_pages):
    page = 1
    page_numbers = []
    links = []
    titles = []
    prices = []
    while page <= max_pages:
        url = 'https://www.barnesandnoble.com/b/books/_/N-1fZ29Z8q8?Nrpp=20&page=' + str(page)
        source_code = requests.get(url,headers=header)
        plain_text = source_code.content
        soup = BeautifulSoup(plain_text,features="html.parser")
        for product_header in soup.findAll('h3',{'class':'product-info-title'}):
            title = product_header.get_text()
            titles.append(title)
            for link in product_header('a'): 
                href = "https://www.barnesandnoble.com/" + link.get('href')
                prices.append(get_single_item_data(href)) 
                links.append(href)
            #print(title)
            #print(href)
            page_numbers.append(page)
        page = page + 1 
    print("page numbers",len(page_numbers))
    print("links",len(links))
    print("titles",len(titles))
    print("prices",len(prices))

    write_to_excel("page","link","title","price",page_numbers,links,titles,prices)



def get_single_item_data(item_url: str) -> str:  
    source_code = requests.get(item_url,headers=header)
    plain_text = source_code.content
    soup = BeautifulSoup(plain_text,features="html.parser")
    for item_price in soup.findAll('span', {'class', 'price current-price ml-0'}):
        return item_price.get_text()


def write_to_excel(column1,column2,column3,column4,data1,data2,data3,data4):
    df = pd.DataFrame({column1:data1,column2:data2,column3:data3,column4:data4})
    df.to_excel('export_dataframe.xlsx',sheet_name='sheet1')

book_spider(1)



