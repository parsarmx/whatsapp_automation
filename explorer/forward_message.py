import time

from config import actionChains, wait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from explorer.pop_up_search import (
    forward,
    pop_up_search,
    pop_up_select_checkbox,
)
from explorer.select_forward_button import select_forward_button
from explorer.select_message import select_last_message


def forward_message(message_path, send_message_to):
    """-------------------------- Find Chat Room --------------------------"""

    xpath = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'
    search_bar = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    actionChains.move_to_element(search_bar).click().perform()

    actionChains.move_to_element(search_bar).send_keys(
        message_path, Keys.RETURN
    ).perform()

    select_last_message()

    select_forward_button()

    pop_up_search(send_message_to)

    time.sleep(1.2)
    pop_up_select_checkbox().click()

    forward()
