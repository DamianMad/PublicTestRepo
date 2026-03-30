from selenium import webdriver
from pages.betting import BettingPage


def test_successful_single_bet_placement():
    driver = webdriver.Chrome()

    betting_page = BettingPage(
        driver=driver,
        base_url="https://qae-assignment-tau.vercel.app/",
        user_id="candidate-3d0b2f5a",
    )

    try:
        betting_page.open()
        betting_page.select_team()
        betting_page.enter_stake("10.09")
        betting_page.place_bet()

        confirmation_text = betting_page.wait_for_confirmation()

        assert "success" in confirmation_text.lower()

    finally:
        driver.quit()