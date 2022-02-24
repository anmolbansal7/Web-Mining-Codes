#Anmol Bansal 19BCE0630
import pandas as pd
import scrapy
class BrickSetSpider(scrapy.Spider):
    name = 'brick_spider'
    #https://www.bewakoof.com
    start_urls = ['https://www.bewakoof.com/sweatshirts-and-hoodies-for-men']

    def parse(self, response):
        SET_SELECTOR = '.productGrid'
        for brickset in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'h3 ::text'
            PRICE_SELECTOR = '///a/div/div[2]/div[2]/span[2]/text()'
            DISCOUNT_SELECTOR = '///a/div/div[2]/div[2]/span[1]/b/text()'
            IMG = 'img ::attr(src)'
            data = {
                'name': brickset.css(NAME_SELECTOR).extract(),
                'price': brickset.xpath(PRICE_SELECTOR).extract(),
                'discount': brickset.xpath(DISCOUNT_SELECTOR).extract(),
                'image': brickset.css(IMG).extract(),
            }
            #print(data)
            df = pd.DataFrame()
            df['name'] = data['name']
            df['price'] = data['price']
            df['finalprice'] = data['discount']
            df['image'] = data['image']
            df['discount'] = df['price'].astype(int) - df['finalprice'].astype(int)
            print(df)
            
