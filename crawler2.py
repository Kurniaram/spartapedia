import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient            # Importing pymongo (You have to install the package first)
client = MongoClient('mongodb+srv://kurniaramadhan:ttg3JzFNrL6LJfuq@cluster0.zb9ev.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client.dbsparta                      # Create a db named 'dbsparta'.

# Baca URLnya dan ambil HTMLnya,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

# Kamu akan memulai "scraping" dari data pada halaman ini
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

# Gunakan requests library untuk mendapatkan kode HTML dari link diatas
data = requests.get(url=url, headers=headers)

# library BeautifulSoup memudahkan kita dalam
# menguraikan kode HTML tersebut,
soup = BeautifulSoup(data.text, 'html.parser')

# Menggunakan select
movies = soup.select('.lister > table > tbody > tr')

# Looping pada setiap filmnya
for movie in movies:
    # Pertama, mari kita ambil judul dari filmnya
    movie_title = movie.select_one('.titleColumn > a').text
    # Lalu, mari kita ambil tahun perilisan film tersebut
    year = movie.select_one('.titleColumn > .secondaryInfo').text
    # Mari kita bersihkan juga value dari setiap tahunnya
    # dengan membuang karakter spesial
    year = year.replace('(', '')
    year = year.replace(')', '')
    # Terakhir, Mari kita ambil rating dari tiap-tiap movies
    rating = movie.select_one('.ratingColumn > strong').text
    # ... dan print semua secara berdampingan!
    doc = {
        'movie' : movie_title,
        'year' : year,
        'rating' : rating
    }
    db.movies.insert_one(doc)