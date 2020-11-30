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

     with open(f'{toSearch}.json', 'w') as f:
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
          


#Read Files
with open('Computer.json', 'r') as f:
     computerJson = json.load(f)
     index = 0
     for computerJson in computerJson:
          getProductDetail(computerJson.get("productUrl"), index)
          index += 1
          print(index)







# getProductDetail("https://www.amazon.com/-/es/gp/slredirect/picassoRedirect.html/ref=pa_sp_atf_aps_sr_pg1_1?ie=UTF8&adId=A0851361U1ATS988B5I7&url=%2FDL72319-inal%25C3%25A1mbrico-retroiluminada-intercomunicador-insuperable%2Fdp%2FB088BF7ZDL%2Fref%3Dsr_1_1_sspa%3F__mk_es_US%3D%25C3%2585M%25C3%2585%25C5%25BD%25C3%2595%25C3%2591%26dchild%3D1%26keywords%3DPhone%26qid%3D1606698772%26sr%3D8-1-spons%26psc%3D1&qualifier=1606698772&id=8419949052712960&widgetName=sp_atf")
# findListOfProducts(toSearch)
#productsUrl.get_attribute("href") for link

# for productUrl in productsUrl:
#     print(productUrl.get_attribute("href"))

# for index, item in enumerate(productsUrl):
#     print(index, item)

# for productTitle in productsTitle:
#     print(productTitle.text)
# try:
#     main = WeproductTitleDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "main"))
#     )
#     articles = main.find_elements_by_class_name("entry-title")
#     print(productContainer)

#     for article in articles:
#         print(article.text)
# finally:
#     driver.quit()




