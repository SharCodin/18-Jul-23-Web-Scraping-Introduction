import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
for li in soup.select("ol.row li"):
    print(li.select_one("h3 a").get("title"))
    print(li.select_one("p.price_color").get_text(strip=True))
    print(li.select_one('a').get('href'))
    print(li.select_one('a > img').get('src'))
    print(li.select_one('p.star-rating').get_attribute_list('class')[1])
