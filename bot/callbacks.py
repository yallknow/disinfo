from bot.chatting import *
from bot.commands import *
from bot.definitions import *
from bot.flags import *
from bot.responses import *

from bs4 import BeautifulSoup
from typing import Iterable

import itertools
import re
import requests


def reply_or_response(bot, message, parameters: Iterable[str], response_data: str) -> None:
    if REPLY_FLAG in parameters:
        reply(bot, message, response_data)
        return

    response(bot, message, response_data)


def send_all_or_some(bot, message, parameters: Iterable[str], news: dict) -> None:
    size = len(news)

    if NUMBER_FLAG in parameters:
        try:
            n = int(parameters[parameters.index(NUMBER_FLAG) + 1])

            if n > len(news):
                raise

            size = n
        except:
            reply_or_response(bot, message, parameters, PARSING_ERROR)
            reply_or_response(bot, message, parameters,
                              INVALID_NUMBER_PARAMETER)

    for i in range(0, size, NEWS_CHUNK_SIZE):
        chunk = dict(itertools.islice(news.items(), i,
                     i + min(size, NEWS_CHUNK_SIZE)))
        size -= NEWS_CHUNK_SIZE
        result = ''.join('\n\n'.join(
            item + '\n' + chunk[item] for item in chunk))
        reply_or_response(bot, message, parameters, result)


def bbc(bot, message, parameters: Iterable[str]) -> None:
    URL = 'https://www.bbc.com'

    if FUTURE_FLAG in parameters:
        send_all_or_some(bot, message, parameters,
                         bbc_future_news(URL, '/future'))
        return

    if SPORT_FLAG in parameters:
        send_all_or_some(bot, message, parameters,
                         bbc_sport_news(URL, '/sport'))
        return

    if TRAVEL_FLAG in parameters:
        send_all_or_some(bot, message, parameters,
                         bbc_travel_news(URL, '/travel'))
        return

    send_all_or_some(bot, message, parameters, bbc_default_news(URL))


def bbc_default_news(url: str) -> dict:
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    blocks = soup.find_all(class_='block-link__overlay-link')

    news = {}

    for block in blocks:
        news[block.string.strip()] = block['href']

        if not url in block['href']:
            news[block.string.strip()] = url + block['href']

    return news


def bbc_future_news(url: str, url_postfix: str) -> dict:
    page = requests.get(url + url_postfix).text
    soup = BeautifulSoup(page, 'html.parser')
    blocks = soup.find_all(class_='article-hero__content-title')

    news = {}

    for block in blocks:
        news[block.a.div.text.strip()] = url + block.a['href']

    blocks = soup.find_all(class_='article-title-card-rectangle__link')

    for block in blocks:
        if block.h2:
            news[block.h2.string.strip()] = url + block['href']

    blocks = soup.find_all(class_='rectangle-story-item__container')

    for block in blocks:
        news[block.a.span.string.strip()] = url + block.a['href']

    blocks = soup.find_all(class_='most-popular-item__content')

    for block in blocks:
        news[block.a.h2.string.strip()] = url + block.a['href']

    return news


def bbc_sport_news(url: str, url_postfix: str) -> dict:
    page = requests.get(url + url_postfix).text
    soup = BeautifulSoup(page, 'html.parser')
    blocks = soup.find_all(class_=re.compile('PromoLink'))

    news = {}

    for block in blocks:
        if block['href'].startswith(url_postfix):
            news[block.find(class_=re.compile('PromoHeadline')
                            ).span.string.strip()] = url + block['href']

    return news


def bbc_travel_news(url: str, url_postfix: str) -> dict:
    page = requests.get(url + url_postfix).text
    soup = BeautifulSoup(page, 'html.parser')
    blocks = soup.find_all(class_='article-title-card-rectangle__link')

    news = {}

    for block in blocks:
        if block.h2:
            news[block.h2.string.strip()] = url + block['href']

    blocks = soup.find_all(class_='rectangle-story-item__container')

    for block in blocks:
        news[block.a.span.string.strip()] = url + block.a['href']

    blocks = soup.find_all(class_='most-popular-item__content')

    for block in blocks:
        news[block.a.h2.string.strip()] = url + block.a['href']

    return news


def help(bot, message, parameters: Iterable[str]) -> None:
    reply_or_response(bot, message, parameters, VALID_COMMANDS_PREFIX +
                      '`' + '` , `'.join(VALID_COMMANDS) + '`')


def nbcnews(bot, message, parameters: Iterable[str]) -> None:
    URL = 'https://www.nbcnews.com'
    send_all_or_some(bot, message, parameters, nbcnews_default_news(URL))


def nbcnews_default_news(url: str) -> dict:
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    blocks = soup.find_all(
        class_='tease-card__headline tease-card__title tease-card__title--news relative')

    news = {}

    for block in blocks:
        if not '/specials/' in block.a['href']:
            news[block.a.span.string.strip()] = block.a['href']

    blocks = soup.find_all(class_='styles_headline__ice3t')

    for block in blocks:
        news[block.a.string.strip()] = block.a['href']

    return news


def nytimes(bot, message, parameters: Iterable[str]) -> None:
    URL = 'https://www.nytimes.com'

    if ART_FLAG in parameters:
        send_all_or_some(bot, message, parameters, nytimes_news(
            URL, '/section/arts', ['css-1w1ypee', 'css-1cn8d5g']))
        return

    if SPORT_FLAG in parameters:
        send_all_or_some(bot, message, parameters, nytimes_news(
            URL, '/section/sports', ['css-6i5eci', 'css-6i5eci', 'css-qrzo5d']))
        return

    if TRAVEL_FLAG in parameters:
        send_all_or_some(bot, message, parameters, nytimes_news(
            URL, '/section/travel', ['css-b8r11n', 'css-jkrs50', 'css-1cn8d5g']))
        return

    send_all_or_some(bot, message, parameters, nytimes_default_news(URL))


def nytimes_default_news(url: str) -> dict:
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    blocks = soup.find_all(class_='story-wrapper')

    NEWS_PREFIX = '/20'
    news = {}

    for block in blocks:
        title = block.find(class_='indicate-hover')
        link = block.find('a')

        if title and link and NEWS_PREFIX in link['href']:
            news[title.string.strip()] = link['href']

    return news


def nytimes_news(url: str, url_postfix: str, classes: Iterable[str]) -> dict:
    page = requests.get(url + url_postfix).text
    soup = BeautifulSoup(page, 'html.parser')
    blocks = soup.find_all(class_=classes)

    news = {}

    for block in blocks:
        news[block.a.string.strip()] = url + block.a['href']

    return news


def start(bot, message, parameters: Iterable[str]) -> None:
    reply_or_response(bot, message, parameters, START_INFO)
    reply_or_response(bot, message, parameters, HELP_INFO)


def watch(bot, message, parameters: Iterable[str]) -> None:
    pass


def unwatch(bot, message, parameters: Iterable[str]) -> None:
    pass
