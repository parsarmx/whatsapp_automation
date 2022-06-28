import time

from config import actionChains, wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from explorer import find_last_message


def select_last_message():
    navbar_xpath = '//*[@id="main"]/header/div[3]/div/div[2]/div/div/span'
    navbar = wait.until(
        EC.presence_of_element_located((By.XPATH, navbar_xpath))
    )
    actionChains.move_to_element(navbar).click().perform()

    select_message_xpath = '//*[@id="app"]/div/span[4]/div/ul/div/div/li[2]'

    navbar_sections = wait.until(
        EC.presence_of_element_located((By.XPATH, select_message_xpath))
    )
    time.sleep(1)
    actionChains.move_to_element(navbar_sections).double_click().perform()

    return find_last_message("_3K4-L", "_2wUmf").click()
