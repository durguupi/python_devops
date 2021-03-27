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
    tags_all = quote.find_all(class_='tags')
    for tag in tags_all:
        tag_name = tag.find_all(class_='tag')
        words = []
        for name in tag_name:
            word = name.text
            words.append(word)

    print(
        f"=========================Quote {index + 1}==================================")
    print(f"Quotes: {remove}")
    print(f"Written by: {author_text}")
    print(f"Tags: {words}")
