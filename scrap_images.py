# Scraping image URLs using selenium
def scrap_image_url(driver):
    images= driver.find_elements_by_xpath("//div[@class='a-section aok-relative s-image-tall-aspect']//img[@class='s-image']")

#print(len(images),len(brands), len(product_description),len(prices))

    product_data={}
    product_data["image_urls"]=[]

    
    for image in images[0:100]:
        source= image.get_attribute('src')
        product_data["image_urls"].append(source)
    print("Returning Scraped data")

    return product_data

#driver.close()
           
    
        
            
            
