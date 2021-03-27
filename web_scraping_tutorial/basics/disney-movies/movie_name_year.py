import requests
from bs4 import BeautifulSoup
# Load the webpage
url = "https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films"

content = requests.get(url).text
soup = BeautifulSoup(content, 'lxml')

# movie_years = soup.find_all(class_="mw-headline")
movies = soup.find_all(class_="wikitable sortable")
year = 1930
for movie in movies:
    movie_names = movie.find_all('i')
    print(
        f"=================={year} to {year + 10}s Movies List===============================")
    for index, movie_name in enumerate(movie_names):

        print(f"{index + 1}. {movie_name.text}")
    year += 10
    if year >= 2030:
        break
