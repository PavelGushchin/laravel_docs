import bs4
import requests


def get_container(article_link):
    article_html = requests.get(article_link).text
    soup = bs4.BeautifulSoup(article_html, 'lxml', parse_only=bs4.SoupStrainer('body'))

    article_container = soup.find(class_='docs_main')
    all_tags_a = article_container.find_all(href=True)

    for a in all_tags_a:
        if a['href'][0] == '#':
            continue
        a.append(f' (***{a["href"]}***) ')

    return article_container
