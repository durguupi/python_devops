# Getting user input and filtering out the jobs having that skill and writing to a file
from bs4 import BeautifulSoup
import requests

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=devops&txtLocation='
print("Put some skill that you are not familiar with")
unfamilar_skill = input(">")
print(f"Filtering out {unfamilar_skill}")
html_text = requests.get(url).text

soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
for index, job in enumerate(jobs):
    company_name = job.find(
        'h3', class_='joblist-comp-name').text.replace(' ', '')
    skills_name = job.find('span', class_='srp-skills').text.replace(' ', '')
    published_date = job.find('span', class_='sim-posted').text
    experience = job.find(
        'ul', class_='top-jd-dtl clearfix').li.text.replace('card_travel', '')
    location = job.find('ul', class_='top-jd-dtl clearfix').span.text
    more_info = job.header.h2.a['href']
    if unfamilar_skill not in skills_name:
        with open('/mnt/g/newyear_2021/python-devops/web_scraping_tutorial/jobs.txt', 'a') as fname:
            fname.write(
                f'******************************** JOB Number:{index + 1} *****************************\n')
            fname.write(f"Company Name: {company_name.strip()}\n")
            fname.write(f"Required Skills: {skills_name.strip()}\n")
            fname.write(f"Published_date: {published_date.strip()}\n")
            fname.write(f"Years of Experience: {experience.strip()}\n")
            fname.write(f"Location: {location}\n")
            fname.write(f"More_information: {more_info}\n")
            fname.write("\n")
