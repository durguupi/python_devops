import requests
from bs4 import BeautifulSoup
# Load the webpage
url = "https://en.wikipedia.org/wiki/Alice_in_Wonderland_(1951_film)"

content = requests.get(url).text
soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())
info_box = soup.find(class_='infobox vevent')
# print(info_box)
info_box_rows = info_box.find_all('tr')
# for row in info_box_rows:
#     print(row.prettify())
movie_info = {}


def get_content_data(row_data):
    if row_data.find('li'):
        return [li.text.strip().replace("\xa0", "") for li in row_data.find_all('li')]
    else:
        return row_data.text.strip().replace("\xa0", "")


for index, row in enumerate(info_box_rows):
    if index == 0:
        movie_info['Title'] = row.find('th').text
    elif index == 1:
        continue
    else:
        content_key = row.find('th').text.replace("company", " company")
        # Since this contains list of values sometimes we are defining function to pull that value
        content_value = get_content_data(row.find('td'))
        movie_info[content_key] = content_value


for key, value in movie_info.items():
    print(f"{key}: {value}")
