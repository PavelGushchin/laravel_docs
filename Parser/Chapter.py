from bs4 import BeautifulSoup

from Parser import Page


def parse(chapter, number):
    chapter_title = number + ") " + chapter.get_text(strip=True)

    soup = BeautifulSoup()
    h1_tag = soup.new_tag("h1")
    h1_tag.append(chapter_title)

    main_content = [
        h1_tag,
        soup.new_tag("br"),
        soup.new_tag("br"),
    ]

    pages = chapter.find_next("ul").find_all("a")
    for page in pages:
        if page["href"].startswith("/"):
            page_url = "https://laravel.com" + page["href"]
            page_content = Page.parse(page_url)
            main_content.extend(page_content)

    for i in range(3):
        main_content.append(soup.new_tag("br"))

    return main_content
