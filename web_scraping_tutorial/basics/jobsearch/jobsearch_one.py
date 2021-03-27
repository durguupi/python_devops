from bs4 import BeautifulSoup
import requests

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=devops&txtLocation='

html_text = requests.get(url).text
# print(html_text)

soup = BeautifulSoup(html_text, 'lxml')
# print(soup.prettify())

job = soup.find('li', class_="clearfix job-bx wht-shd-bx")
# print(job)

# Since we get so many white spaces while printing the job name we are going to replace it with nothing
company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
# print(company_name)

skills_name = job.find('span', class_='srp-skills').text.replace(' ', '')
# print(skills_name)

published_date = job.find('span', class_='sim-posted').text
# print(published_date)

experience = job.find(
    'ul', class_='top-jd-dtl clearfix').li.text.replace('card_travel', '')
# print(experience)
location = job.find('ul', class_='top-jd-dtl clearfix').span.text
print(location)
more_info = job.header.h2.a['href']
print(more_info)
# print(f'''
# Company Name: {company_name}
# Required Skills: {skills_name}
# Published_date: {published_date}
# ''')
