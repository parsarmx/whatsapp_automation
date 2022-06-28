from config import wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def find_conversation_panel(class_name, child_name):
    chatroom = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, class_name))
    )
    all_child_by_class = chatroom.find_elements(By.CLASS_NAME, child_name)
    hyper_link = all_child_by_class[len(all_child_by_class) - 1].find_element(
        By.TAG_NAME, "a"
    )

    return hyper_link


def find_last_message(class_name, child_name):
    chatroom = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, class_name))
    )
    all_child_by_class = chatroom.find_elements(By.CLASS_NAME, child_name)
    message = all_child_by_class[len(all_child_by_class) - 1].find_elements(
        By.CLASS_NAME, "_3BK98"
    )

    return message[0]
