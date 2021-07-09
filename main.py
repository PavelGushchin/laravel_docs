import datetime
import os

from Parser import Site

parsed_site = Site.parse("https://laravel.com/docs/")

output_dir = "LARAVEL DOCS"
output_filename = "LARAVEL MANUAL " + str(datetime.date.today()) + ".html"

os.makedirs(output_dir, exist_ok=True)

with open(output_dir + "/" + output_filename, 'w') as file:
    file.write(parsed_site)
