from bs4 import BeautifulSoup
import requests

# --------------------------------------------------------- #
page_to_scrape = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
# --------------------------------------------------------- #

prices = soup.findAll("p", attrs={"class": "price_color"})
price_list = []

for i in prices:
    var = i.getText(strip=True)[2:len(i.getText(strip=True))]
    price_list.append(float(var))

titles = soup.find_all('a')
book_titles = []

for link in titles:
    if link.has_attr('title'):
        book_titles.append(link.attrs['title'])

links = soup.find_all('a')
book_links = []

for link in links:
    if link.has_attr('href'):
        book_links.append(link.attrs['href'])


products = []
for i in zip(price_list, book_titles, book_links):
    products.append(i)

print(products)
