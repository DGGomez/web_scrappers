import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myUrl = 'https://www.bell.ca/Bell-bundles'
uClient = uReq(myUrl)
page_html = uClient.read()
uClient.close()

filename =  "bell_bundles.csv"
f = open(filename,"w")
#change this
headers = "brand, product_name, shipping \n"
f.write(headers)

#parser
page_soup = soup(page_html, "html.parser")
#grab items
containers = page_soup.findAll("div",{"class": "rsx-sb-bndl-bundles-bundle col-xs-12 col-md-4"})

for container in containers:
    price = container
    brand = container.div.div.a.img["title"]
    title_container = container.findAll("a",{"class":"item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li",{"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    print("brand: "+brand)
    print("product_name: "+product_name)
    print("shipping: "+shipping)

    f.write(brand + ","+product_name.replace(",","|") +","+ shipping+"\n")