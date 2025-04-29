from playwright.sync_api import sync_playwright
from time import sleep
from Functionalities import login, logout, setup, invite_friends
import data, pyperclip

with (sync_playwright() as play):
    #setting up
    browser, context, tab = setup(play)

    signup_form = data.FORM_BASED_REGISTRATION

    #Filling signup form
    sleep(3)
    tab.get_by_text(text='Sign up').click() #To click Sign Up button
    sleep(0.5)
    tab.type(selector='input[type="text"][name="first_name"]', text=signup_form['first_name'], delay=100)
    sleep(0.5)
    tab.type(selector='input[type="text"][name="last_name"]', text=signup_form['last_name'], delay=100)
    sleep(0.5)
    tab.type(selector='input[type="email"]', text=signup_form['mail_id'], delay=100)
    sleep(0.5)
    tab.type(selector='input[type="password"][name="regpassword"]', text=signup_form['password'], delay=100)
    sleep(0.5)
    tab.check(selector='input[type="checkbox"]') # For selecting check box
    sleep(0.5)
    tab.get_by_text(text='Create Account').click()
    sleep(0.5)

    #Redirecting to verification link
    verification_link = input("Enter verification link received via mail: ")
    sleep(3)
    tab = context.new_page()
    tab.goto(url=verification_link)
    sleep(2)

    #Login
    login(tab, signup_form['mail_id'], signup_form['password'])
    sleep(3)

    #Navigating to Form
    tab.get_by_text(text='Mentee').click()
    sleep(0.8)
    tab.get_by_text(text='Let\'s get started').click()
    sleep(0.5)

    #Filling form
    form = data.MENTEE_REGISTRATION_FORM

    sleep(2)
    tab.type(selector='input[type="text"][name="middle_name"]', text=form['middle_name'], delay=100)
    sleep(0.5)
    tab.type(selector='input[type="text"][title="Primary Phone Number"]', text=form['primary'], delay=100)
    sleep(0.5)
    tab.type(selector='input[type="text"][title="Secondary Phone Number"]', text=form['secondary'], delay=100)
    sleep(0.5)

    tab.get_by_text(text=form['gender'], exact=True).click()
    sleep(0.5)
    tab.type(selector='input[type="text"][name="address_1"]', text=form['address1'], delay=100)
    sleep(0.5)
    tab.type(selector='input[type="text"][name="address_2"]', text=form['address2'], delay=100)
    sleep(0.5)

    tab.type(selector='input[type="text"][name="zip_code"]', text=form['zipcode'], delay=100)
    sleep(0.5)
    tab.keyboard.press('ArrowDown')
    sleep(0.5)
    tab.keyboard.press('Enter')
    sleep(0.5)

    for i in form['goals']:
        tab.locator(selector='input[type="text"][placeholder="Type and press Enter to add new options"]').type(text=i, delay=100)
        tab.keyboard.press('Enter')
        sleep(0.5)
    tab.locator(selector='input[type="file"]').set_input_files(files=form['files'])
    sleep(0.5)

    #Cancel or Save or Submit
    while 1:
        choice = int(input('To Cancel the process, Enter 1.\nTo Save the form, Enter 2.\nTo Submit the form, Enter 3.\nEnter: '))
        sleep(3)
        if choice in [1, 2,3]:
            if choice == 1:
                #Cancel
                tab.get_by_text(text='Cancel').nth(1).click()
                sleep(5)

                # Login
                login(tab, signup_form['mail_id'], signup_form['password'])
                sleep(3)

                #Fill required fields alone
                tab.type(selector='input[type="text"][title="Primary Phone Number"]', text=form['primary'],
                         delay=100)
                sleep(0.5)

            elif choice == 2:
                #Save
                tab.get_by_text(text='Save').click()
                sleep(2)

                # Cancel
                tab.get_by_text(text='Cancel').nth(1).click()
                sleep(2)

                #Login
                login(tab, signup_form['mail_id'], signup_form['password'])

                #Pausing automation for manually filling form fields
                tab.pause()
                sleep(2)

            # Submit
            tab.get_by_text(text='Submit', exact=True).click()
            sleep(5)

            #Invite Friends
            invite_friends(tab)

            #Logout
            logout(tab)
            sleep(3)
            browser.close()
            break
        else:
            print('\nInvalid input\n')
