import bs4
import requests


def get_content(article_link):
    article_html = requests.get(article_link).text
    article_container = bs4.BeautifulSoup(article_html, 'lxml', bs4.SoupStrainer(class_='docs_main'))

    all_tags_a = article_container.find_all(href=True)

    for a in all_tags_a:
        if a['href'][0] == '#':
            continue
        a.append(f' (***{a["href"]}***) ')

    return article_container.unwrap()
