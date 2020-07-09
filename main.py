# Importing Packages
import selenium
from selenium import webdriver
from save_images import make_directory, save_images
from scrap_images import scrap_image_url
from selenium.common.exceptions import StaleElementReferenceException

# Creating an instance of google chrome
DRIVER_PATH="C:\\Scrape Image\\chromedriver.exe"

# To run chrome in a headfull mode(like regular chrome):
driver=webdriver.Chrome(executable_path=DRIVER_PATH)
current_page_url=driver.get("https://www.amazon.in/s?k=saree&qid=1593704576&ref=sr_pg_1")
DIRNAME="saree"
make_directory(DIRNAME)
start_page=1
total_page=2
# Scraping the Pages
for page in range(start_page,total_page+1):
    try:
        product_details=scrap_image_url(driver=driver)
        print("Scraping Page {0} of {1} Pages".format(page,total_page))

        page_value=driver.find_element_by_xpath("//li[@class='a-selected']").text
        print("The current page scraped is {}".format(page_value))

        #Downloading the images
        save_images(data=product_details, dirname= DIRNAME, page=page)
        print("Scraping of page {0} done".format(page))

    

    except StaleElementReferenceException as Exception:
            print("We are facing an exception")
            exp_page= driver.find_element_by_xpath("//li[@class='a-normal']").text
            print("The page value at the time of exception is {}".format(exp_page))

            value=driver.find_element_by_xpath("//li[@class='a-normal']")
            link= value.get_attribute('href')
            driver.get(link)

            product_details=scrap_image_url(driver=driver)
            print("Scraping Page {0} of {1} pages".format(page_value))

            #Downloading the images
            save_images(data=product_details,dirname=DIRNAME, page=page)
            print("Scraping of page {0} done".format(page))


            button_type= driver.find_element_by_xpath("//div[@class='a-selected']//div[@class='normal']").get_attribute('innerHTML')
            if button_type=='Next':
                driver.find_element_by_xpath("//div[@class='a-selected']").click()
            else:
                driver.find_element_by_xpath("//div[@class='a-selected'][2]").click()

            new_page= driver.find_element_by_xpath("//div[@class='a-selected']").text
            print("The new page is {}".format(new_page))



            
