# This will list the jobs only based on the location
from bs4 import BeautifulSoup
import requests

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=devops&txtLocation='

html_text = requests.get(url).text

soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
for job in jobs:
    location = job.find('ul', class_='top-jd-dtl clearfix').span.text
    if location == 'Pune':
        company_name = job.find(
            'h3', class_='joblist-comp-name').text.replace(' ', '')
        skills_name = job.find(
            'span', class_='srp-skills').text.replace(' ', '')
        published_date = job.find('span', class_='sim-posted').text
        experience = job.find(
            'ul', class_='top-jd-dtl clearfix').li.text.replace('card_travel', '')

        print(f"Company Name: {company_name.strip()}")
        print(f"Required Skills: {skills_name.strip()}")
        print(f"Published_date: {published_date.strip()}")
        print(f"Years of Experience: {experience.strip()}")
        print(f"Location: {location}")
        print('=============================')
