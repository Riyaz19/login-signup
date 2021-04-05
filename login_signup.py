import json
def greed():
    print('\n \t \t welcome yo my Terminal    !!')

def asking():
    print('\t 1.SIGNUP \n  \t 2.Login  ')
    userask = input(' Signup or login \n \n \t ')
    return userask

def signup():
    details = {}#for storing the data
    print("welcme to signup Page")
    username = input("\n \n  Enter your username  \t \t  " )
    email = input("\n \n \t Enter your email \t \t")
    password = input("\n \n Enter the password\n, password must contain '@' or '#' and you password should be more than 8 lenght and less than 16 \t \t  " )
    confirm_pswd = input("\n \n  Confirm  your password  \t \t  " )
    profile = input("\n \n \t Enter your bio \t \t")
    if password == confirm_pswd:
        if '@' in  password or '#' in password  and 8>=len(password)<=16 :
            details['username'] = username
            details['password'] = password
            details['profile'] = profile
            details['email'] = email

            with open(r'C:\Users\Admin\Downloads\login_signup.json','r') as json_file: #opening the file, the name of file 'login_signup.json'.
                data = json.load(json_file)
                temp = data['users']

                for ex in temp:
                    if ex['email'] == email:#compare the email, why comparirng email because the email always  unique. 
                        print("user allready exists please login")
                        return False
                temp.append(details)

            with open(r"C:\Users\Admin\Downloads\login_signup.json",'w') as f: 
                json.dump(data, f)
            print("\n \t  You are succesfully signup ")
        else:
            print("password must contain '@' or '#' and you password should be more than 8 lenght and less than 16 ")
            signup()
    else:
        print("Error!! \n password does't match " )
        signup()
    


def login():
    username = input("\n \n \t Enter your username  ")
    password = input("\n \n \t Enter your password  ")
    with open(r"C:\Users\Admin\Downloads\login_signup.json",'r') as fd:
        users_data = json.load(fd)
        all_data = users_data["users"]
    for dics in all_data:
        if username == dics['username'] and password == dics['password']:
            print("\n \n \t \t \t  succesfully logged IN")
            print(dics)
            return dics
    print("User Not found")
    reagain=input('''\t\tDo you want to create an account write 1!\n  or Do you try login again\n  write 2''').upper()
    if reagain=="1":
        signup()
    elif reagain=="2":
        login()
    else:
        print("you enter a wrong input")


def main():
    greed()
    deci = asking()
    if  deci == "signup":
        signup()
        print("now login ")
        login()
    elif  deci == "login":
        login()
    else:
        print("unvalid operation")

if __name__ == "__main__":
    main()