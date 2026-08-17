import scrapy

class JumiaSpider(scrapy.Spider):
    name = "jumia"
    allowed_domains = ["jumia.ug"]
    start_urls = ["https://www.jumia.ug/smartphones/"]

    def parse(self, response):
        for product in response.css("article.prd"):
               yield {
                  "name": product.css("h3.name::text, div.name::text").get(),
                  "price": product.css("div.prc::text").get(),
                  "rating": product.css("div.stars._s::text").get(),
                  "url": "https://www.jumia.ug" + product.css("a::attr(href)").get(),
                }

        # Follow next page
        next_page = response.css("a[aria-label='Next Page']::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)
