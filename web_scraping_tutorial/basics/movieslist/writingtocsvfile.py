# Printing movie name director name year of release and ratings
import random
import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.imdb.com/india/top-rated-tamil-movies/"


def main():
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    movies = soup.find_all('tbody', class_='lister-list')
    for movie in movies:
        movies_tr = movie.find_all('tr')

        # Writing the data to csv file
        file1 = open(
            '/mnt/g/newyear_2021/python-devops/web_scraping_tutorial/basics/movieslist/tamilmovies.csv', 'w')
        writer = csv.writer(file1)

        # Writing headers
        writer.writerow(['Movie Ranking', 'Movie Name',
                         'Release Year', 'Director Name', 'Ratings'])

        for index, movie_tr in enumerate(movies_tr):
            # print(movies_tr)
            movie_name = movie_tr.find('td', class_='titleColumn').a.text

            movie_director = movie_tr.find(
                'td', class_='titleColumn').a['title'].split(',')[0].replace('(dir.)', '')

            release_year = movie_tr.find(
                'td', class_='titleColumn').span.text.replace('(', '').replace(')', '')

            ratings = movie_tr.find(
                'td', class_='ratingColumn imdbRating').text.strip()

            writer.writerow(
                [index + 1, movie_name,
                 release_year, movie_director, ratings])


if __name__ == '__main__':
    main()
