import requests
from bs4 import BeautifulSoup


def login():
    print('login....')
    datas = {
        'username': 'user',
        'password': 'user12345'
    }

    res = requests.post('http://167.172.70.208:9999/login', data=datas)

    f = open('./res.html', 'w+')
    f.write(res.text)
    f.close()

def get_urls():
    print('getting urls.....')

def get_detail():
    print('getting detail....')

def create_csv():
    print('csv generated....')

def run():
    login()
    get_urls()
    get_detail()
    create_csv()
