from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# launch chrome
driver = webdriver.Chrome()

# navigate to the page
driver.get('https://www.wellsfargo.com/')
assert 'Wells Fargo' in driver.title

# focus on login
elem = driver.find_element(By.NAME, "j_username")
elem.send_keys('')

# move cursor to the card button
wait = WebDriverWait(driver, 3600)
cc_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'PLATINUM CARD')));

print('clicked')

driver.close()
