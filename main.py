import bs4
import requests
import Chapter

main_page_html = requests.get('https://laravel.com/docs/').text

sidebar = bs4.BeautifulSoup(main_page_html, 'lxml', parse_only=bs4.SoupStrainer(id='indexed-nav'))
chapters_titles = sidebar.find_all('h2')
# chapters_containers = sidebar.find('ul').find_all('li', recursive=False)

for chapter_number, chapter_title in enumerate(chapters_titles):
    Chapter.save(chapter_title, chapter_number + 1, main_page_html)
