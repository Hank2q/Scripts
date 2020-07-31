import requests
from bs4 import BeautifulSoup
import os

html = requests.get('https://www.merriam-webster.com/word-of-the-day').text

soup = BeautifulSoup(html, 'html.parser')

word = soup.select_one('body > div.outer-container > div > div.main-wrapper.clearfix > main > article > div.article-header-container.wod-article-header > div.quick-def-box > div.word-header > div > h1').text

word_type = soup.select_one('body > div.outer-container > div > div.main-wrapper.clearfix > main > article > div.article-header-container.wod-article-header > div.quick-def-box > div.word-attributes > span.main-attr').text


definitions = soup.select('body > div.outer-container > div > div.main-wrapper.clearfix > main > article > div.lr-cols-area.clearfix.sticky-column > div.left-content > div > div.wod-definition-container > p')
definitions ='\n'.join([defen.text for defen in definitions])

examples_frame = soup.find('div', class_='wotd-examples')
example = examples_frame.find('p').text
highlight = f'[{word}]'.join(example.split(word))

msg = f'''\
[{word.capitalize()}] 
-{word_type}

{definitions}

{highlight}
'''
print(msg)
save = input('Save word? [Y/N]: ')
if save.lower() == 'y':
    with open(r"C:\Users\HASSANIN\Documents\words_of_days.txt", 'a') as f:
        f.write(msg)
        f.write('_'* 90)
        f.write('\n')
