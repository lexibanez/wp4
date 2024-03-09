# store urls into a file
def store_urls(urls: list) -> None:
    ''' Stores the urls into a file'''
    with open('urls.txt', 'w') as file:
        for url in urls:
            file.write(url + '\n')


# retrieve urls from a file
def retrieve_urls() -> list:
    ''' Retrieves the urls from a file and returns them as a list of strings'''
    try:
        with open('urls.txt', 'r') as file:
            urls = file.readlines()
            urls = [url.strip() for url in urls]
            return urls
    except FileNotFoundError:
        print('File not found')
        return
