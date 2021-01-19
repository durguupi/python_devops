from requests_html import HTML, HTMLSession

session = HTMLSession()
req = session.get('https://linuxjourney.com/lesson/file-permissions')

html = req.html

# print(html.html)

lesson = html.find('div.lesson-content', first=True)
# print(lesson.html)
header = lesson.find('h3', first=True)
print(header.text)
parag = lesson.find('p', first=True)
print(parag.text)
