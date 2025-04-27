from playwright.sync_api import sync_playwright
from time import  sleep
import data
from data import EXEC_PATH, SITE_URL

with sync_playwright() as play:
    #setup
    browser = play.chromium.launch(executable_path=EXEC_PATH, headless=False, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    mail_id = data.ADMIN_MAIL_ID
    password = data.ADMIN_PASSWORD

    tab = context.new_page()
    sleep(0.5)
    tab.goto(url=SITE_URL)
    sleep(0.5)

    #Login
    tab.type(selector='input[type="email"]', text=mail_id, delay=100)
    sleep(0.5)
    tab.type(selector='input[type="password"]', text=password, delay=100)
    sleep(0.5)
    tab.press(selector='button[type="submit"]', key="Enter")  # "Enter" -> keyboard key
    sleep(0.5)

    #Navigating to Add Users form
    tab.get_by_role(role="button", name="Users").click()
    sleep(0.5)
    tab.locator(selector='img[alt="AddUserIcon"]').click()
    sleep(2)

    #Form
    form = data.ADD_USER

    tab.type(selector='input[type="text"][name="FirstName"]', text=form['first_name'], delay=100)
    sleep(0.5)
    tab.type(selector='input[type="text"][name="MiddleName"]', text=form['role'], delay=100)
    sleep(0.5)

    tab.type(selector='input[type="text"][name="LastName"]', text=form['last_name'], delay=100)
    sleep(0.5)
    tab.type(selector='input[type="email"][name="EmailId"]', text=form['mail_id'], delay=100)
    sleep(0.5)

    tab.type(selector='input[type="tel"][name="PrimaryPhoneNumber"]', text=form['primary'], delay=100)
    sleep(0.5)
    tab.type(selector='input[type="tel"][name="SecondaryPhoneNumber"]', text=form['secondary'], delay=100)
    sleep(0.5)

    tab.locator('input#react-select-4-input').click() #clicking the dropdown
    sleep(0.5)
    tab.get_by_text(text=form['role'], exact=True).click()
    sleep(0.5)

    tab.locator('input#react-select-5-input').click() #clicking the dropdown
    sleep(0.5)
    options = tab.locator('[id^="react-select-5-option"]') #Find all options
    sleep(0.5)
    for i in range(options.count()):
        tab.locator('input#react-select-5-input').click() # Open the dropdown each time (since it might close after selecting)
        sleep(0.5)
        options.nth(0).click() # Get the top most existing element as each click will change indices of elements
        sleep(0.5)

    choice = 0
    while 1:
        choice = int(input('To Cancel the Process, Enter 1.\nTo Submit the form, Enter 2.\nEnter: '))
        if choice in [1,2]:
            break
        print("\nInvalid Input\n")

    sleep(2)
    if choice == 1:
        tab.get_by_text('Cancel').nth(1).click()
    else:
        tab.get_by_text('Submit').click()
    sleep(3)

    browser.close()



