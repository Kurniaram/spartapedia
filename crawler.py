import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# Start coding
# tag.text
# tag['attribute']

movies = soup.select('.lister > table > tbody > tr')

for movie in movies:
    movie_title = movie.select_one('.titlecolumn > a').text
    print(movie_title)