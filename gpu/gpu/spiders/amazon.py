import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['www.amazon.ca']
    start_urls = ['https://www.amazon.ca/s?k=graphics+card+3080&crid=TI694OTJJXR6&sprefix=graphics+card+3080%2Caps%2C111&ref=nb_sb_noss']


    def parse(self, response):
        # Product frame
        products = response.css('div.s-card-container.s-overflow-hidden.aok-relative.s-expand-height.s-include-content-margin.s-latency-cf-section.s-card-border')
        # Iterate through all the products
        for product in products: 
            # Data points
            name = product.css('h2.a-size-mini span.a-size-base-plus::text').get()
            cur_price = product.css('div.a-row span.a-offscreen::text').get()
            orig_price = product.css('div.a-row span.a-text-price span.a-offscreen::text').get()
            shipping = product.css('div.a-row span.a-color-base::text').get()
            link = 'https://www.amazon.ca' + product.css('h2.a-size-mini a.a-link-normal::attr(href)').get()
            # Find brand from string
            first_word = name.split(' ')[0].upper() # Grab the first word in the string
            brand = first_word if first_word in ['MSI', 'ZOTAC', 'ASUS', 'EVGA', 'GIGABYTE', 'NVIDIA'] else ' '

            item = {
                'Brand' : brand,
                'Product Name' : name,
                'Current Price' : cur_price,
                'Original Price' : orig_price,
                'Shipping' : shipping,
                'Link' : link,
            }
            yield item

        # Pagination
        pagination_link = response.css('a.s-pagination-item::attr(href)').get() # Find the link to the next page
        if pagination_link is not None:
            yield response.follow(pagination_link, callback=self.parse)

