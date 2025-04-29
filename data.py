#Setup
EXEC_PATH = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
SITE_URL = 'https://mma-socialimpact.socialroots-test.net/'

#Admin Credentials
ADMIN_MAIL_ID = 'jaishritest@gmail.com'
ADMIN_PASSWORD = 'Data@123'

#Mentor Credentials
MENTOR_MAIL_ID = 'sanjay@dataterrain.com'
MENTOR_PASSWORD = 'Data@123'

#Mentee Credentials#1
MENTEE_MAIL_ID = 'menteesanjay@gmail.com'
MENTEE_PASSWORD = 'Data@123'

#Mentee Credentials#2
MENTEE_MAIL_ID_2 = 'testmentee6@gmail.com'
MENTEE_PASSWORD_2 = 'Data@123'

#Forgot Password Credential
NEW_PASSWORD = 'Data@1234'

#Registration
GOOGLE_BASED_REGISTRATION = {
    "username":"Test Mentee",
    "mail_id":"testmentee6@gmail.com",
    "password":"Data@1234"
}
FORM_BASED_REGISTRATION = {
    "first_name":"Test",
    "last_name":"User",
    "mail_id":MENTEE_MAIL_ID_2,
    "password":MENTEE_PASSWORD_2
}
MENTOR_REGISTRATION_FORM = {
    "middle_name":"Mentor",
    "primary":"1234567890",
    "secondary":"2345678901",
    "gender":"Male",
    "address1":"AAA",
    "address2":"BBB",
    "zipcode":"10002",
    "areas_of_expertise":['abc','def'],
    "highest_degree":"PhD",
    "field":"Engineering",
    "institution":"ABC University",
    "previously_trained":"No",
    "experience":"Sample description",
    "years":"5",
    "goals":['ghi','jkl'],
    "files":["C:/Users/SANJAY S/Desktop/sample1.jpeg", "C:/Users/SANJAY S/Desktop/sample2.jpeg"]
}
MENTEE_REGISTRATION_FORM = {
    "middle_name":"Mentee",
    "primary":"3456789012",
    "secondary":"4567890123",
    "gender":"Male",
    "address1":"AAA",
    "address2":"BBB",
    "zipcode":"94102",
    "goals":['ghi','jklm'],
    "files":["C:/Users/SANJAY S/Desktop/sample1.jpeg", "C:/Users/SANJAY S/Desktop/sample2.jpeg"]
}

#Admin adds a User
ADD_USER = {
    "first_name":"Test",
    "last_name":"User",
    "mail_id":"testmentee6@gmail.com",
    "primary":"1234567890",
    "secondary":"2345678901",
    "role":"Mentor"
}

#User Account Actions by Admin
ACCOUNT_ACTION_MAIL_ID = 'testmentee6@gmail.com'