# store urls into a file
def store_urls(urls: list) -> None:
    with open('urls.txt', 'w') as file:
        for url in urls:
            file.write(url + '\n')

# retrieve urls from a file
def retrieve_urls() -> list:
    try:
        with open('urls.txt', 'r') as file:
            urls = file.readlines()
            urls = [url.strip() for url in urls]
            return urls
    except FileNotFoundError:
        print('File not found')
        return

