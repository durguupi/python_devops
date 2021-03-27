import requests
from bs4 import BeautifulSoup
import re

url = "https://quotes.toscrape.com/tag/inspirational/"
response = requests.get(url).text

soup = BeautifulSoup(response, 'lxml')
# quote_first = soup.find(class_='text')
# print(quote_first)

quotes = soup.find_all(class_='quote')
for index, quote in enumerate(quotes):
    quo = quote.find(class_='text')
    out_quote = quo.text
    # To remove quotes from the output string
    remove = out_quote[1:-1]

    author = quote.find(class_='author')
    author_text = author.text

    print(
        f"=========================Quote {index + 1}==================================")
    print(f"Quotes: {remove}")
    print(f"Written by: {author_text}")
