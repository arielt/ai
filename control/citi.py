from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import ActionChains

# launch chrome
driver = webdriver.Chrome()

# navigate to the page
driver.get('https://www.citi.com/')
assert 'Citi' in driver.title

# login, detect input field by unique ID
print('looking for username element')
card_span = WebDriverWait(driver, 3600).until(EC.presence_of_element_located((By.ID, 'username')))
login = driver.find_element(By.ID, 'username')
login.send_keys('')
print('focused on login')

# review transactions
transaction_tile = WebDriverWait(driver, 3600).until(EC.presence_of_element_located((By.ID, 'ums-transaction-tile')))
ActionChains(driver).move_to_element(transaction_tile).perform()
print('moved to transactions')

payment_span = WebDriverWait(driver, 3600).until(EC.presence_of_element_located((By.ID, 'dummy')))

print('dummy wait is over')

driver.close()
