import requests
from bs4 import BeautifulSoup
import boto3

def handler(event, context):

    cur_dt = "{:%B %d, %Y}".format(datetime.datetime.now())

    ACCESS_KEY_ID = 'AKIAUPGXYIMMXYPTFWMH'
    ACCESS_SECRET_KEY = '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'
    BUCKET_NAME = 'arn:aws:s3:::tinggitecc'
    FILE_NAME = cur_dt + "asapbabi_testing.csv"

    data = scrap_webpage()

    # S3 Connect
    s3 = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        config=Config(signature_version='s3v4')
    )

    # Uploaded File
    s3.Bucket(BUCKET_NAME).put_object(Key=FILE_NAME, Body=data)

def scrap_webpage():
    webpage_url = "http://covid-19.moh.gov.my/terkini/082020/situasi-terkini-14-ogos-2020"
    page = urlopen(webpage_url)
    soup = BeautifulSoup(page, "html.parser")
    
    news_row = soup.find_all('tr', {'class': ['nn']})
    news = []
    for story in news_row:
        news.append(story.find('li').contents[0])

    df = pd.DataFrame.from_dict(news)

    def dataframe_sum_words(words, dataframe):
        summary = []
        for each in words:
            count = df[0].str.count('\\b'+each+'\\b', re.I).sum()
            summary.append([str(each), str(count)])
            summary_df = pd.DataFrame.from_records(summary, columns=['word','count'])
            return summary_df

    summary = dataframe_sum_words([ENTER_WORDS_OF_INTEREST], df)
    write_data = summary.to_csv(index=False)

    return write_data
