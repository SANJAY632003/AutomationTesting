from time import sleep
from typing import Tuple
from playwright.sync_api import Playwright, Browser, BrowserContext, Page
import data, pyperclip

def setup(play:Playwright)-> Tuple[Browser, BrowserContext, Page]:
    browser = play.chromium.launch(executable_path=data.EXEC_PATH, headless=False, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    tab = context.new_page()
    sleep(0.5)
    tab.goto(url=data.SITE_URL)
    sleep(0.5)
    return browser, context, tab

def login(tab, mail_id, password):
    tab.type(selector='input[type="email"]', text=mail_id, delay=100)
    sleep(0.5)
    tab.type(selector='input[type="password"]', text=password, delay=100)
    sleep(0.5)
    tab.press(selector='button[type="submit"]', key="Enter")  # "Enter" -> keyboard key
    sleep(0.5)

def logout(tab):
    tab.locator(selector='img[class="MuiAvatar-img css-1hy9t21"]').first.click()
    sleep(0.5)
    tab.locator(selector='img[alt="LogoutIcon"]').click()
    sleep(1.5)
    tab.get_by_text(text='Logout', exact=True).first.click()

def invite_friends(tab):
    tab.get_by_text(text='Invite friends').click()
    sleep(2)
    tab.type(selector='textarea[name="recipients"]', text=f'{data.MENTOR_MAIL_ID}, {data.MENTEE_MAIL_ID}', delay=100)
    sleep(2)
    tab.locator(selector='img[alt="Copy link"]').click()
    print(f'Copied link: {pyperclip.paste()}')
    sleep(2)
    tab.get_by_text(text='Send Invites').click()
    sleep(2)

