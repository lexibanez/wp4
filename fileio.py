# store urls into a file
def store_urls(urls: list) -> None:
    with open('urls.txt', 'w') as f:
        for url in urls:
            f.write(url + '\n')

# retrieve urls from a file
def retrieve_urls() -> list:
    try:
        with open('urls.txt', 'r') as f:
            urls = f.readlines()
            urls = [url.strip() for url in urls]
            return urls
    except FileNotFoundError:
        print('File not found')
        return []

