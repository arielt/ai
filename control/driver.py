from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import ActionChains

# launch chrome
driver = webdriver.Chrome()

# navigate to the page
driver.get('https://www.wellsfargo.com/')
assert 'Wells Fargo' in driver.title

# focus on login
elem = driver.find_element(By.NAME, "j_username")
elem.send_keys('')

# wait till card span appears and move to it
card_span = WebDriverWait(driver, 3600).until(EC.presence_of_element_located((By.XPATH, '//span[text()="PLATINUM CARD"]')))
ActionChains(driver).move_to_element(card_span).perform()

print('moved to span')

payment_span = WebDriverWait(driver, 3600).until(EC.presence_of_element_located((By.XPATH, '//span[text()="Make Payment"]')))

print('payment appeared')

driver.close()
