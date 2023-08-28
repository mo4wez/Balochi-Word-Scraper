from word_scraper import WordScraperBot
from time import sleep


letters = [
    'آ',
    'ا',
    'ب',
    'پ',
    'ت',
    'ٹ',
    'ج',
    'چ',
    'د',
    'ڈ',
    'ر',
    'ز',
    'ژ',
    'س',
    'ش',
    'ک',
    'گ',
    'ل',
    'م',
    'ن',
    'و',
    'ه',
    'ی',
]


if __name__ == '__main__':
    for letter in letters:
        url = f'https://www.webonary.org/balochidictionary/browse/browse-vernacular/?letter={letter}&key=bcc'
        bot = WordScraperBot(base_url=url)
        bot.run()
