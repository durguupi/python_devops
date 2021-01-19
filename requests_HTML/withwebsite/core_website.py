from requests_html import HTML, HTMLSession

session = HTMLSession()
req = session.get('https://coreyms.com/')

# print(req.status_code)
# print(req.html)
# print(req.text)

html = req.html

article = html.find('article', first=True)
print(article.html)
