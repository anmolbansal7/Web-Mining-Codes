# Anmol Bansal 19BCE0630
import requests
from bs4 import BeautifulSoup
import csv
# https://www.bewakoof.com
URL = "https://www.bewakoof.com/sweatshirts-and-hoodies-for-men"
r = requests.get(URL)
# For printing the HTML Content
# print(r.content)

soup = BeautifulSoup(r.content, 'html5lib')
# Parsing the HTML Content in DOM
# print(soup.prettify())

hoodies = []

table = soup.find('div', attrs={'class': 'productGrid'})

for row in table.findAll('div', attrs={'class': 'productCardBox'}):
    hoodie = {}
    hoodie['name'] = row.h3.text
    price = row.find('span', attrs={'class': 'actualPriceText'})
    hoodie['price'] = price.text
    # Discount was shown directly by final price, so I converted it
    discount = int(price.text) - int(row.b.text)
    hoodie['discount'] = discount
    hoodie['image'] = row.img['src']
    hoodies.append(hoodie)

# Storing the data in csv file
filename = 'hoodies.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f, ['name', 'price', 'discount', 'image'])
    w.writeheader()
    for hoodie in hoodies:
        w.writerow(hoodie)