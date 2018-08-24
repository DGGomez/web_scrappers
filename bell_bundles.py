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
headers = "name, price \n"
f.write(headers)

#parser
page_soup = soup(page_html, "html.parser")
#grab items
containers = page_soup.findAll("div",{"class": "rsx-sb-bndl-bundles-bundle col-xs-12 col-md-4"})

for container in containers:
    price_container = container.findAll("span", {"class":"rsx-price rsx-bell-font rsx-txt-size-36"})
    price = price_container[0].text + price_container[1].text + price_container[2].text
    title_container = container.findAll("h2",{"class":"rsx-sb-bndl-bundles-bundle-title rsx-caret rsx-caret_bottom rsx-caret_blue"})
    product_name = title_container[0].text

    print("product_name: "+product_name)
    print("price: "+price)

    f.write(product_name + ","+price.replace(",","|")+"\n")
