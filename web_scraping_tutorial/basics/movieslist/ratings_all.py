# Printing movie name director name year of release and ratings
import random
import requests
from bs4 import BeautifulSoup
url = "https://www.imdb.com/india/top-rated-tamil-movies/"


def main():
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    movies = soup.find_all('tbody', class_='lister-list')
    for movie in movies:
        movies_tr = movie.find_all('tr')
        for movie_tr in movies_tr:
            # print(movies_tr)
            movie_name = movie_tr.find('td', class_='titleColumn').a.text

            movie_director = movie_tr.find(
                'td', class_='titleColumn').a['title'].split(',')[0].replace('(dir.)', '')

            release_year = movie_tr.find(
                'td', class_='titleColumn').span.text.replace('(', '').replace(')', '')

            ratings = movie_tr.find(
                'td', class_='ratingColumn imdbRating').text

            print(f"Movie Name: {movie_name}")
            print(f"Release Year: {release_year}")
            print(f"Director Name: {movie_director}")
            print(f"Ratings: {ratings.strip()}")
            print("================================")


if __name__ == '__main__':
    main()
