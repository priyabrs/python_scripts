# from urllib import response
import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/news')
yc_webpage = response.text
# print()

soup = BeautifulSoup(yc_webpage, 'html.parser')
article_tag = soup.find_all(name='a', class_='titlelink')
#get_text
print(article_tag.getText())

#get specific element from a tag

print(article_tag.get('href'))

#get upvote count
upvote_tag = soup.find(name='span', class_='score')
print(upvote_tag.getText())
article_text = []
article_link = []
for tag in article_tag:
    article_text.append(tag.getText())
    article_link.append(tag.get('href'))

article_upvotes = [ int(score.getText().split(' ')[0]) for score in soup.find_all(name='span', class_='score')]
# article_upvotes = list(map(lambda x:int(x.split(' ')[0]), article_upvotes_text))
# print(article_upvotes)

import pandas as pd
# print(article_text)
# print(article_link)
print(len(article_upvotes))
# df = pd.DataFrame(
#     {
#         'article_text':article_text,
#         'article_link':article_link,
#         'article_upvotes':article_upvotes
#     }
# )


# print(df)