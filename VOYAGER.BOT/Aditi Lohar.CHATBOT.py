A =  input("\n\t\t\t\t\t\t\t\t\tClick here To Talk with Aditi lohar\t\t\t\t\t\t\n\n")
import time
def chat(text):
    for char in text:
        print(char,end = "",flush = True)
        time.sleep(0.04)
chat("Hi, I'm Aditi Lohar, what's your name ?\n\n")
user_name = input("")
chat(f"\nNice to meet you {user_name}\n\n")
chat(f"Which department are you from  {user_name} ?\n\n")
user_department = input("")
chat(f"\nOh,it's nice {user_name} 😊\n\n")
chat(f"{user_name} which year are you studying ?\n\n")
user_yearofstudy = input().lower()
if (user_yearofstudy ==  "second year" or user_yearofstudy == "2"):
    chat(f"\nOh its nice ra\n\n")
    chat(f"Which Section Are you {user_name}\n\n")
    user_section2 = input()
    chat("\noh good\n\n")
    chat(f"{user_name},I am enrolled in a club that regularly holds events which may help you earn credit through certificates.\n\n")
    chat(f"Wanna join any of the events ?\n\n")
    chat(f"\n\n1.XYZ\n2.ABC\n3.DEV\n4.No thanks\n\n")
    sundar = input()
    if ( sundar == "1"):
        user_event1 = "XYZ"
        chat(f"\n\nok thanks {user_name},Hang on a sec, I'll sign up for the event.\n")
        chat(f"{user_name} , can i get your mobile number\n")
        user_number = int(input())
        chat(f"your register number please\n")
        user_registernumber = int(input(""))
        email = str(user_registernumber) + "@klu.ac.in"
        chat(f"Okay {user_name} nice meeting you, your ticket will be sent to your email id {email} with in few working days")
        chat(f"\nThanks,good bye {user_name}")
    elif( sundar == "2"):
        user_event2 = "ABC"
        chat(f"\n\nok thanks {user_name},Hang on a sec, I'll sign up for the event.\n")
        chat(f"{user_name} , can i get your mobile number\n")
        user_number = int(input())
        chat(f"your register number please\n")
        user_registernumber = int(input(""))
        email = str(user_registernumber) + "@klu.ac.in"
        chat(f"Okay {user_name} nice meeting you, your ticket will be sent to your email id {email} with in few working days")
        chat(f"\nThanks ,good bye {user_name}")
    elif( sundar == "3"):
        user_event3 = "DEV"
        chat(f"\n\nok thanks {user_name},Hang on a sec, I'll sign up for the event.\n")
        chat(f"{user_name} , can i get your mobile number\n")
        user_number = int(input())
        chat(f"your register number please\n")
        user_registernumber = int(input(""))
        email = str(user_registernumber) + "@klu.ac.in"
        chat(f"Okay {user_name} nice meeting you, your ticket will be sent to your email id {email} with in few working days\n")
        chat(f"\ngood bye {user_name}")
    elif( sundar == "4"):
        chat(f"okay no problem {user_name},i understand you have a good day 😊\n")
elif(user_yearofstudy ==  "third year" or user_yearofstudy == "3"):
    chat(f"\nOh its nice brother")
    chat(f"Which Section Are you Brother\n\n")
    user_section3 = input()
    chat("\noh good\n\n")
    chat(f"{user_name} Bro ,I am enrolled in a club that regularly holds events which may help you earn credit through certificates.\n\n")
    chat(f"Wanna join any of the events ?\n\n")
    chat(f"\n\n1.XYZ\n2.ABC\n3.DEV\n4.No thanks\n\n")
    hanuma = input()
    if ( hanuma == "1"):
        user_event1 = "XYZ"
        chat(f"\n\nok thanks {user_name},Hang on a sec, I'll sign up for the event.\n")
        chat(f"{user_name} , can i get your mobile number\n")
        user_number = int(input())
        chat(f"your register number please\n")
        user_registernumber = int(input(""))
        email = str(user_registernumber) + "@klu.ac.in"
        chat(f"Okay {user_name} nice meeting you, your ticket will be sent to your email id {email} with in few working days")
        chat(f"\nThanks,good bye {user_name}")
    elif( hanuma == "2"):
        user_event2 = "ABC"
        chat(f"\n\nok thanks {user_name},Hang on a sec, I'll sign up for the event.\n")
        chat(f"{user_name} , can i get your mobile number\n")
        user_number = int(input())
        chat(f"your register number please\n")
        user_registernumber = int(input(""))
        email = str(user_registernumber) + "@klu.ac.in"
        chat(f"Okay {user_name} nice meeting you, your ticket will be sent to your email id {email} with in few working days")
        chat(f"\nThanks ,good bye {user_name}")
    elif( hanuma == "3"):
        user_event3 = "DEV"
        chat(f"\n\nok thanks {user_name},Hang on a sec, I'll sign up for the event.\n")
        chat(f"{user_name} , can i get your mobile number\n")
        user_number = int(input())
        chat(f"your register number please\n")
        user_registernumber = int(input(""))
        email = str(user_registernumber) + "@klu.ac.in"
        chat(f"Okay {user_name} nice meeting you, your ticket will be sent to your email id {email} with in few working days\n")
        chat(f"\ngood bye {user_name}")
    elif( hanuma == "4"):
        chat(f"okay no problem {user_name},i understand you have a good day 😊\n")
    
elif(user_yearofstudy ==  "fourth year" or user_yearofstudy == "4"):
    chat(f"\nOh its nice brother")
    chat(f"Which Section Are you Brother\n\n")
    user_section4 = input()
    chat("\noh good\n\n")
    chat(f"{user_name} Bro ,I am enrolled in a club that regularly holds events which may help you earn credit through certificates.\n\n")
    chat(f"Wanna join any of the events ?\n\n")
    chat(f"\n\n1.XYZ\n2.ABC\n3.DEV\n4.No thanks\n\n")
    bhanu = input()
    if ( bhanu == "1"):
        user_event1 = "XYZ"
        chat(f"\n\nok thanks {user_name},Hang on a sec, I'll sign up for the event.\n")
        chat(f"{user_name} , can i get your mobile number\n")
        user_number = int(input())
        chat(f"your register number please\n")
        user_registernumber = int(input(""))
        email = str(user_registernumber) + "@klu.ac.in"
        chat(f"Okay {user_name} nice meeting you, your ticket will be sent to your email id {email} with in few working days")
        chat(f"\nThanks,good bye {user_name}")
    elif( bhanu == "2"):
        user_event2 = "ABC"
        chat(f"\n\nok thanks {user_name},Hang on a sec, I'll sign up for the event.\n")
        chat(f"{user_name} , can i get your mobile number\n")
        user_number = int(input())
        chat(f"your register number please\n")
        user_registernumber = int(input(""))
        email = str(user_registernumber) + "@klu.ac.in"
        chat(f"Okay {user_name} nice meeting you, your ticket will be sent to your email id {email} with in few working days")
        chat(f"\nThanks ,good bye {user_name}")
    elif( bhanu == "3"):
        user_event3 = "DEV"
        chat(f"\n\nok thanks {user_name},Hang on a sec, I'll sign up for the event.\n")
        chat(f"{user_name} , can i get your mobile number\n")
        user_number = int(input())
        chat(f"your register number please\n")
        user_registernumber = int(input(""))
        email = str(user_registernumber) + "@klu.ac.in"
        chat(f"Okay {user_name} nice meeting you, your ticket will be sent to your email id {email} with in few working days\n")
        chat(f"\ngood bye {user_name}")
    elif( bhanu == "4"):
        chat(f"okay no problem {user_name},i understand you have a good day 😊\n")
elif(user_yearofstudy ==  "first year" or user_yearofstudy == "1"):
    chat(f"\nHope you're doing well, kiddo")
    chat(f"Which Section Are you {user_name}\n\n")
    user_section1 = input()
    chat("\noh good\n\n")
    chat(f"{user_name},I am enrolled in a club that regularly holds events which may help you earn credit through certificates.\n\n")
    chat(f"Wanna join any of the events ?\n\n")
    chat(f"\n\n1.XYZ\n2.ABC\n3.DEV\n4.No thanks\n\n")
    ashfaq = input()
    if ( ashfaq == "1"):
        user_event1 = "XYZ"
        chat(f"\n\nok thanks {user_name},Hang on a sec, I'll sign up for the event.\n")
        chat(f"{user_name} , can i get your mobile number\n")
        user_number = int(input())
        chat(f"your register number please\n")
        user_registernumber = int(input(""))
        email = str(user_registernumber) + "@klu.ac.in"
        chat(f"Okay {user_name} nice meeting you, your ticket will be sent to your email id {email} with in few working days")
        chat(f"\nThanks,good bye {user_name}")
    elif( ashfaq == "2"):
        user_event2 = "ABC"
        chat(f"\n\nok thanks {user_name},Hang on a sec, I'll sign up for the event.\n")
        chat(f"{user_name} , can i get your mobile number\n")
        user_number = int(input())
        chat(f"your register number please\n")
        user_registernumber = int(input(""))
        email = str(user_registernumber) + "@klu.ac.in"
        chat(f"Okay {user_name} nice meeting you, your ticket will be sent to your email id {email} with in few working days")
        chat(f"\nThanks ,good bye {user_name}")
    elif( ashfaq == "3"):
        user_event3 = "DEV"
        chat(f"\n\nok thanks {user_name},Hang on a sec, I'll sign up for the event.\n")
        chat(f"{user_name} , can i get your mobile number\n")
        user_number = int(input())
        chat(f"your register number please\n")
        user_registernumber = int(input(""))
        email = str(user_registernumber) + "@klu.ac.in"
        chat(f"Okay {user_name} nice meeting you, your ticket will be sent to your email id {email} with in few working days\n")
        chat(f"\ngood bye {user_name}")
    elif( ashfaq == "4"):
        chat(f"okay no problem {user_name},i understand you have a good day 😊\n")
import random
import string

def generate_token(email):
    random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    email_part = email.split('@')[0][:4].upper()  
    return f"{email_part}-{random_part}"

def collect_user_info():
    user_info = {
        'Name': user_name,
        'Department': user_department,
        'Year of Study': user_yearofstudy,
        'Section': '',
        'Event': '',
        'Email': email
    }
    
    if user_yearofstudy in ['second year', '2']:
        user_info['Section'] = user_section2
        user_info['Event'] = user_event1 if sundar == '1' else user_event2 if sundar == '2' else user_event3 if sundar == '3' else 'No event'
    elif user_yearofstudy in ['third year', '3']:
        user_info['Section'] = user_section3
        user_info['Event'] = user_event1 if hanuma == '1' else user_event2 if hanuma == '2' else user_event3 if hanuma == '3' else 'No event'
    elif user_yearofstudy in ['fourth year', '4']:
        user_info['Section'] = user_section4
        user_info['Event'] = user_event1 if bhanu == '1' else user_event2 if bhanu == '2' else user_event3 if bhanu == '3' else 'No event'
    elif user_yearofstudy in ['first year', '1']:
        user_info['Section'] = user_section1
        user_info['Event'] = user_event1 if ashfaq == '1' else user_event2 if ashfaq == '2' else user_event3 if ashfaq == '3' else 'No event'

    return user_info

def display_ticket(user_info):
    token = generate_token(user_info['Email'])
    print("\n\n==================== YOUR EVENT TICKET ====================")
    for key, value in user_info.items():
        print(f"{key}: {value}")
    print(f"Token: {token}")
    print("==========================================================")

user_info = collect_user_info()
display_ticket(user_info)


    
    




    
    






        
