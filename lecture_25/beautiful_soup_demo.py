from bs4 import BeautifulSoup
import requests


url = 'https://example.com'
res = requests.get(url)
html_content = res.content

soup = BeautifulSoup(html_content, 'html.parser')
title = soup.select_one('title').text
print(title)

links = soup.select('a')
for link in links:
    print(link.get('href'))