import requests
from bs4 import BeautifulSoup

from Parser import Chapter


def parse(laravel_site):
    main_page = BeautifulSoup(
        requests.get(laravel_site).text,
        'lxml'
    )

    main_container = main_page.find(id='main-content')
    main_container.clear()

    sidebar = main_page.find(id='indexed-nav')
    chapters = sidebar.find_all('h2')

    for (number, chapter) in enumerate(chapters):
        chapter_content = Chapter.parse(chapter, str(number + 1))

        main_container.extend(chapter_content)

    # Convert <link> tags from relative to absolute
    for link_tag in main_page.find_all('link', href=True):
        if link_tag['href'].startswith('/'):
            link_tag['href'] = 'https://laravel.com' + link_tag['href']

    return str(main_page)
