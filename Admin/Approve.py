from playwright.sync_api import sync_playwright
from time import sleep
from Functionalities import setup, login, logout
import data

with sync_playwright() as play:
    # setup
    browser, context, tab = setup(play)
    mail_id = data.ADMIN_MAIL_ID
    password = data.ADMIN_PASSWORD

    # login
    login(tab, mail_id, password)

    # Navigating to Requests Page
    tab.get_by_role(role="button", name="Users").click()
    sleep(1)
    tab.locator(selector='img[alt="UserJoinRequestIcon"]').click()
    sleep(3)

    # search the user by mail id
    tab.type(selector='input[type="text"][placeholder="Search User Name/ Email"]', text=data.ACCOUNT_ACTION_MAIL_ID, delay=100)
    sleep(3)

    # Approval Flow Selection
    choice = int(input('To approve from 3 dots, Enter 1.\nTo approve from User Profile, Enter 2.\nEnter: '))

    sleep(2)
    browser.close()