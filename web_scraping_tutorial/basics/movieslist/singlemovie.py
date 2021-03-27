import random
import requests
from bs4 import BeautifulSoup
url = "https://www.imdb.com/india/top-rated-tamil-movies/"


def main():
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    # movies = soup.find('td', class_='titleColumn')
    movie_name = soup.find('td', class_='titleColumn').a.text
    movie_director = soup.find(
        'td', class_='titleColumn').a['title'].split(',')[0].replace('(dir.)', '')
    # print(movie_director)
    release_year = soup.find(
        'td', class_='titleColumn').span.text.replace('(', '').replace(')', '')
    ratings = soup.find(
        'td', class_='ratingColumn imdbRating').text

    print(f"Movie Name: {movie_name}")
    print(f"Release Year: {release_year}")
    print(f"IMDB Rating: {ratings.strip()}")
    print(f"Movie Director: {movie_director}")

    print("================================")


if __name__ == '__main__':
    main()
