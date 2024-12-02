from selenium import webdriver
from game import Game

#Keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=chrome_options)

driver.set_window_position(-1000, 0)
driver.maximize_window()

driver.get('https://orteil.dashnet.org/cookieclicker/')

Game(driver).play()

#driver.close()