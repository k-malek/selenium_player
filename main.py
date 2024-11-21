from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from popup_utils import PopupHandler

#Keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=chrome_options)

driver.set_window_position(-1000, 0)
driver.maximize_window()

driver.get('https://orteil.dashnet.org/cookieclicker/')

popup_handler=PopupHandler(driver)

popup_handler.close_popups()
sleep(1)
popup_handler.close_notes()

GAME=driver.find_element(By.ID,'game')

#driver.close()