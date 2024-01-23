from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


def main():
    running = True
    max_wait_time = 1
    while running:
        all_products = driver.find_elements(By.CSS_SELECTOR, "#products .product")
        not_shown_products = driver.find_elements(
            By.CSS_SELECTOR, "#products .product.toggledOff"
        )
        curr_products = [
            product for product in all_products if product not in not_shown_products
        ]
        cookie.click()
        for product in curr_products:
            product.click()
        # try:
        #     upgrade_element = WebDriverWait(driver, max_wait_time).until(
        #         EC.presence_of_element_located((By.CSS_SELECTOR, "#upgrades div"))
        #     )
        #     upgrade_element.click()
        # except TimeoutException:
        #     print("time run out")


target = "https://orteil.dashnet.org/cookieclicker/"

service = webdriver.ChromeService(executable_path=binary_path, port=8080)
options = webdriver.ChromeOptions()

# options.add_argument("--start-maximized")
options.headless = True
options.binary_location = "/usr/bin/brave-browser-stable"

driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(10)
driver.get(target)
start = driver.find_element(By.CSS_SELECTOR, "div .langSelectButton")
start.click()
time.sleep(1)

cookie = driver.find_element(By.CSS_SELECTOR, "button")
# all_upgrades = driver.find_elements(By.CSS_SELECTOR, "#store #upgrades div")
# for upgrade in all_upgrades:
#     print(upgrade.get_attribute("id"))
# time.sleep(20)
# all_upgrades = driver.find_elements(By.CSS_SELECTOR, "#upgrades div")
# for upgrade in all_upgrades:
#     print(upgrade.get_attribute("id"))
main()
driver.close()
driver.quit()
