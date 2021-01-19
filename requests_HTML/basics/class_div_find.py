from requests_html import HTML

with open('python-devops/requests_HTML/basic.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)

# This will return list of the items found in the div class and article
articles = html.find('div.article')
for article in articles:
    headline = article.find('h2', first=True).text
    summary = article.find('p', first=True).text
    print(headline)
    print(summary)
    print()
