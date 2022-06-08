import csv
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import driver
from explorer import search_chatroom

driver.get("https://web.whatsapp.com")

if __name__ == "__main__":
    search_chatroom('//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')