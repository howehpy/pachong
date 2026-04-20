from scrapling.spiders import Spider, Response


class QuotesSpider(Spider):
    name = "quotes_spider"
    start_urls = ["https://quotes.toscrape.com/"]

    async def parse(self, response: Response):
        for quote in response.css('.quote'):
            yield {
                "text": quote.css('.text::text').get(),
                "author": quote.css('.author::text').get(),
                "tags": quote.css('.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)


if __name__ == "__main__":
    result = QuotesSpider().start()
    print(f"共抓取 {len(result.items)} 条名言")
    for item in result.items[:5]:
        print(item)
    result.items.to_json('quotes_output.json')
    print("结果已保存到 quotes_output.json")
