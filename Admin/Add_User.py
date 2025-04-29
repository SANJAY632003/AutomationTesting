from playwright.sync_api import sync_playwright
from time import  sleep
from Functionalities import login, logout, invite_friends, setup
import data, pyperclip

with sync_playwright() as play:
    #setup
    browser, context, tab = setup(play)
    mail_id = data.ADMIN_MAIL_ID
    password = data.ADMIN_PASSWORD

    #login
    login(tab, mail_id, password)

    #Navigating to Add Users form
    tab.get_by_role(role="button", name="Users").click()
    sleep(0.5)
    tab.locator(selector='img[alt="AddUserIcon"]').click()
    sleep(2)

    #Filling Add Users Form
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

    #should learn this segment
    tab.locator('input#react-select-5-input').click() #clicking the dropdown
    sleep(0.5)
    options = tab.locator('[id^="react-select-5-option"]') #Find all options
    sleep(0.5)
    for i in range(options.count()):
        tab.locator('input#react-select-5-input').click() # Open the dropdown each time (since it might close after selecting)
        sleep(0.5)
        options.nth(0).click() # Get the top most existing element as each click will change indices of elements
        sleep(0.5)

    #Cancel or Submit
    choice = 0
    while 1:
        choice = int(input('To Cancel the Process, Enter 1.\nTo Submit the form, Enter 2.\nEnter: '))
        if choice in [1,2]:
            break
        print("\nInvalid Input\n")
    sleep(2)
    if choice == 1:
        tab.get_by_text('Cancel').nth(1).click()
        sleep(0.5)
        logout(tab)
        sleep(2)
        browser.close()
        exit()
    else:
        tab.get_by_text('Submit').click()
    sleep(3)

    #Logout
    logout(tab)

    # Redirecting to verification link
    verification_link = input("Enter verification link received via mail: ")
    sleep(3)
    tab.goto(url=verification_link)

    # mail-id and password
    mail_id = input('Enter mail id received via mail: ')
    password = input('Enter password received via mail: ')

    #Mentor or Mentee Registration
    registration_form = data.MENTOR_REGISTRATION_FORM if form['role']=='Mentor' else data.MENTEE_REGISTRATION_FORM

    #Login
    login(tab, mail_id, password)

    sleep(3)
    if form['role']=='Mentor':
        # Mentor Registration
        tab.get_by_text(text=registration_form['gender'], exact=True).click()
        sleep(0.5)
        tab.type(selector='input[type="text"][name="address_1"]', text=registration_form['address1'], delay=100)
        sleep(0.5)
        tab.type(selector='input[type="text"][name="address_2"]', text=registration_form['address2'], delay=100)
        sleep(0.5)

        tab.type(selector='input[type="text"][name="zip_code"]', text=registration_form['zipcode'], delay=100)
        sleep(0.5)
        tab.keyboard.press('ArrowDown')
        sleep(0.5)
        tab.keyboard.press('Enter')
        sleep(0.5)
        for i in registration_form['areas_of_expertise']:
            tab.locator(selector='input[type="text"][placeholder="Type and press Enter to add new options"]').nth(
                0).type(text=i, delay=100)
            tab.keyboard.press('Enter')
            sleep(0.5)

        tab.type(selector='input[type="text"][name="highest_degree"]', text=registration_form['highest_degree'], delay=100)
        sleep(0.5)
        tab.type(selector='input[type="text"][name="field_of_study"]', text=registration_form['field'], delay=100)
        sleep(0.5)
        tab.type(selector='input[type="text"][name="institution_name"]', text=registration_form['institution'], delay=100)
        sleep(0.5)

        tab.get_by_text(text=registration_form['previously_trained'], exact=True).click()
        sleep(0.5)
        if registration_form['previously_trained'] == "Yes":
            tab.type(selector='input[type="text"][name="mentor_exp_desc"]', text=registration_form['experience'], delay=100)
            sleep(0.5)
        tab.type(selector='input[type="number"][name="years_of_experience"]', text=registration_form['years'], delay=100)
        sleep(0.5)

        for i in registration_form['goals']:
            tab.locator(selector='input[type="text"][placeholder="Type and press Enter to add new options"]').nth(
                1).type(text=i, delay=100)
            tab.keyboard.press('Enter')
            sleep(0.5)
        tab.locator(selector='input[type="file"]').set_input_files(files=registration_form['files'])
        sleep(0.5)
    else:
        # Mentee Registration
        tab.get_by_text(text=registration_form['gender'], exact=True).click()
        sleep(0.5)
        tab.type(selector='input[type="text"][name="address_1"]', text=registration_form['address1'], delay=100)
        sleep(0.5)
        tab.type(selector='input[type="text"][name="address_2"]', text=registration_form['address2'], delay=100)
        sleep(0.5)

        tab.type(selector='input[type="text"][name="zip_code"]', text=registration_form['zipcode'], delay=100)
        sleep(0.5)
        tab.keyboard.press('ArrowDown')
        sleep(0.5)
        tab.keyboard.press('Enter')
        sleep(0.5)

        for i in registration_form['goals']:
            tab.locator(selector='input[type="text"][placeholder="Type and press Enter to add new options"]').type(
                text=i, delay=100)
            tab.keyboard.press('Enter')
            sleep(0.5)
        tab.locator(selector='input[type="file"]').set_input_files(files=registration_form['files'])
        sleep(0.5)

    # Cancel or Save or Submit
    while 1:
        choice = int(input('To Cancel the process, Enter 1.\nTo Save the form, Enter 2.\nTo Submit the form, Enter 3.\nEnter: '))
        sleep(3)
        if choice in [1, 2, 3]:
            if choice == 1:
                # Cancel
                tab.get_by_text(text='Cancel').nth(1).click()
                sleep(3)

                #Login
                login(tab, mail_id, password)

            elif choice == 2:
                # Save
                tab.get_by_text(text='Save').click()
                sleep(2)

                # Cancel
                tab.get_by_text(text='Cancel').nth(1).click()
                sleep(2)

                # Login
                login(tab, mail_id, password)

                # Pausing automation for manually filling form fields
                tab.pause()
                sleep(2)

            # Submit
            tab.get_by_text(text='Submit', exact=True).click()
            sleep(5)

            # Invite Friends
            invite_friends(tab)

            # Logout
            logout(tab)
            sleep(2)
            browser.close()
            break
        else:
            print('\nInvalid input\n')

    browser.close()



