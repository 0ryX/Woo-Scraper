from requests_html import HTMLSession
import csv

url = 'https://barefootbuttons.com/product-category/version-1/'

s = HTMLSession()


def get_links(url):
    r = s.get(url)
    items = r.html.find('div.product-small.box')
    links = []
    for item in items:
        links.append(item.find('a', first=True).attrs['href'])

    return links

def get_products(link):
    r= s.get(link)

    title = r.html.find('h1', first=True).full_text
    price = r.html.find('span.woocommerce-Price-amount.amount bdi')[1].full_text
    sku = r.html.find('span.sku', first=True).full_text
    tag = r.html.find('a[rel=tag]', first=True).full_text

    product = {
        'title': title.strip(),
        'price': price.strip(),
        'sku': sku.strip(),
        'tag': tag.strip()
    }
    print(product)
    return product
    
    print(title,price)

links = get_links(url)
results = []

for link in links:
    results.append(get_products(link))

with open('results.csv', 'w', encoding='utf8', newline='') as f:
    wr = csv.DictWriter(f, fieldnames=results[0].keys(),)
    wr.writeheader()
    wr.writerows(results)


