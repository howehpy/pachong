from scrapling.fetchers import StealthyFetcher

page = StealthyFetcher.fetch('https://quotes.toscrape.com/', headless=True)

quotes = page.css('.quote')
for quote in quotes[:3]:
    text = quote.css('.text::text').get()
    author = quote.css('.author::text').get()
    print(f'作者: {author}')
    print(f'名言: {text}')
    print('-' * 60)
