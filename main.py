from selenium import webdriver
from game import Game

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://orteil.dashnet.org/cookieclicker/')

Game(driver).play()
