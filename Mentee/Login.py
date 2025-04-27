from time import sleep
from playwright.sync_api import sync_playwright
import data

with (sync_playwright() as play):

    browser = play.chromium.launch(executable_path=data.EXEC_PATH, headless=False, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True) # To disable default view port
    mail_id = data.MENTEE_MAIL_ID
    password = data.MENTEE_PASSWORD

    tab = context.new_page()
    sleep(0.5)
    tab.goto(url=data.SITE_URL)
    sleep(0.5)
    tab.type(selector='input[type="email"]',text=mail_id, delay=100)
    sleep(0.5)
    tab.type(selector='input[type="password"]',text=password, delay=100)
    sleep(0.2)
    tab.press(selector='button[type="submit"]', key="Enter") # "Enter" -> keyboard key
    sleep(10)

    browser.close()