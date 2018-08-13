import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myUrl = 'https://www.newegg.com/Product/ProductList.aspx?Submit=StoreIM&Depa=1&Category=38'
uClient = uReq(myUrl)
page_html = uClient.read()
uClient.close()

filename =  "products.csv"
f = open(filename,"w")
headers = "brand, product_name, shipping \n"
f.write(headers)

#parser
page_soup = soup(page_html, "html.parser")
#grab items
containers = page_soup.findAll("div",{"class": "item-container"})

for container in containers:
    brand = container.div.div.a.img["title"]
    title_container = container.findAll("a",{"class":"item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li",{"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    print("brand: "+brand)
    print("product_name: "+product_name)
    print("shipping: "+shipping)

    f.write(brand + ","+product_name.replace(",","|") +","+ shipping+"\n")