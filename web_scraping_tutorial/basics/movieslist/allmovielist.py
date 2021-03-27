# This program is only for listing movie name, movie director and release year
import random
import requests
from bs4 import BeautifulSoup
url = "https://www.imdb.com/india/top-rated-tamil-movies/"


def main():
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    movies = soup.find_all('td', class_='titleColumn')

    for movie in movies:
        # print(movie)
        movie_name = movie.find('a').text
        movie_director = movie.find('a')['title'].split(',')[
            0].replace('(dir.)', '')
        release_year = movie.find(
            'span').text.replace('(', '').replace(')', '')

        print(f"Movie Name: {movie_name}")
        print(f"Release Year: {release_year}")
        print(f"Director Name: {movie_director}")
        print("================================")


if __name__ == '__main__':
    main()
