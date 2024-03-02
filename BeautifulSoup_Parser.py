from bs4 import BeautifulSoup
import requests

def parse(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'lxml')
    div = soup.find('div', id='question-mini-list')
    a = div.find_all('a', class_="s-link")
    create_file(url, a)

def create_file(url, a):
    with open("topics.doc", "w", encoding='utf-16') as doc:
        for i in a:
            result = i.text, url+i.get('href')
            doc.write(str(result))

def main():
    parse('https://ru.stackoverflow.com')


if __name__ == '__main__':
    main()

