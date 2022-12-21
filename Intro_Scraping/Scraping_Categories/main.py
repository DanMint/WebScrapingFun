from bs4 import BeautifulSoup
import requests

# --------------------------------------------------------- #
page_to_scrape = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
# --------------------------------------------------------- #

base_link = "https://books.toscrape.com/"

# Here we scrape all the links
categories = soup.find('ul', attrs={"class": "nav nav-list"})
links = []

for i in categories.find_all('a'):
    if i.has_attr('href'):
        links.append(i.attrs['href'])

for i in links:
    print(base_link + i)

