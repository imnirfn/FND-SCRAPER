import newspaper as ns
from newspaper import Article
url = ns.build('https://newspaper.readthedocs.io/en/latest/', language='en')

for category in url.category_urls():
    print(category)

article = url.articles[0]
article.download()
article.parse()

print(article.text)


