from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import ActionChains

# launch chrome
driver = webdriver.Chrome()

# navigate to the page
driver.get('https://www.chase.com/')
assert 'Chase' in driver.title

# Login. Detect input field by unique ID.
card_span = WebDriverWait(driver, 3600).until(EC.element_located_to_be_selected((By.ID, 'userId-text-input-field')))
login = driver.find_element(By.ID, 'userId-text-input-field')
login.send_keys('')
print('focused on login')

# wait till card span appears and move to it
card_span = WebDriverWait(driver, 3600).until(EC.presence_of_element_located((By.XPATH, '//span[text()="PLATINUM CARD"]')))
ActionChains(driver).move_to_element(card_span).perform()
print('moved to span')

payment_span = WebDriverWait(driver, 3600).until(EC.presence_of_element_located((By.XPATH, '//span[text()="Make Payment"]')))

print('payment appeared')

driver.close()
