from requests import get
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/search/title/?release_date=2017-01-01,2020-12-31'
response = get(url)
soup = BeautifulSoup(response.text, 'html.parser')

movie_divs = soup.find_all('div', class_ ='lister-item mode-advanced')
# TO-DO:
# extract each column of data
# name of movie(3rd div, inside h3 and a), year release(3rd div, inside span and a classname), imdb rating, metascore, num of votes

first_movie = movie_divs[8]
firstmovie_name = first_movie.h3.a.text
firstmovie_year = first_movie.h3.find('span', class_ = 'lister-item-year text-muted unbold').text
firstmovie_imdb = first_movie.strong.text
if(first_movie.find('span', class_ = 'metascore favorable')):
    firstmovie_score = int(first_movie.find('span', class_ = 'metascore favorable').text)
else:
    firstmovie_score = 0
firstmovie_votes = first_movie.find('span', attrs = {'name': 'nv'}).text
