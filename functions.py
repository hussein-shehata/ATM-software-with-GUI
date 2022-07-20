def check_number(string) :
    try :
        int(string)
        flag = True
    except :
        flag = False

    return flag 


def read_name(text) :
    temp=text.find("name")
    first_pos = temp + 7
    end_pos = text.find("  ",first_pos)
    name = text[first_pos : end_pos]
    return name

def read_password(text) :
    temp=text.find("password")
    first_pos = temp + 11
    end_pos = text.find("  ",first_pos)
    password = text[first_pos : end_pos]
    return password

def read_balance(text) :
    temp=text.find("balance")
    first_pos = temp + 10
    end_pos = -1 #becuase balance is the last thing in the line 
    end_pos = text.find(" ",first_pos)
    balance = text[first_pos : end_pos]
    balance.rstrip()
    return balance

def read_ID(text) :
    temp=text.find("ID")
    first_pos = temp + 5
    end_pos = text.find("  ",first_pos)
    ID = text[first_pos : end_pos]
    return ID

def read_status(text) :
    temp=text.find("status")
    first_pos = temp + 8
    end_pos = text.find("  ",first_pos)
    status = text[first_pos : end_pos]
    return status

def update_database(database_dict) :
    global fileobj
    fileobj=open("database.txt","w+")

    fileobj.seek(0)

    
    user_IDs = list( database_dict.keys() )
    user_numbers = len(user_IDs)

    for line in range (0,user_numbers ) :
        update_line = "ID : " +  user_IDs[line] + "     " + "name : " + database_dict[ user_IDs[line] ]["Name"] +  "     " + "password : " + database_dict[ user_IDs[line] ]["Password"] +  "     " + "balance : " + database_dict[ user_IDs[line] ]["Balance"]  +  "     " + "status :" + database_dict[ user_IDs[line] ]["Status"]+"\n"
        fileobj.write(update_line)
        fileobj.flush()
        #fileobj.write("\n")
        #print( update_line)

    fileobj.close()


def database_init():
    global fileobj
    fileobj=open("database.txt","r+")
    text=fileobj.readlines()
    database_dict ={}

    for line in text :
        line.rstrip()
        #print(line)
        ID= read_ID(line)
        name= read_name(line)
        password= read_password(line)
        balance= read_balance(line)
        status = read_status(line)
        database_dict [ID] ={"Name":name, "Password": password, "Balance": balance, "Status": status}
    fileobj.close()
    return database_dict

fileobj=None
test_try = 24
#data=database_init()

#data["215321701332"]["Balance"] = "500"
#data["215321701332"]["Password"] = "1234"

#update_database(data)
#data = database_init()
#print(data)