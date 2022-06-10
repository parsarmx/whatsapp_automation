from config import actionChains, wait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from explorer import select_send_message_section
from explorer.send_message import send_hyper_link_message


def search_chatroom(xpath, self_message, phone_number):
    first_path = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    actionChains.move_to_element(first_path).click().perform()

    actionChains.move_to_element(first_path).send_keys(
        self_message, Keys.RETURN
    ).perform()

    send_hyper_link_message(phone_number)
    return
