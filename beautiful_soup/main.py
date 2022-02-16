from operator import contains
from bs4 import BeautifulSoup
import lxml

with open('website.html', encoding='utf-8') as html_file:
    contents = html_file.read()

soup = BeautifulSoup(contents, 'html.parser')
# soup.prettify()
#prints first h3 it finds
# print(soup.h3) 

#Find all the tags named as list
all_anchor_tags = soup.find_all(name='p')

#get the text in the tags
print(all_anchor_tags[1].getText())

#get name of the tag
print(all_anchor_tags[1].name)

#get value of an attribute
all_anchor_tags = soup.find_all(name='a')
for tag in all_anchor_tags:
    print(tag.get('href'))

#find one tag with a specific id/class
heading = soup.find(name='h1', id='name')
print(heading)

soup_heading = soup.find(name='h3', class_ = 'heading')
print(soup_heading.get('class'))

#css selector
company_art = soup.select_one(selector = 'p a')
head = soup.select('.heading')
print(company_art)
print(head)