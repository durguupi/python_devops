from requests_html import HTML

with open('python-devops/requests_HTML/basic.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)

# print(html.html)
# To find the title of the website ,we have to filter it with the keyword "find" as title.
# Here title can be many and it returns the list of elements
# So first to get only first match of title we use the following way

# FIND method uses CSS selectors
match = html.find('Title', first=True)
print(match.text)

# To find <div id="footer"> we have to use the # symbol
match_foot = html.find('#footer', first=True)
print(match_foot.text)
