import bs4
import requests
from copy import copy


def get(article_link):
    article_html = requests.get(article_link).text
    soup = bs4.BeautifulSoup(article_html, 'lxml', parse_only=bs4.SoupStrainer('body'))

    article_container = soup.find(class_='docs_main')
    all_tags_a = article_container.find_all(href=True)

    for a in all_tags_a:
        if a['href'][0] == '#':
            continue
        a.append(f' (***{a["href"]}***) ')

    br_tag = soup.new_tag('br')
    article_container.append(br_tag)
    article_container.append(copy(br_tag))

    article_tags = [tag for tag in article_container.children if str(tag) != '\n']

    return article_tags
