from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import boto3
import pandas

def handler(event, context):

    ACCESS_KEY_ID = 'AKIAUPGXYIMMXYPTFWMH'
    ACCESS_SECRET_KEY = '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'
    BUCKET_NAME = 'tinggitecc'
    FILE_NAME = "test_lambda.csv"

    data = extract_links()

    # S3 Connect
    s3 = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY 
    )

    # Uploaded File
    s3.Bucket(BUCKET_NAME).put_object(Key=FILE_NAME, Body=data)


def scrape():
    webpage_url = 'http://covid-19.moh.gov.my/terkini/082020/situasi-terkini-14-ogos-2020'
    page = urlopen(webpage_url)
    soup = BeautifulSoup(page, 'html.parser')
   
    for divs in soup.find_all(re.compile('li')):
        print(divs)

def extract_links():
    # TO-DO : To receive user input url
    webpage_url = 'http://covid-19.moh.gov.my/terkini/082020/situasi-terkini-14-ogos-2020'
    page = urlopen(webpage_url)
    soup = BeautifulSoup(page, 'html.parser')
    links = []
    
    for link in soup.find_all('a', attrs={'href': re.compile('^/terkini')}):
        # TO-DO : To receive user input
        links.append('http://covid-19.moh.gov.my' + link.get('href') + '\n')
        #print('http://covid-19.moh.gov.my' + link.get('href'))
    df = pd.DataFrame.from_dict(links)
    data =  links.to_csv(index=False)

    return data
    
       # with open('urls.txt', 'a') as f_out:
       #     for line in links:
       #         f_out.write(line)
        

#scrape()
#extract_links()
