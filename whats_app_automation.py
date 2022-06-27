import csv
import time

from config import driver
from explorer import (
    forward_message,
    search_chatroom,
    select_last_message,
    send_message,
)

driver.get("https://web.whatsapp.com")

if __name__ == "__main__":
    self_message = input()
    phone_number = input()

    forward_message(self_message, phone_number)
    select_last_message()
    # search_chatroom(
    #     '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]',
    #     self_message,
    #     phone_number,
    # )
    # with open("repo/phonenumbers.csv") as csv_file:
    #     csv_reader = csv.reader(csv_file, delimiter=",")
    #     for row in csv_reader:
    #         time.sleep(2)
    #         search_chatroom(
    #             '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]',
    #             phone_number,
    #             row[0],
    #         )
    #         time.sleep(2)
    #         send_message("test")
