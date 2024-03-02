import requests
import lxml.html
import csv
import re
def parse(url):
    source = requests.get(url)
    tree = lxml.html.document_fromstring(source.text)
    text_original = tree.xpath('//*[@id="click_area"]/div//*[@class="original"]/text()')
    text_translate = tree.xpath('//*[@id="click_area"]/div//*[@class="translate"]/text()')
    create_file(url, text_original, text_translate)

def create_file(url, text_original, text_translate):
    file_title = re.split(":|/|.html", url)
    with open(f"{file_title[-2]}.csv", "w", encoding='utf-16') as result:
        write = csv.writer(result)
        for i in range(len(text_original)):
            write.writerow([text_original[i]])
            write.writerow([text_translate[i]])
def main():
    parse('https://www.amalgama-lab.com/songs/a/ariana_grande/yes_and.html')


if __name__ == '__main__':
    main()