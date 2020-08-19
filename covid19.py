from requests import get
from bs4 import BeautifulSoup

def situasi_terkini():
    url = 'http://covid-19.moh.gov.my/terkini/082020/situasi-terkini-15-ogos-2020'
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    cv_data = []

    cases_divs = soup.find('div', class_ = 'e-content')

    print(cases_divs.ul.text)

def malaysia_cases():
    url = 'https://www.google.com/search?client=firefox-b-d&q=covid+cases#wptab=s:H4sIAAAAAAAAAONgVuLVT9c3NMwySk6OL8zJecTozS3w8sc9YSmnSWtOXmO04eIKzsgvd80rySypFNLjYoOyVLgEpVB1ajBI8XOhCvHsYuL2SE3MKckILkksKV7Eyp2cX5aZopCcWJxaDACL0InvewAAAA'
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    divs = soup.find('div', class_ = 'vnLNtd mnr-c P6OZi V14nKc ptcLIOszQJu__wholepage-card wp-ms')
    print(type(divs))

malaysia_cases()
#situasi_terkini()


