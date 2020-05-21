from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import sys

### setting up webbrower
dir_path = os.path.dirname(os.path.realpath(__file__))
options = webdriver.ChromeOptions()
prefs = {'download.default_dir' : '%s/STOCKFILE'%dir_path}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome()

### using tickers from tickers.txt to create a list of links
urls = list()
with open('tickersR.txt','r') as ticker_file:
    tickers = ticker_file.readline().split(" ")
    urls = ["https://finance.yahoo.com/quote/%s/history?period1=1589155200&period2=1589241600&interval=1d&filter=history&frequency=1d"%ticker for ticker in tickers]

print("*****Created *****\n %s"%urls)
### use the list to loop through the site
brokenlinks = list()
for url in urls:
    try:
        print('Starting on %s'%url)
        driver.get(url)

        ### selecting the max time period and click apply
        print('sleeping 2sec')
        timeperiodButton = driver.find_element_by_xpath("//span[@class='C($linkColor) Fz(14px)']")
        timeperiodButton.click()

        time.sleep(2)
        print('sleeping 2sec')
        maxButton = driver.find_element_by_xpath("//span[contains(text(),'Max')]")
        maxButton.click()
        print('Applying MAX DAYS')

        time.sleep(2)
        print('sleeping 2sec')
        applyButton = driver.find_element_by_xpath("//span[contains(text(),'Apply')]")
        applyButton.click()
        time.sleep(2)
        print('sleeping 2sec')

        ### click download
        downloadButton = driver.find_element_by_xpath('//span[contains(text(),\'Download\')]')
        downloadButton.click()
        time.sleep(2)
    except:
        with open('brokenlinks.txt','a+') as broken:
            broken.write(url)
        brokenlinks.append(url)

driver.close()