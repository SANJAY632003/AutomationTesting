from playwright.sync_api import sync_playwright
from time import sleep
import data

with sync_playwright() as play:
    #seting up
    browser = play.chromium.launch(executable_path=data.EXEC_PATH, headless=False, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    mail_id = data.MENTOR_MAIL_ID

    #Forgot password
    tab = context.new_page()
    tab.goto(url=data.SITE_URL)
    sleep(0.5)
    tab.press(selector='button[type="button"][class="text-[12px]  "]',key="Enter")
    sleep(0.5)
    tab.type(selector='input[type="text"]', text=mail_id, delay=100)
    sleep(0.5)
    tab.press(selector='button[type="submit"]', key="Enter")
    sleep(0.5)

    #OTP
    otp=input("Enter OTP: ")
    for i in range(len(otp)):
        tab.locator('input.otp-input').nth(i).type(text=otp[i], delay=100)
    sleep(2)
    tab.press(selector='button[type="button"]', key="Enter")

    #Password Change
    while 1:
        choice = int(input('To set new password, Enter 1.\nTo revert back to old password, Enter 2.\nEnter: '))
        if choice in [1, 2]:
            break
        print('\nInvalid input\n')

    password = data.NEW_PASSWORD if choice==1 else data.MENTOR_PASSWORD

    tab.type(selector='input[type="password"][placeholder="Enter new password"]', text=password, delay=100)
    sleep(0.5)
    tab.type(selector='input[type="password"][placeholder="Enter confirm password"]', text=password,delay=100)
    sleep(0.5)
    tab.press(selector='button[type="submit"]', key="Enter")
    sleep(0.5)

    #Login
    tab.type(selector='input[type="email"]', text=mail_id, delay=100)
    sleep(0.5)
    tab.type(selector='input[type="password"]', text=password, delay=100)
    sleep(0.2)
    tab.press(selector='button[type="submit"]', key="Enter")  # "Enter" -> keyboard key
    sleep(10)