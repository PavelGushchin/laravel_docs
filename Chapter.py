import bs4
import os
import Article

output_dirname = 'LARAVEL DOCS'
os.makedirs(output_dirname, exist_ok=True)


def save(chapter_title, chapter_number, main_page_html):
    a_tags_in_chapter = chapter_title.find_next('ul').find_all('a')

    links_to_articles = []
    for article_a_tag in a_tags_in_chapter:
        if article_a_tag['href'][0] != '/':
            continue
        links_to_articles.append(f'https://laravel.com{article_a_tag["href"]}')

    main_page = bs4.BeautifulSoup(main_page_html, 'lxml')
    main_container = main_page.find(class_='docs_main')
    main_container.clear()

    for article_link in links_to_articles:
        article = Article.get(article_link)
        main_container.extend(article)

    all_link_tags_with_hrefs = main_page.find_all('link', href=True)
    for link_tag in all_link_tags_with_hrefs:
        if link_tag['href'][0] != '/':
            continue
        link_tag['href'] = 'https://laravel.com' + link_tag['href']

    output_filename = f'{output_dirname}/{chapter_number}) {chapter_title.get_text(strip=True)}.html'

    with open(output_filename, 'w') as file:
        file.write(str(main_page))
