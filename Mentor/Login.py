from time import sleep
from playwright.sync_api import sync_playwright
from Functionalities import login, logout, setup
import data

with (sync_playwright() as play):
    #setup
    browser, context, tab = setup(play)
    mail_id = data.MENTOR_MAIL_ID
    password = data.MENTOR_PASSWORD

    #login
    login(tab, mail_id, password)
    sleep(2)

    #logout
    logout(tab)
    sleep(2)

    browser.close()