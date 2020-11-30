# import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time
import json


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH) #The Web Browser Will be using
productList = []

# Variables
toSearch = "Phone"


# page source
pageSource = driver.page_source

def findListOfProducts(productToSearch):
     driver.get('https://amazon.com')
     search = driver.find_element_by_id("twotabsearchtextbox") #Searching the input for search
     search.send_keys(productToSearch)   #Typying whaht's gonna search
     search.send_keys(Keys.RETURN) # Pressing Enter to search
     # main = driver.find_elements_by_id("main")
     productsTitle = driver.find_elements_by_css_selector("h2.a-size-mini span.a-color-base")
     productsUrl = driver.find_elements_by_css_selector("h2.a-size-mini a.a-link-normal")

     #Grouping the information
     for (productUrl, productTitle) in zip(productsUrl, productsTitle): 
          productUrlHttps = productUrl.get_attribute("href")
          newProduct = {
               "productName": productTitle.text,
               "productUrl" : productUrlHttps
          }
          print(type(newProduct))
          productList.append(newProduct.copy())


     # print("List of all products", productList)
     listOfProductsInJson = json.dumps(productList)
     print("Json",listOfProductsInJson)

     with open(f'{productToSearch}_List.json', 'w') as f:
          json.dump(productList, f)

     driver.quit()

def getProductDetail(productUrl, fileName):
     driver.get(productUrl)
     productImage = driver.find_elements_by_id("landingImage")
     productTitle = driver.find_elements_by_id("productTitle")
     productDescription = driver.find_elements_by_css_selector("#feature-bullets ul li")
     productDescriptionText = ""
     
     for productDescription in productDescription:
          productDescriptionText = productDescriptionText + productDescription.text

     
     productDescriptionText = productDescriptionText.replace('"', '')
     for (productImage, productTitle) in zip(productImage, productTitle): 
          productImageText = productImage.get_attribute("src")
          newProductDetail = {
               "productImage": productImageText,
               "productName": productTitle.text,
               "productDescription" : productDescriptionText
          }
          # print(newProductDetail)
          # print("Product Description", productDescriptionText)
          newProductDetailJson = json.dumps(newProductDetail)
          print("Json",newProductDetailJson)

          with open(f'{fileName}.json', 'w') as f:
               json.dump(newProductDetail, f)

          # driver.quit()
          


findListOfProducts(toSearch)

#Read the json and scrap the products
with open('computer_List.json', 'r') as f:
     computerJson = json.load(f)
     index = 0
     for computerJson in computerJson:
          getProductDetail(computerJson.get("productUrl"), index)
          index += 1
          print(index)




