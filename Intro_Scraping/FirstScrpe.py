from bs4 import BeautifulSoup
import requests

# This means go to this website
page_to_scrape = requests.get("https://quotes.toscrape.com/")
# Here we use soup to parse the website 
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
# He we scrape
quotes = soup.findAll("span", attrs={"class": "text"})
authors = soup.findAll("small", attrs={"class": "authors"})

for quote in quotes:
    print(quote)

for author in authors:
    print(author)
