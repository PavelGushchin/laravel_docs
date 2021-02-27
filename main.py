import os

import bs4
import requests

import Chapter

main_page_html = requests.get('https://laravel.com/docs/').text
main_page = bs4.BeautifulSoup(main_page_html, 'lxml')

main_container = main_page.find(class_='docs_main')
main_container.clear()

sidebar = bs4.BeautifulSoup(main_page_html, 'lxml', parse_only=bs4.SoupStrainer(id='indexed-nav'))
chapters_titles = sidebar.find_all('h2')

for chapter_number, chapter_title in enumerate(chapters_titles):
    new_h1_tag = main_page.new_tag('h1')
    new_h1_tag.append(f'{chapter_number + 1}) {chapter_title.get_text(strip=True)}')
    main_container.append(new_h1_tag)

    for i in range(2):
        main_container.append(main_page.new_tag('br'))

    Chapter.save_to_container(main_container, chapter_title)

    for i in range(3):
        main_container.append(main_page.new_tag('br'))

possibly_broken_link_tags = main_page.find_all('link', href=True)
for link_tag in possibly_broken_link_tags:
    if link_tag['href'].startswith('/'):
        link_tag['href'] = 'https://laravel.com' + link_tag['href']


output_dirname = 'LARAVEL DOCS'
os.makedirs(output_dirname, exist_ok=True)

with open(f'{output_dirname}/LARAVEL MANUAL.html', 'w') as file:
    file.write(str(main_page))
