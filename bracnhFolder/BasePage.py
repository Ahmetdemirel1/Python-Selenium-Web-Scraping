from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time



#========= variables =========
departure_city = "istanbul"
arrival_city = "paris"
week = 6





options = webdriver.ChromeOptions()
#options.add_argument('--headless')
options.add_argument('disable-infobars')
options.add_argument('disable-popup-blocking')
#driver = webdriver.Remote(service.service_url, capabilities)
driver_path = '/Users/sahabt/Desktop/PythonSelenium/web_scraping/driver/chromedriver'
driver = webdriver.Chrome(driver_path, chrome_options=options)
driver.get('https://www.obilet.com/ucak-bileti')



def waiter(sec):
    time.sleep(sec)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



class SearchFlightGetDetail():
    waiter(1)
    from_city = driver.find_element_by_css_selector("#select2-dll-flight-from-container").click()
    write_from_city_name = driver.find_element_by_xpath(".//input[@placeholder='Şehir veya Havalimanı']").send_keys(departure_city)
    waiter(1)
    select_from_city = driver.find_element_by_xpath("//*[@id='select2-dll-flight-from-results']/li[1]").click()
    waiter(5)



    to_city = driver.find_element_by_css_selector("#select2-dll-flight-to-container").click()
    write_to_city_name = driver.find_element_by_xpath(".//input[@placeholder='Şehir veya Havalimanı']").send_keys(arrival_city)
    waiter(1)
    select_to_city = driver.find_element_by_xpath("//*[@id='select2-dll-flight-to-results']/li[1]").click()

    driver.find_element_by_xpath(".//h1[@class='header']").click()


    click_search_button = driver.find_element_by_id("btn-find-flight-ticket").click()
    waiter(10)
    for i in range(week):
        waiter(10)
        wait = WebDriverWait(driver, 10)
        date = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='content']/div/div[4]/div[1]/div/div[1]/div/div[1]/div[2]/span[1]")))
        date_info = date.text
        for count in range(1, 5):
            waiter(5)
            airline_title = driver.find_element_by_xpath(".//div[@class='item row journey'][" + str(count) + "]//div[1]//div//div//span").text
            flight_clock = driver.find_element_by_xpath(".//div[@class='item row journey']["+ str(count) +"]//div[2]//div//div//span").text
            price = driver.find_element_by_xpath(".//div[@class='item row journey']["+ str(count) +"]//div[5]//div[@class='price row notranslate ']//div").text


            print(bcolors.HEADER + "Uçuş bilgileri:" + bcolors.ENDC)
            print("Tarih:" + str(date_info) + bcolors.OKBLUE + "  Firma ismi:" + str(airline_title) + bcolors.OKGREEN + "  Uçuş Saati:" + str(flight_clock) +bcolors.WARNING + "  Fiyat:" + str(price)+ bcolors.ENDC)


        click_next_button = driver.find_element_by_xpath("//*[@id='content']/div/div[4]/div[1]/div/div[1]/div/div[1]/div[3]/a").click()



driver.quit()