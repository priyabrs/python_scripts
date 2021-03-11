from bs4 import BeautifulSoup
import requests

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')

soup = BeautifulSoup(response.text, 'html.parser')
film_tag_list = [film_text.getText() for film_text in soup.find_all(name='h3', class_ = 'title')]
# with open('100_films.txt', 'w') as film_file:

# for film_text in soup.find_all(name='h3', class_ = 'title'):
# replace 12th number movie
film_tag_list[-12] = '12) The Godfather Part II'
film_num_list = []
film_title_list = []
for film_tag in film_tag_list:
    film_num_list.append(int(film_tag.split(')')[0]))
    film_title_list.append(film_tag.split(')')[1])

film_sorted = sorted(dict(zip(film_num_list, film_title_list)).items())

with open('100_Films.txt', 'w') as film_file:
    for item in film_sorted:
        film_file.write(f'{item[0]}: {item[1]}\n')

    

