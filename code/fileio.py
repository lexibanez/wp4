"""
This module contains functions to store and retrieve URLs from a file.
The `store_urls` function takes a list of URLs and writes them to a file.
The `retrieve_urls` function reads the URLs from the file and returns
them as a list.
"""


# store urls into a file
def store_urls(urls: list) -> None:
    ''' Stores the urls into a file'''
    with open('urls.txt', 'w', encoding='utf-8') as file:
        for url in urls:
            file.write(url + '\n')


# retrieve urls from a file
def retrieve_urls() -> list:
    ''' Retrieves the urls from a file and returns them as a list of strings'''
    try:
        with open('urls.txt', 'r', encoding='utf-8') as file:
            urls = file.readlines()
            urls = [url.strip() for url in urls]
            return urls
    except FileNotFoundError:
        print('File not found')
        return None
