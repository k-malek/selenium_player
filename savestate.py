from os.path import isfile
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

class SaveStateHandler():
    def __init__(self,driver: webdriver) -> None:
        self.driver=driver

    def save_state(self) -> None:
        self.driver.find_element(By.ID,'prefsButton').click()
        self.driver.find_element(By.XPATH,'//*[@id="menu"]/div[3]/div/div[4]/a[1]').click()
        state=self.driver.find_element(By.ID,'textareaPrompt').text
        with open('savestate.dt','w+',encoding='utf-8') as f:
            f.write(state)
        self.driver.find_element(By.ID,'promptClose').click()
        self.driver.find_element(By.CSS_SELECTOR,'#menu .menuClose').click()

    def load_state(self) -> None:
        state=None
        if isfile('savestate.dt'):
            with open('savestate.dt','r',encoding='utf-8') as f:
                state=f.readline()
        if state:
            self.driver.find_element(By.ID,'prefsButton').click()
            self.driver.find_element(By.XPATH,'//*[@id="menu"]/div[3]/div/div[4]/a[2]').click()
            self.driver.find_element(By.ID,'textareaPrompt').send_keys(state)
            self.driver.find_element(By.ID,'promptOption0').click()
            sleep(0.1)
            self.driver.find_element(By.CSS_SELECTOR,'#menu .menuClose').click()