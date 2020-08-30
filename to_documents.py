import newspaper as ns
import boto3

def handler(event, context):

    ACCESS_KEY_ID = 'AKIAUPGXYIMMXYPTFWMH'
    ACCESS_SECRET_KEY = 'OqnPxNLRypT+6zj8GHCKabiQbh3oKIJYaGL6wN97'
    BUCKET_NAME = 'tinggitecc'
    FILE_NAME = "docs_text_sample.txt"

    data = func()

    # S3 Connect
    s3 = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY
    )

    # Uploaded File
    s3.Bucket(BUCKET_NAME).put_object(Key=FILE_NAME, Body=data)

def func():
    url = ns.build('https://newspaper.readthedocs.io/en/latest/', language='en')

    for category in url.category_urls():
        print(category)

    article = url.articles[0]
    article.download()
    article.parse()

    print(article.text)
    return article.text

