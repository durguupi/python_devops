from bs4 import BeautifulSoup

with open('/mnt/g/newyear_2021/python-devops/web_scraping_tutorial/basics/home.html', 'r') as htmlfile:
    content = htmlfile.read()
    # print(content)

# We are creating an instance of beautifulsoup and first argument we will be passing is html file
# and then the name of the parser in this case it is lxml
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())

# Grab all the html tags which is h5
    tags = soup.find("h5")  # It grabs only the first value of h5 it finds.
    tags_all = soup.find_all('h5')  # This grabs all the values of h5
    # print(tags_all)

# Now we can use the above way to get all the courses defined in the html file
    courses_html_tags = soup.find_all('h5')
    for course in courses_html_tags:
        print(course.text)
    print("===================")

    # Now we are going to get the course name as wel the proce assoicated with it
    # We use class_ since class is keyword in python
    course_cards = soup.find_all('div', class_='card')

    for card in course_cards:
        course_name = card.h5.text
        course_price = card.a.text.split()[-1]
        # We are splitting so we can get only the last element of the price which is price value
        # course_price_split = card.a.text.split()
        # print(course_price_split[-1])
        print(f"The {course_name} costs {course_price}")
