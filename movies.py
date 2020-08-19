import boto3
from requests import get
from bs4 import BeautifulSoup
import pandas as pd

def handler(event, context):

    ACCESS_KEY_ID = 'AKIAUPGXYIMMXYPTFWMH'
    ACCESS_SECRET_KEY = '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'
    BUCKET_NAME = 'tinggitecc'
    FILE_NAME = "some_movies_data.csv"

    data = scrape_movies()

    # S3 Connect
    s3 = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY
    )

    # Uploaded File
    s3.Bucket(BUCKET_NAME).put_object(Key=FILE_NAME, Body=data)

def scrape_movies():
	url = 'https://www.imdb.com/search/title/?release_date=2017-01-01,2020-12-31'
	response = get(url)
	soup = BeautifulSoup(response.text, 'html.parser')

	movie_divs = soup.find_all('div', class_ ='lister-item mode-advanced')
	# TO-DO: ALL DONE
	# extract each column of data
	# name of movie(3rd div, inside h3 and a), year release(3rd div, inside span and a classname), imdb rating, metascore, num of votes
	names = []
	years = []
	imdbs = []
	scores = []
	votes = []

	for movie in movie_divs:
    		name = movie.h3.a.text
    		names.append(name)
    		year = movie.h3.find('span', class_ = 'lister-item-year text-muted unbold').text
    		years.append(year)
    		if(movie.strong):
        		imdb = movie.strong.text
        		imdbs.append(imdb)
    		else:
        		imdb = 0
        		imdbs.append(imdb)
    		if(movie.find('span', class_ = 'metascore favorable')):
        		score = movie.find('span', class_ = 'metascore favorable').text
        		scores.append(int(score))
    		else:
        		score = 0
        		scores.append(int(score))
    		if(movie.find('span', attrs = {'name': 'nv'})):
        		vote = movie.find('span', attrs = {'name': 'nv'})['data-value']
        		votes.append(int(vote))
    		else:
        		vote = 0
        		votes.append(vote)

	test_df = pd.DataFrame({
    		'movie': names,
    		'year': years,
    		'imdb': imdbs,
    		'score': scores,
    		'vote': votes
	})
	#test_df.to_csv(r'/Users/s3ns3/Documents/Projects/vuejs/fnd-scraper/movies.csv')
	print(test_df)
	data = test_df.to_csv(index=False)
	return data



