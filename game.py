from time import sleep

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By

from popup_utils import PopupHandler
from savestate import SaveStateHandler


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

    def click_cookie(self,extended:bool=False) -> None:
        clicks_amount=Game.CLICKS_PER_CYCLE * 10 if extended else Game.CLICKS_PER_CYCLE
        for _ in range(clicks_amount):
            try:
                self.driver.find_element(By.ID,'bigCookie').click()
                self.click_golden_cookie()
            except ElementClickInterceptedException:
                break

    def get_upgrade(self,source:str) -> None:
        while True:
            upgrades = self.driver.find_element(By.ID,source).find_elements(By.CSS_SELECTOR,'div.enabled')
            if upgrades:
                upgrades[-1].click()
            else:
                break

    def click_golden_cookie(self) -> None:
        golden_cookie = self.driver.find_element(By.ID,'goldenCookie').find_elements(By.CSS_SELECTOR,'div')
        if golden_cookie:
            golden_cookie[0].click()

    def save_state(self) -> None:
        self.savestate_handler.save_state()

    def load_state(self) -> None:
        self.savestate_handler.load_state()

    def play(self) -> None:
        self.setup_game()
        i=0
        while True:
            self.click_cookie(i==9)
            self.get_upgrade('upgrades')
            self.get_upgrade('products')
            self.popup_handler.close_notes()
            if i==9:
                self.save_state()
            i=i+1 if i<9 else 0