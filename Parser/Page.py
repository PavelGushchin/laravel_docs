import requests
from bs4 import BeautifulSoup


def parse(page_url):
    soup = BeautifulSoup(
        requests.get(page_url).text,
        "lxml",
    )

    page = soup.find(id="main-content")

    # Expanding links, because otherwise we won't see them in our future PDF file
    for a in page.find_all("a", href=True):
        if a["href"].startswith("#"):
            continue
        a.append(f" (***{a['href']}***) ")

    # Renaming h tags, because we need h1 tag for Chapter title, but now it's used for Page title
    rename_tag('h4', 'h5', page)
    rename_tag('h3', 'h4', page)
    rename_tag('h2', 'h3', page)
    rename_tag('h1', 'h2', page)

    for i in range(3):
        page.append(soup.new_tag("br"))

    return page.contents


def rename_tag(old_tag_name, new_tag_name, page):
    old_tags = page.find_all(old_tag_name)

    for old_tag in old_tags:
        old_tag.name = new_tag_name
