# -*- coding: utf-8 -*-
import json
import re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def wait_element(driver, by_content, by=By.ID, timeout=8, to_sleep=0):
    try:
        element_present = EC.presence_of_element_located((by, by_content))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
        pass
        return False
    if to_sleep > 0:
        time.sleep(to_sleep)
    return True


def get_app_data(url):
    dataset = []
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    current_page_driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
    current_page_driver.get(url)

    wait_element(current_page_driver, '//h1/span', by=By.XPATH)
    name = current_page_driver.find_element_by_xpath('//h1/span').text
    wait_element(current_page_driver, "//div[(contains(@aria-label, 'Avaliado') or contains(@aria-label, 'Rated')) and not(@role)]/..", by=By.XPATH)
    box_data = current_page_driver.find_element_by_xpath("//div[(contains(@aria-label, 'Avaliado') or contains(@aria-label, 'Rated')) and not(@role)]/..")
    stars = int(''.join(re.findall(r'\d+', box_data.find_element_by_xpath("./div[1]").text))) / 10
    votes = int(''.join(re.findall(r'\d+', box_data.find_element_by_xpath("./span/span[2]").text)))

    current_page_driver.close()
    record = {'name': name, 'stars': stars, 'votes': votes}
    return record


def scrapy_google_play(url):
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
    driver.get(url)
    whole_dataset = []
    links = driver.find_elements_by_xpath("//h2[text() = 'Apps']/../../../../div[2]/div/c-wiz/div/div/div/div/a")

    for link in links:
        url_app = link.get_attribute('href')
        app_data = get_app_data(url_app)

        whole_dataset.append(app_data)

    driver.close()
    return whole_dataset


url = 'https://play.google.com/store/search?q=.gov.br'
result = scrapy_google_play(url)
with open('data.json', 'w') as fp:
    json.dump(result, fp)
print(result)