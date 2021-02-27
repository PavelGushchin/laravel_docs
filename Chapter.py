import Article


def save_to_container(main_container, chapter_title):
    all_a_tags_in_chapter = chapter_title.find_next('ul').find_all('a')

    links_to_articles = []
    for a_tag in all_a_tags_in_chapter:
        if a_tag['href'].startswith('/'):
            links_to_articles.append('https://laravel.com' + a_tag['href'])

    for link_to_article in links_to_articles:
        article_content = Article.get_content(link_to_article)
        main_container.extend(article_content)
