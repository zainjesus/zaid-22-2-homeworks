from pprint import pprint
from bs4 import BeautifulSoup as BS

import requests

# Фильмы
film_horror = "https://rezka.ag/films/horror/"
film_fiction = "https://rezka.ag/films/fiction/"
film_action = "https://rezka.ag/films/action/"
film_detective = "https://rezka.ag/films/detective/"

# Сериалы
serial_horror = "https://rezka.ag/series/horror/"
serial_fantasy = "https://rezka.ag/series/fantasy/"
serial_action = "https://rezka.ag/series/action/"
serial_detective = "https://rezka.ag/series/detective/"

# Аниме
anime_senen = "https://rezka.ag/animation/shounen/"
anime_mystery = "https://rezka.ag/animation/mystery/"
anime_drama = "https://rezka.ag/animation/drama/"
anime_detective = "https://rezka.ag/animation/detective/"

# Мультфильмы
cartoon_fairy = "https://rezka.ag/cartoons/fairytale/"
cartoon_fiction = "https://rezka.ag/cartoons/fiction/"
cartoon_comedy = "https://rezka.ag/cartoons/comedy/"
cartoon_soviet = "https://rezka.ag/cartoons/soyzmyltfilm/"





HEADERS = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 YaBrowser/22.9.3.888 Yowser/2.5 Safari/537.36"
}


def get_html(url, params=''):
    req = requests.get(url=url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='b-content__inline_item')
    movie = []
    for item in items:
        info = item.find('div', class_="b-content__inline_item-link").find('div').getText().split(', ')
        movie.append({
            'title': item.find('div', class_="b-content__inline_item-link").find('a').getText(),
            'link': item.find('div', class_="b-content__inline_item-link").find('a').get('href'),
            'length': item.find('span', class_='info').getText()
            if item.find('span', class_='info') is not None else "Фильм",
            'year': info[0],
            'country': info[1],
        })

    return movie


def get_horror():
    html = get_html(film_horror)
    if html.status_code == 200:
        horror = []
        for i in range(1, 2):
            html = get_html(f"{film_horror}page/{i}/")
            current_page = get_data(html.text)
            horror.extend(current_page)
        return horror
    else:
        raise Exception("Error in parser1!!!")


def get_fiction():
    html = get_html(film_fiction)
    if html.status_code == 200:
        fiction = []
        for i in range(1, 2):
            html = get_html(f"{film_fiction}page/{i}/")
            current_page = get_data(html.text)
            fiction.extend(current_page)
        return fiction
    else:
        raise Exception("Error in parser1!!!")


def get_action():
    html = get_html(film_action)
    if html.status_code == 200:
        action = []
        for i in range(1, 2):
            html = get_html(f"{film_action}page/{i}/")
            current_page = get_data(html.text)
            action.extend(current_page)
        return action
    else:
        raise Exception("Error in parser1!!!")


def get_detective():
    html = get_html(film_detective)
    if html.status_code == 200:
        anime = []
        for i in range(1, 2):
            html = get_html(f"{film_detective}page/{i}/")
            current_page = get_data(html.text)
            anime.extend(current_page)
        return anime
    else:
        raise Exception("Error in parser1!!!")


def get_horror_serial():
    html = get_html(serial_horror)
    if html.status_code == 200:
        anime = []
        for i in range(1, 2):
            html = get_html(f"{serial_horror}page/{i}/")
            current_page = get_data(html.text)
            anime.extend(current_page)
        return anime
    else:
        raise Exception("Error in parser1!!!")


def get_fantasy():
    html = get_html(serial_fantasy)
    if html.status_code == 200:
        anime = []
        for i in range(1, 2):
            html = get_html(f"{serial_fantasy}page/{i}/")
            current_page = get_data(html.text)
            anime.extend(current_page)
        return anime
    else:
        raise Exception("Error in parser1!!!")


def get_action_serial():
    html = get_html(serial_action)
    if html.status_code == 200:
        anime = []
        for i in range(1, 2):
            html = get_html(f"{serial_action}page/{i}/")
            current_page = get_data(html.text)
            anime.extend(current_page)
        return anime
    else:
        raise Exception("Error in parser1!!!")


def get_detective_serial():
    html = get_html(serial_detective)
    if html.status_code == 200:
        anime = []
        for i in range(1, 2):
            html = get_html(f"{serial_detective}page/{i}/")
            current_page = get_data(html.text)
            anime.extend(current_page)
        return anime
    else:
        raise Exception("Error in parser1!!!")


def get_senen():
    html = get_html(anime_senen)
    if html.status_code == 200:
        anime = []
        for i in range(1, 2):
            html = get_html(f"{anime_senen}page/{i}/")
            current_page = get_data(html.text)
            anime.extend(current_page)
        return anime
    else:
        raise Exception("Error in parser1!!!")


def get_mystery():
    html = get_html(anime_mystery)
    if html.status_code == 200:
        anime = []
        for i in range(1, 2):
            html = get_html(f"{anime_mystery}page/{i}/")
            current_page = get_data(html.text)
            anime.extend(current_page)
        return anime
    else:
        raise Exception("Error in parser1!!!")


def get_drama():
    html = get_html(anime_drama)
    if html.status_code == 200:
        anime = []
        for i in range(1, 2):
            html = get_html(f"{anime_drama}page/{i}/")
            current_page = get_data(html.text)
            anime.extend(current_page)
        return anime
    else:
        raise Exception("Error in parser1!!!")


def get_detective_anime():
    html = get_html(anime_detective)
    if html.status_code == 200:
        anime = []
        for i in range(1, 2):
            html = get_html(f"{anime_detective}page/{i}/")
            current_page = get_data(html.text)
            anime.extend(current_page)
        return anime
    else:
        raise Exception("Error in parser1!!!")


def get_fairy():
    html = get_html(cartoon_fairy)
    if html.status_code == 200:
        anime = []
        for i in range(1, 2):
            html = get_html(f"{cartoon_fairy}page/{i}/")
            current_page = get_data(html.text)
            anime.extend(current_page)
        return anime
    else:
        raise Exception("Error in parser1!!!")


def get_fiction_cartoon():
    html = get_html(cartoon_fiction)
    if html.status_code == 200:
        anime = []
        for i in range(1, 2):
            html = get_html(f"{cartoon_fiction}page/{i}/")
            current_page = get_data(html.text)
            anime.extend(current_page)
        return anime
    else:
        raise Exception("Error in parser1!!!")


def get_comedy():
    html = get_html(cartoon_comedy)
    if html.status_code == 200:
        anime = []
        for i in range(1, 2):
            html = get_html(f"{cartoon_comedy}page/{i}/")
            current_page = get_data(html.text)
            anime.extend(current_page)
        return anime
    else:
        raise Exception("Error in parser1!!!")


def get_soviet():
    html = get_html(cartoon_soviet)
    if html.status_code == 200:
        anime = []
        for i in range(1, 2):
            html = get_html(f"{cartoon_soviet}page/{i}/")
            current_page = get_data(html.text)
            anime.extend(current_page)
        return anime
    else:
        raise Exception("Error in parser1!!!")



