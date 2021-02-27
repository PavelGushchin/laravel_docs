import bs4
import requests


def get_content(article_link):
    article_page_html = requests.get(article_link).text
    article_page = bs4.BeautifulSoup(article_page_html, 'lxml', parse_only=bs4.SoupStrainer('body'))

    article_container = article_page.find(class_='docs_main')

    # Expanding links, because otherwise we won't see them in our future PDF file
    old_a_tags = article_container.find_all('a', href=True)
    for a in old_a_tags:
        if a['href'].startswith('#'):
            continue
        a.append(f' (***{a["href"]}***) ')

    # Renaming h tags, because we need h1 tag for Chapter Title, but now it's used for Article Title
    rename_tag('h4', 'h5', article_page)
    rename_tag('h3', 'h4', article_page)
    rename_tag('h2', 'h3', article_page)
    rename_tag('h1', 'h2', article_page)

    for i in range(3):
        article_container.append(article_page.new_tag('br'))

    article_content = [tag for tag in article_container.children]

    return article_content


def rename_tag(old_tag_name, new_tag_name, page):
    old_tags = page.find_all(old_tag_name)

    for old_tag in old_tags:
        old_tag.name = new_tag_name
