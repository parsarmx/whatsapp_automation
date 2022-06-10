from asyncio import wait_for

from config import actionChains, wait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from explorer import find_conversation_panel
from explorer.select_send_message_section import select_send_message_section

xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'


def send_hyper_link_message(phone_number):
    text = f"https://wa.me/{phone_number}"

    chat_section = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    actionChains.move_to_element(chat_section).click().perform()
    actionChains.move_to_element(chat_section).send_keys(text, Keys.RETURN).perform()
    return find_conversation_panel("_3K4-L", "_2wUmf")


def send_message(message):
    chat_section = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    actionChains.move_to_element(chat_section).click().perform()
    actionChains.move_to_element(chat_section).send_keys(message, Keys.RETURN).perform()
    return
