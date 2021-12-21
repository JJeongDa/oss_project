import pandas as pd
import re
from bs4 import BeautifulSoup as bs
import requests

url = 'https://www.mangoplate.com/search/%EB%85%B8%EC%9B%90-%EC%84%B8%EA%B3%84%EC%9D%8C%EC%8B%9D?keyword=%EB%85%B8%EC%9B%90%20%EC%84%B8%EA%B3%84%EC%9D%8C%EC%8B%9D&page=1'

titles = []
view_counts = []
review_counts = []
menu_name = '세계음식'

res = requests.get(url.format(), headers={'User-Agent': 'Chrome'})
nowon_world = bs(res.text, 'html.parser')

list_soup = nowon_world.find_all('div', 'info')

for item in list_soup:
    title = item.find('h2', 'title').text
    title = re.sub("\n", "", title)
    titles.append(title)

    view_count = item.find('span', 'view_count').text
    view_count = re.sub(",", "", view_count)
    view_counts.append(int(view_count))

    review_counts.append(int(item.find('span', 'review_count').text))

data = {
    "메뉴종류": menu_name,
    "상호명": titles,
    "조회수": view_counts,
    "리뷰수": review_counts
}
df = pd.DataFrame(data)
df.to_csv(
    './data/nowon_world.csv', sep=',', encoding='utf-8', index=None
)
# df = pd.read_csv('./data/nowon_world.csv', index_col=0)