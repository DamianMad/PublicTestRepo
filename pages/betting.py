import re
from decimal import Decimal
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BettingPage:
    TEAM_BUTTON = (By.ID, "odds-premier-league-manutd-chelsea-home")
    STAKE_INPUT = (By.ID, "bet-slip-stake-input")
    PLACE_BET_BUTTON = (By.ID, "bet-slip-place-bet")
    BET_CONFIRMATION = (By.XPATH, "//h2[text()='Bet Placed Successfully!']")

    def __init__(self, driver: WebDriver, base_url: str, user_id: str, timeout: int = 10):
        self.driver = driver
        self.base_url = base_url
        self.user_id = user_id
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(f"{self.base_url}?user-id={self.user_id}")

    def select_team(self):
        self.wait.until(EC.element_to_be_clickable(self.TEAM_BUTTON)).click()

    def enter_stake(self, value: str):
        stake_input = self.wait.until(EC.visibility_of_element_located(self.STAKE_INPUT))
        stake_input.clear()
        stake_input.send_keys(value)

    def place_bet(self):
        self.wait.until(EC.element_to_be_clickable(self.PLACE_BET_BUTTON)).click()

    def wait_for_confirmation(self):
        return self.wait.until(EC.visibility_of_element_located(self.BET_CONFIRMATION)).text