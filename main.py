import bs4
import requests
import Volume

main_page_html = requests.get('https://laravel.com/docs/8.x').text

sidebar = bs4.BeautifulSoup(main_page_html, 'lxml', parse_only=bs4.SoupStrainer(id='indexed-nav'))
volumes_all = sidebar.find_all('h2')
# volumes_all = sidebar.find('ul').find_all('li', recursive=False)

for volume_title_tag in volumes_all:
    Volume.save(volume_title_tag)
