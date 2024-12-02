from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

class PopupHandler:
    
    def __init__(self,driver:webdriver) -> None:
        self.DRIVER = driver

    def close_popups(self) -> None:
        self.DRIVER.find_element(By.CSS_SELECTOR,'[aria-label="Manage options"]').click()
        self.DRIVER.find_element(By.CSS_SELECTOR,'[aria-label="Confirm choices"]').click()
        sleep(0.4)
        self.DRIVER.find_element(By.CLASS_NAME,'cc_btn_accept_all').click()
        self.DRIVER.find_element(By.ID,'langSelect-EN').click()
        sleep(0.6)
        self.DRIVER.find_element(By.XPATH,'/html/body/div[2]').shadow_root.find_element(By.CLASS_NAME,'ft-reg-bubble-close').click()

    def close_notes(self) -> None:
        while self.DRIVER.find_element(By.ID,'notes').find_elements(By.CSS_SELECTOR,'div[id*=note]'):
            note = self.DRIVER.find_element(By.ID,'notes').find_elements(By.CSS_SELECTOR,'div[id*=note]')[0]
            try:
                note.find_element(By.CSS_SELECTOR,'div.close').click()
            except StaleElementReferenceException:
                print(f'Element {note} has been hidden')
                continue