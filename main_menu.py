import functions 
import tkinter
from tkinter import messagebox

database_dict = functions.database_init()
false_entry = 0 # variable to count the number of incorrect entry in the welcome menu 

#variables to store the user data
user_ID = None
user_password = None
user_balance = None
user_name = None 
#****************************this functions will be in another module after testing ***************************

def sign_in_Btn_func() :
    global welcome_menu_window 
    global current_state 

    global user_ID
    global user_password
    global user_balance 
    global user_name 

    user_ID =  userID_Entry.get() 
    user_password =  password_Entry.get() 
    try :
        check_temp = int ( user_ID)
        check_temp = int ( user_password)
    except :
        messagebox.showerror("Error",message=" Wrong input  ",parent = welcome_menu_window)
        return 

    database_IDs = database_dict.keys()
    
    if (user_ID not in database_IDs) :
        messagebox.showerror("Error",message="not in database  ",parent = welcome_menu_window)

    elif (database_dict[user_ID]["Status"] == "locked"):
         messagebox.showerror("Error",message="your account is locked please go to the bank  ",parent = welcome_menu_window)

    else :
        if (database_dict[user_ID]["Password"] == user_password ):
            correct_entry = True
        else :
            correct_entry = False
            global false_entry 
            false_entry = false_entry + 1 

        if (correct_entry == True ) :   
            current_state = "home_menu"

            user_balance = int( database_dict[user_ID]["Balance"] )
            user_name =  database_dict[user_ID]["Name"] 

            false_entry = 0
            welcome_menu_window.destroy()

        elif (correct_entry == False ) :
            if (false_entry > 3 ):
                print ("the account is locked ") #h3mlha pop up
                database_dict[user_ID]["Status"] =  "locked"
                functions.update_database(database_dict)

            else :
                print("you entered wrong password \nyou have " ,4-false_entry,"Trials remaining ")



#*************************** new features*****************************

def create_account_Btn_func() :
    global current_state
    global welcome_menu_window

    welcome_menu_window.destroy()
    current_state = "create_account_menu"

def submit_new_account_Btn_func() :
    global current_state 
    global create_account_menu_window

    new_user_ID = userID_Entry.get()
    new_user_name = user_name_Entry.get()
    new_user_password = password_Entry.get()
    new_user_balance = balance_Entry.get()

    if (new_user_ID in database_dict) :
        messagebox.showerror("Error",message="User Already exist")
        current_state = "welcome_menu"

    else :
        database_dict[new_user_ID] = {"Name":new_user_name, "Password": new_user_password, "Balance": new_user_balance, "Status": "unlocked"}
        functions.update_database(database_dict)

    create_account_menu_window.destroy()
    current_state = "welcome_menu"


def back_Btn_func():
    global current_state
    global create_account_menu_window

    create_account_menu_window.destroy()
    current_state = "welcome_menu"


def cash_withdraw_Btn_func():
    global current_state 
    global home_menu_window

    current_state = "cash_withdraw"
    home_menu_window.destroy()

def balance_inquiry_Btn_func():
    global current_state 
    global home_menu_window

    display_str ="Hello mr " + user_name + " \nyour balance inquiry is " + str( user_balance )
    messagebox.showerror("Balance Inquiry",message= display_str)
    #home_menu_window.destroy()
    current_state = "home_menu"
    


def password_change_Btn_func():
    global current_state 
    current_state = "password_change"
    home_menu_window.destroy()

def fawry_Btn_func():
    global current_state 
    current_state = "fawry_sevice"
    home_menu_window.destroy()



def required_withdraw_Btn_func() :
    global required_withdraw_Entry
    global cash_withdraw_window 
    global current_state 
    global user_balance
    
    try :
        required_withdraw = int( required_withdraw_Entry.get() )  #momken a3ml hna try and except 
        
    except :
        messagebox.showerror("Error",message="Wrong Input ",parent = cash_withdraw_window)
        return

    #****************if conditions for the cash withdraw
    if (required_withdraw > 5000 ) :
        messagebox.showerror("Error",message="the maxmiumn value is 5000",parent = cash_withdraw_window)

    elif (required_withdraw % 100 != 0 ) : 
        messagebox.showerror("Error",message="Not allowed value",parent = cash_withdraw_window)

    elif ( required_withdraw > user_balance ):
        messagebox.showerror("Error",message="No sufficient balance ",parent = cash_withdraw_window)
        cash_withdraw_window.destroy()
        current_state = "home_menu"

    else :
        ATM_Actuator_Out() 
        user_balance = user_balance - required_withdraw 
        database_dict[user_ID]["Balance"] = str( user_balance )

        messagebox.showerror("Error",message="Thank you",parent = cash_withdraw_window)
        cash_withdraw_window.destroy()
        current_state = "home_menu"
        #print(database_dict)
        functions.update_database(database_dict)            #testingggggggggggg
   
        


def password_Btn_func() :
    global password_change_window 
    global current_state 
    
    global database_dict
    global user_ID
    global user_password
    global user_balance 
    global user_name 

    password1 = password_1_Entry.get()
    try :
        check_temp = int (password1) 
    except :
        messagebox.showerror("Error",message="Wrong Input ",parent = password_change_window)
        return

    password2 = password_2_Entry.get()
    if (password1 == password2 ):
        if ( len(password1) != 4 ):
            messagebox.showerror("Error",message="Password length must be equal to 4 ",parent = password_change_window)
        else :
            user_password = password1
            database_dict[user_ID]["Password"] = user_password # momken a5leha yt3mlha editing fe el file nfso el txt bs b3den
            password_change_window.destroy()
            current_state = "welcome_menu"
            functions.update_database(database_dict)            #testingggggggggggg
    else :
        messagebox.showerror("Error",message="The two passwords arenot matched  ",parent = password_change_window)

  

def orange_Btn_func():
    global current_state 
    global fawry_menu_window

    fawry_menu_window.destroy()
    current_state = "recharge_menu"

def vodafone_Btn_func():
    global current_state 
    global fawry_menu_window

    fawry_menu_window.destroy()
    current_state = "recharge_menu"

def etisalat_Btn_func():
    global current_state 
    global fawry_menu_window

    fawry_menu_window.destroy()
    current_state = "recharge_menu"

def we_Btn_func():
    global current_state 
    global fawry_menu_window

    fawry_menu_window.destroy()
    current_state = "recharge_menu"


def submit_Btn_func():
    global recharge_menu_window
    global current_state

    global database_dict
    global user_ID
    global user_password
    global user_balance 
    global user_name 


    try :
        recharge_amount = int( recharge_amount_Entry.get() )
        phone_number = number_Entry.get()
        check_temp = int (phone_number)

    except :
        messagebox.showerror("Error",message="Wrong Input ",parent = recharge_menu_window)
        return

#checking if the phone number is valid
    if ( len(phone_number) != 11) :
        messagebox.showerror("Error",message="Phone number length must be equal to 11 ",parent = recharge_menu_window)
    else :
        #checking if the balance have suffcient sum 
        if (recharge_amount > user_balance ):
            messagebox.showerror("Error",message=" No sufficient balance ",parent = recharge_menu_window)
            recharge_menu_window.destroy()
            current_state = "home_menu"
        
        else :
            messagebox.showerror("notice",message="Thank you ",parent = recharge_menu_window)
            recharge_menu_window.destroy()
            current_state = "home_menu" 
            user_balance = user_balance - recharge_amount
            database_dict[user_ID]["Balance"] = str( user_balance ) # momken a5leha yt3mlha editing fe el file nfso el txt bs b3den
            functions.update_database(database_dict)            #testingggggggggggg



def exit_Btn_func():
    global current_state 
    global home_menu_window
    global welcome_menu_window

    try :
        home_menu_window.destroy()
    except :
        pass
    try:
        welcome_menu_window.destroy()
    except :
        pass
    current_state = "exit_action"


def ATM_Actuator_Out():
    print("will be implented later")


    



current_state = "welcome_menu"
Flag = True


while( Flag == True) :
#********************************************************************************    
#*********************************welcome menu part **********************************
#**********************************************************************************

    if (current_state == "welcome_menu") :
        #initlize the window 
        welcome_menu_window = tkinter.Tk()

        welcome_menu_window.title(" Welcome menu Window")

        welcome_menu_window.geometry("400x400")

        welcome_menu_window.resizable(False,False)

        welcome_menu_window.configure(background = "Lavender")     
    # making the 2 entries 
        userID_Entry = tkinter.Entry(welcome_menu_window, width = 40, background = "White", foreground = "Black")
        userID_Entry.place(x = 100, y = 0)

        password_Entry = tkinter.Entry(welcome_menu_window, width = 40, background = "White", foreground = "Black", show='*')
        password_Entry.place(x = 100, y = 40)

    #making the 2 labels 
        userID_Label = tkinter.Label(welcome_menu_window, text = "userID: ")
        userID_Label.place(x= 0, y= 0)

        password_Label = tkinter.Label(welcome_menu_window, text = "password ")
        password_Label.place(x= 0, y= 40)

    #making the 3 button to sign in and to close and to create new user
        sign_in_Btn = tkinter.Button(welcome_menu_window, text = "Sign in", width = 8, height = 2, background = "Green", foreground = "White", command = sign_in_Btn_func)
        sign_in_Btn.place(x= 100, y= 100)

        exit_Btn = tkinter.Button(welcome_menu_window, text = "Exit", width = 8, height = 2, background = "Green", foreground = "White", command = exit_Btn_func)
        exit_Btn.place(x= 200, y= 100)
    
        create_account_Btn = tkinter.Button(welcome_menu_window, text = "Create account", width = 12, height = 2, background = "Green", foreground = "White", command = create_account_Btn_func)
        create_account_Btn.place(x= 300, y= 100)

        welcome_menu_window.mainloop()

#********************************************************************************    
#*********************************home menu part **********************************
#**********************************************************************************

    elif (current_state == "home_menu") :
        home_menu_window = tkinter.Tk()

        home_menu_window.title(" Home menu Window")

        home_menu_window.geometry("400x400")

        home_menu_window.resizable(False,False)

        home_menu_window.configure(background = "Lavender")     

    #making the 5 buttons to demonstrate the avaible options 
        cash_withdraw_Btn = tkinter.Button(home_menu_window, text = "Cash withdraw", width = 15, height = 2, background = "Green", foreground = "White", command = cash_withdraw_Btn_func)
        cash_withdraw_Btn.place(x= 10, y= 10)

        balance_inquiry_Btn = tkinter.Button(home_menu_window, text = "Balance Inquiry", width = 15, height = 2, background = "Green", foreground = "White", command = balance_inquiry_Btn_func)
        balance_inquiry_Btn.place(x= 200, y= 10)

        password_change_Btn = tkinter.Button(home_menu_window, text = "password change", width = 15, height = 2, background = "Green", foreground = "White", command = password_change_Btn_func)
        password_change_Btn.place(x= 10, y= 50)

        fawry_Btn = tkinter.Button(home_menu_window, text = "Fawry Service", width = 15, height = 2, background = "Green", foreground = "White", command = fawry_Btn_func)
        fawry_Btn.place(x= 200, y= 50)

        exit_Btn = tkinter.Button(home_menu_window, text = "Exit", width = 15, height = 2, background = "Green", foreground = "White", command = exit_Btn_func)
        exit_Btn.place(x= 100, y= 100)

        home_menu_window.mainloop()
        

    #*********************************************************************************
    # ************************** Create account menu part ****************************
    # ********************************************************************************
        
    elif ( current_state == "create_account_menu") :
        #initlize the window 
        create_account_menu_window = tkinter.Tk()

        create_account_menu_window.title(" Create account menu Window")

        create_account_menu_window.geometry("400x400")

        create_account_menu_window.resizable(False,False)

        create_account_menu_window.configure(background = "Lavender")     
    # making the 4 entries 
        userID_Entry = tkinter.Entry(create_account_menu_window, width = 40, background = "White", foreground = "Black")
        userID_Entry.place(x = 100, y = 0)

        user_name_Entry = tkinter.Entry(create_account_menu_window, width = 40, background = "White", foreground = "Black")
        user_name_Entry.place(x = 100, y = 40)

        password_Entry = tkinter.Entry(create_account_menu_window, width = 40, background = "White", foreground = "Black", show='*')
        password_Entry.place(x = 100, y = 80)

        balance_Entry = tkinter.Entry(create_account_menu_window, width = 40, background = "White", foreground = "Black")
        balance_Entry.place(x = 100, y = 120)

    #making the 4 labels 
        userID_Label = tkinter.Label(create_account_menu_window, text = "userID: ")
        userID_Label.place(x= 0, y= 0)

        name_Label = tkinter.Label(create_account_menu_window, text = "name ")
        name_Label.place(x= 0, y= 40) 

        password_Label = tkinter.Label(create_account_menu_window, text = "password ")
        password_Label.place(x= 0, y= 80)     

        balance_Label = tkinter.Label(create_account_menu_window, text = "Balance ")
        balance_Label.place(x= 0, y= 120)    

    #making 2 buttons one for back and one for submit
        submit_new_account_Btn = tkinter.Button(create_account_menu_window, text = "Submit", width = 15, height = 2, background = "Green", foreground = "White", command = submit_new_account_Btn_func)
        submit_new_account_Btn.place(x= 80, y= 200)

        back_Btn = tkinter.Button(create_account_menu_window, text = "Back", width = 15, height = 2, background = "Green", foreground = "White", command = back_Btn_func)
        back_Btn.place(x= 200, y= 200)


        create_account_menu_window.mainloop()

#********************************************************************************    
#*********************************cash withdraw part **********************************
#**********************************************************************************
    elif ( current_state == "cash_withdraw") :


        cash_withdraw_window = tkinter.Tk()

        cash_withdraw_window.title("Cash withdraw Window")

        cash_withdraw_window.geometry("400x400")

        cash_withdraw_window.resizable(False,False)

        cash_withdraw_window.configure(background = "Lavender")

        #making button to accept the entry 
        required_withdraw_Btn = tkinter.Button(cash_withdraw_window, text = "Accept", width = 8, height = 2, background = "Green", foreground = "White", command = required_withdraw_Btn_func)
        required_withdraw_Btn.place(x= 200, y= 100)

        #making the label for the entry
        required_withdraw_Label = tkinter.Label(cash_withdraw_window, text = "required withdraw : ")
        required_withdraw_Label.place(x= 0, y= 0)

        # making the entry to take the required withdraw 
        required_withdraw_Entry = tkinter.Entry(cash_withdraw_window, width = 40, background = "White", foreground = "Red")
        required_withdraw_Entry.place(x = 150, y = 0)

        #required_withdraw = required_withdraw_Entry.get() feh moshkla hna 3aiz ab2a ashofha 

        #user_balance = database_dict[user_ID]["Balance"]




        cash_withdraw_window.mainloop()

#********************************************************************************    
#*********************************password change part **************************
#********************************************************************************

    elif (current_state == "password_change"):
        password_change_window = tkinter.Tk()

        password_change_window.title(" Password change window")

        password_change_window.geometry("400x400")

        password_change_window.resizable(False,False)

        password_change_window.configure(background = "Lavender")     
    # making the 2 entries 
        password_1_Entry = tkinter.Entry(password_change_window, width = 40, background = "White", foreground = "Black", show='*')
        password_1_Entry.place(x = 200, y = 0)

        password_2_Entry = tkinter.Entry(password_change_window, width = 40, background = "White", foreground = "Black", show='*')
        password_2_Entry.place(x = 200, y = 40)

    #making the 2 labels 
        password_1_Label = tkinter.Label(password_change_window, text = "The new password ")
        password_1_Label.place(x= 0, y= 0)

        password_2_Label = tkinter.Label(password_change_window, text = "confirm the new password ")
        password_2_Label.place(x= 0, y= 40)

    #making the 2 button to sign in and to close
        password_Btn = tkinter.Button(password_change_window, text = "OK", width = 8, height = 2, background = "Green", foreground = "White", command = password_Btn_func)
        password_Btn.place(x= 200, y= 100)

        password_change_window.mainloop()

    elif (current_state == "fawry_sevice") :
        fawry_menu_window = tkinter.Tk()

        fawry_menu_window.title(" Fawry menu window")

        fawry_menu_window.geometry("400x400")

        fawry_menu_window.resizable(False,False)

        fawry_menu_window.configure(background = "Lavender")     

    #making the 4 buttons to demonstrate the avaible options 
        orange_Btn = tkinter.Button(fawry_menu_window, text = "Orange Recharge", width = 15, height = 2, background = "Green", foreground = "White", command = orange_Btn_func)
        orange_Btn.place(x= 10, y= 10)

        vodafone_Btn = tkinter.Button(fawry_menu_window, text = "Vodafone Recharge", width = 15, height = 2, background = "Green", foreground = "White", command = vodafone_Btn_func)
        vodafone_Btn.place(x= 200, y= 10)

        etisalat_Btn = tkinter.Button(fawry_menu_window, text = "Etisalat Recharge", width = 15, height = 2, background = "Green", foreground = "White", command = etisalat_Btn_func)
        etisalat_Btn.place(x= 10, y= 50)

        we_Btn = tkinter.Button(fawry_menu_window, text = "We Recharge", width = 15, height = 2, background = "Green", foreground = "White", command = we_Btn_func)
        we_Btn.place(x= 200, y= 50)

        fawry_menu_window.mainloop()
    
    elif (current_state == "recharge_menu") :

        recharge_menu_window = tkinter.Tk()

        recharge_menu_window.title(" Recharge menu window")

        recharge_menu_window.geometry("400x400")

        recharge_menu_window.resizable(False,False)

        recharge_menu_window.configure(background = "Lavender")

    # making the 2 entries 
        number_Entry = tkinter.Entry(recharge_menu_window, width = 40, background = "White", foreground = "Black")
        number_Entry.place(x = 200, y = 0)

        recharge_amount_Entry = tkinter.Entry(recharge_menu_window, width = 40, background = "White", foreground = "Black")
        recharge_amount_Entry.place(x = 200, y = 40)

        #making the 2 labels 
        number_Label = tkinter.Label(recharge_menu_window, text = "The phone number  ")
        number_Label.place(x= 0, y= 0)

        recharge_amount_Label = tkinter.Label(recharge_menu_window, text = "The recharge amount ")
        recharge_amount_Label.place(x= 0, y= 40) 

        #making button to submit
        submit_Btn = tkinter.Button(recharge_menu_window, text = "OK", width = 8, height = 2, background = "Green", foreground = "White", command = submit_Btn_func)
        submit_Btn.place(x= 200, y= 100)


        recharge_menu_window.mainloop()

    elif (current_state == "exit_action"):
        Flag = False 

