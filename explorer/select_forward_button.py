from config import wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def select_forward_button():
    footer = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "OVz7E"))
    )
    all_child_by_class = footer.find_elements(By.CLASS_NAME, "_1fimr")
    button = all_child_by_class[-1]
    return button.click()
