# Getting the movie link and title
import requests
from bs4 import BeautifulSoup
# Load the webpage
url = "https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films"

content = requests.get(url).text
soup = BeautifulSoup(content, 'lxml')
# We are parsing using select method and having a period in each class and with italic font
movies = soup.select(".wikitable.sortable i a")
print(len(movies))
# print(movies[0:10])
# print(movies[0])
# print(movies[0].a['href'])
# print(movies[0].a['title'])
for index, movie in enumerate(movies):
    relative_path = movie['href']
    movie_title = movie['title']
    print(relative_path)
    print(movie_title)
    print()
