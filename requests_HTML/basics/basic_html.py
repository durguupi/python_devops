from requests_html import HTML

with open('python-devops/requests_HTML/basics/basic.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)

# To access the contents of the website we use text
print(html.text)
# To print the html format of the website
print(html.html)

# To print only the title of the sample HTML

match = html.find('Title')
# This just prints the element matching with title in the form of list
print(match)

# To print the output of the title of first match
print(match[0].text)

# To print the output of the title of first match in html format
print(match[0].html)
