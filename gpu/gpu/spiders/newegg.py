import scrapy


class GpuSpiderSpider(scrapy.Spider):
    name = 'newegg'
    allowed_domains = ['www.newegg.ca']
    start_urls = ['https://www.newegg.ca/p/pl?d=graphics+card+3080']

    
    def parse(self, response):
        products = response.css('div.item-cell')
        for product in products:
            # Data Points
            name = product.css('a.item-title::text').get()
            cur_price = '$' + product.css('li.price-current strong::text').get() + product.css('li.price-current sup::text').get()
            orig_price = product.css('span.price-was-data::text').get()
            shipping = product.css('li.price-ship::text').get()
            link = product.css('div.item-container a::attr(href)').get()
            # Find product brand from string
            first_word = name.split(' ')[0].upper()
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
