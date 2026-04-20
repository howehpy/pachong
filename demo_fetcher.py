from scrapling.fetchers import Fetcher

page = Fetcher.get('https://quotes.toscrape.com/')

quotes = page.css('.quote')
for quote in quotes:
    text = quote.css('.text::text').get()
    author = quote.css('.author::text').get()
    tags = quote.css('.tag::text').getall()
    print(f'作者: {author}')
    print(f'名言: {text}')
    print(f'标签: {", ".join(tags)}')
    print('-' * 60)
