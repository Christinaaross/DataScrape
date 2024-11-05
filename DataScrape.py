# data_scraper.py
import requests
from bs4 import BeautifulSoup
import time
import random

headers = {
    #mimic real browser
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}

def get_product_data(url):
    #Send request to webpage
    session = requests.Session()
    response = requests.get(url, headers=headers)
    # checking if successful by html 200 status code
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        price = soup.select_one('[class*="price"]').get_text(strip=True) if soup.select_one('[class*="price"]') else 'N/A'
        # inspect page you want to extract from 

     # need to return the data we just got
        return{
         "price": price
         #"rating": rating
        }
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None
    
urls = [
    
        "https://fehaute.com/products/lapel-collar-regular-fit-tweed-urban-buckle-tweed-jacket-16330240?variant=4305910"
        #"https://www.nordstrom.com/s/plaid-wool-blend-reefer-coat/8006953?origin=category-personalizedsort&breadcrumb=Home%2FWomen%2FClothing%2FCoats%20%26%20Jackets&color=001"
         # Big brands like nordstrom are more difficult to do Status code 429(You not getting in)
    ]

all_product_data = []

for url in urls:
    product_data = get_product_data(url)
    if product_data:
        all_product_data.append(product_data)
    # Pause between requests to avoid getting flagged
    time.sleep(random.uniform(5, 10))
#random time bwteen 5 and 10 seconds

# Display gathered data
for product in all_product_data:
    print(product)

    # output: {'price': '$199'}