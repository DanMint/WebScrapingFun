from bs4 import BeautifulSoup
import requests
import csv

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

all_titles = []
all_prices = []
all_links = []

for i in range(len(links)):
    # --------------------------------------------------------- #
    page_to_scrape_new = requests.get(base_link + links[i])
    temp_soup = BeautifulSoup(page_to_scrape_new.text, "html.parser")
    # --------------------------------------------------------- #

    prices = temp_soup.findAll("p", attrs={"class": "price_color"})
    price_list = []

    for j in prices:
        var = j.getText(strip=True)[2:len(j.getText(strip=True))]
        price_list.append(float(var))

    # Here we start playing with links(href).
    titles = temp_soup.find_all('a')
    book_titles = []

    for link in titles:
        # Here we only want the title of the href
        if link.has_attr('title'):
            book_titles.append(link.attrs['title'])

    links_of_books = temp_soup.find_all('a')
    book_links = []

    for link in links_of_books:
        # Here we actualy want the link itself.
        if link.has_attr('href'):
            book_links.append(link.attrs['href'])

    for j in book_titles:
        all_titles.append(j)

    for j in price_list:
        all_prices.append(j)

    for j in book_links:
        all_links.append(j)

Details = ['Book Title', 'Price', 'Link']
all_info = list(zip(all_titles, all_prices, all_links))

with open('All_Books_Info.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(Details)
    write.writerows(all_info)
