import newspaper as ns
import boto3
import requests
import json
import urllib.request

def handler(event, context):

    ACCESS_KEY_ID = 'AKIAUPGXYIMMXYPTFWMH'
    ACCESS_SECRET_KEY = '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'
    BUCKET_NAME = 'tinggitecc'
    FILE_NAME = "news.txt"

    # json.loads(json.dumps(event))
    url = json.loads(json.dumps(event))
    parse = ns.build(url["data"], language='en')
    
    article = parse.articles[0]
    article.download()
    article.parse()

    print(article.text)
    data = article.text



    # return response
    x = {
        "data": article.text
    }

    # S3 Connect
    s3 = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY
    )

    # Uploade File to S3
    s3.Bucket(BUCKET_NAME).put_object(Key=FILE_NAME, Body=data)

    return x["data"]
    
def to_docs():
    # json.loads(json.dumps(event))
    event = { 
        "data": "https://www.malaymail.com/news/malaysia/2020/08/31/malaysia-reports-second-covid-19-death-in-two-days-six-new-cases/1898831", 
        "date": "April20"
    }

    url = json.loads(json.dumps(event))
    print(url["data"])
    parse = ns.build(url["data"], language='zh')
    
    article = parse.articles[0]
    article.download()
    article.parse()

    print(article.text)

    x = {
        "article_text": article.text
    }

    data = json.loads(json.dumps(x))
    print(data)
    return data

def tunnel():
   cmd = 'curl '
   os.system(cmd)
