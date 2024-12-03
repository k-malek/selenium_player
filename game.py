from time import sleep
from popup_utils import PopupHandler
from savestate import SaveStateHandler
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

class Game():

    CLICKS_PER_CYCLE = 100

    def __init__(self, driver:webdriver) -> None:
        self.driver=driver
        self.popup_handler = PopupHandler(self.driver)
        self.savestate_handler = SaveStateHandler(self.driver)

    def setup_game(self) -> None:
        self.popup_handler.close_popups()
        sleep(1)
        self.popup_handler.close_notes()
        self.load_state()

    def click_cookie(self,extended=False) -> None:
        clicks_amount=Game.CLICKS_PER_CYCLE * 10 if extended else Game.CLICKS_PER_CYCLE
        for _ in range(clicks_amount):
            try:
                self.driver.find_element(By.ID,'bigCookie').click()
                self.click_golden_cookie()
            except ElementClickInterceptedException:
                break

    def pick_products(self) -> None:
        while True:
            products = self.driver.find_element(By.ID,'products').find_elements(By.CSS_SELECTOR,'div.enabled')
            if products:
                products[-1].click()
            else:
                break        

    def pick_upgrade(self) -> None:
        upgrades = self.driver.find_element(By.ID,'upgrades').find_elements(By.CSS_SELECTOR,'div.enabled')
        if upgrades:
            upgrades[-1].click()

    def click_golden_cookie(self) -> None:
        golden_cookie = self.driver.find_element(By.ID,'goldenCookie').find_elements(By.CSS_SELECTOR,'div')
        if golden_cookie:
            golden_cookie[0].click()

    def save_state(self) -> None:
        self.savestate_handler.save_state()

    def load_state(self) -> None:
        self.savestate_handler.load_state()

    def play(self):
        self.setup_game()
        i=0
        while True:
            self.click_cookie(i==9)
            self.pick_upgrade()
            self.pick_products()
            self.popup_handler.close_notes()
            if i==9:
                self.save_state()
            i=i+1 if i<9 else 0