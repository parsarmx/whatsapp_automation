from config import actionChains, wait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


def pop_up_search(contact):
    xpath = '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[2]'

    first_path = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    actionChains.move_to_element(first_path).click().perform()

    actionChains.move_to_element(first_path).send_keys(contact).perform()


def pop_up_select_checkbox():

    forward_to = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "_3uIPm"))
    )
    all_child_by_class = forward_to.find_elements(By.CLASS_NAME, "_2nY6U")

    return all_child_by_class[0]


def forward():

    icon = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/span/div/div/div',
            )
        )
    )
    actionChains.move_to_element(icon).click().perform()
    # return actionChains.move_to_element(icon).click().perform()
