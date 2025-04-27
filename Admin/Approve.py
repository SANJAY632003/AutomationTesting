from playwright.sync_api import sync_playwright
from time import sleep
from Functionalities import setup, login, logout
import data

with sync_playwright() as play:
    #setup
    browser, context, tab = setup(play)
    mail_id = data.ADMIN_MAIL_ID
    password = data.ADMIN_PASSWORD

    #login
    login(tab, mail_id, password)

    
    sleep(2)
    browser.close()