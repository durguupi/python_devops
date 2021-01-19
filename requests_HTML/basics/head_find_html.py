from requests_html import HTML

with open('python-devops/requests_HTML/basic.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)

# print(html.text)

# In this we are selcting the class article from the html output which is in form of CSS selector as div
# Since we have used first to True. It will print only the first match
article = html.find('div.article', first=True)
print(article.text)
print()
headline = article.find('h2', first=True)
# we can add text at the end of the find as well to get the contents of the paragraph
summary = article.find('p', first=True).text
print(headline.text)
print(summary)
