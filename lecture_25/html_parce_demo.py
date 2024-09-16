from lxml import html
import requests, re


# url = 'https://example.com'
url = 'https://www.guru99.com/'
res = requests.get(url)
html_content = res.text
tree = html.fromstring(html_content)
title = tree.findtext('.//title')
print('Title of the page is:', title)
pattern = r"(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,})(\.[a-zA-Z0-9]{2,})?"

links = tree.xpath('//a/@href')
links_filtered = []
for link in links:
    if re.search(pattern, link):
        links_filtered.append(link)

for link in links_filtered:
    print(link)

print(len(links_filtered))
distinct_links = set(links_filtered)
print('distinct', len(distinct_links))

# links = tree.xpath('//a/text()')
# for link in links:
#     print('Link:', link)