You need to install this packages to use this scrapper:

1) ChromeDriver => https://sites.google.com/a/chromium.org/chromedriver/downloads
2) Selenium => pip install selenium

Configuration

Once you downloaded ChromeDriver you need to place chromeDriver any place you want and add the route where you placed it inside PATH constant in scrapper.py

Usage

This is just a simple scrapper that's the reason it doesn't have any UI, so to use this scrapper there are 2 functions:

findListOfProducts(): With this function you'll find the first page of the list of products in Amazon

Example:
toSearch = "Computer"
findListOfProducts(toSearch)

This will create a file called Computer_List.json with all the products with the Product name and it's URL.

getProductDetail() : With this function you'll get (Product Image, Product Name, Product Description) of the product, this function will create a json file or each product detail.

You can use the file created by findListOfProducts or you can place a simple Amazon detail product URL

Example With File generated by findListOfProducts function:

with open('computer_List.json', 'r') as f:
     computerJson = json.load(f)
     index = 0
     for computerJson in computerJson:
          getProductDetail(computerJson.get("productUrl"), index)
          index += 1
          print(index)


Example using a URL

getProductDetail("https://www.amazon.com/-/es/TC-895-UA92-Desktop-procesador-i5-10400-802-11ax/dp/B088X2YR3X/ref=sr_1_2?dchild=1&keywords=computer&qid=1606705818&sr=8-2")