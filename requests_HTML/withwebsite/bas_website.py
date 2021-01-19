from requests_html import HTML, HTMLSession

session = HTMLSession()

req = session.get('https://httpbin.org')

# print(req.status_code)
# print(req.text)

html = req.html

title = html.find('title', first=True)
print(title.text)
print("==============================================")

wrappers_first = html.find('div.wrapper', first=True)
print(wrappers_first.html)

# print("==============================================")

# info = html.find('div.info')
# # print(info)

# print("==============================================")
# for inf in info:
#     info_head = inf.find('h2', first=True)
#     print(info_head.text)

# wrappers = html.find('div.wrapper')
# print(wrappers)
# print("==============================================")
# for wrapper in wrappers:
#     wrapper_div = wrapper.find('div', first=True)
#     print(wrapper_div.text)
