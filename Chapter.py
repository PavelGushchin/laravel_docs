import bs4
import os
import Article
from copy import copy

output_dirname = 'LARAVEL DOCS'
os.makedirs(output_dirname, exist_ok=True)


def save(chapter_title, chapter_number, main_page_html):
    a_tags_in_chapter = chapter_title.find_next('ul').find_all('a')

    links_to_articles = []
    for article_a_tag in a_tags_in_chapter:
        links_to_articles.append(f'https://laravel.com{article_a_tag["href"]}')

    main_page = bs4.BeautifulSoup(main_page_html, 'lxml')
    main_container = main_page.find(class_='docs_main')
    main_container.clear()

    for article_link in links_to_articles:
        article_container = Article.get_container(article_link)

        for tag in article_container.children:
            if str(tag) == '\n':
                continue
            main_container.append(tag)

        br_tag = main_page.new_tag('br')
        main_container.append(br_tag)
        main_container.append(copy(br_tag))

    output_filename = f'{output_dirname}/{chapter_number}) {chapter_title.get_text(strip=True)}.html'

    with open(output_filename, 'w') as file:
        file.write(str(main_page))
