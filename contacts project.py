import csv
import os
from subprocess import call
from time import sleep
#--------------------------------clearscreen------------------------------
def clear():
    if os.name == 'nt': 
        _ = os.system('cls')
    
    else: 
        _ = os.system('clear')

#---------------------------------inputfunc-------------------------------
def inputfunc():
    
    clist = []
    contacts = 'contacts.csv'
    with open (contacts, 'a' , newline = '') as csvfile:
        
        writer = csv.writer(csvfile, delimiter = ',')

        name = input('Enter name(necessary) : ')
        while name == '':
            name = input('Enter name(necessary) : ')
        clist.append(name)
        
        family_name = input('Enter family name(necessary) : ')
        while family_name == '':
            family_name = input('Enter family name(necessary) : ')
        clist.append(family_name)

        phone_number = input('Enter phone number(necessary) : ')
        while phone_number == '':
            phone_number = input('Enter phone number(necessary) : ')
        clist.append(phone_number)    

        email = input('Enter email address : ')
        clist.append(email)
        
        address = input('Enter address : ')
        clist.append(address)
        
        writer.writerow(clist)
        print('\nDone!')

        sleep(1.5)
        clear()

    csvfile.close()

#-------------------------------listfunc-----------------------------------
def listfunc():
    
    contacts = 'contacts.csv'

    with open (contacts, 'r', newline = '') as csvfile:

        reader = csv.reader(csvfile, delimiter = ',')
        for row in reader:
            print('\n',' '.join(row),'\n')

    csvfile.close()

#-------------------------------searchfunc----------------------------------
def searchfunc():
    
    contacts = 'contacts.csv'

    with open(contacts, 'r', newline = '') as csvfile:
        x = 0
        searchphrase = input('Enter whatever you remember from that contact : ')
        clear()

        searchlines = csvfile.readlines()

        for i, line in enumerate(searchlines):                   #searches in contacts and find all information about contact!
            if searchphrase in line:
                x = 1
                for l in searchlines[i:i+1]:
                    print(l)        
        
            else:
                pass
    if x == 0:
        print('There\'s no contact with this number!')
        sleep(1.7)
        clear()

    csvfile.close()

#--------------------------------deletefunc---------------------------------
def deletefunc():
    
    contacts = 'contacts.csv'

    with open(contacts, 'r', newline = '') as csvfile:
        
        dname = input('Enter name or family name :')
        clear()
   
        searchlines = csv.reader(csvfile)
        newlist = []
        flag = 0
        
        for row in searchlines:                   #searches in contacts and find all information about contact!
            newlist.append(row)
            
            for field in row:
                if field == dname :
                    newlist.remove(row)
                    flag = 1

                else:
                    pass
    if flag == 0:
        print('There\'s no contact with this specification!')
        sleep(1.7)
        clear()
        
    csvfile.close()

    with open (contacts, 'w' , newline = '') as csvfile:
        writer = csv.writer(csvfile, delimiter = ',')

        writer.writerows(newlist)

        print('\nDone!\n')
        sleep(1)
        clear()
    csvfile.close()

#---------------------------------changeinfofunc----------------------------
def changeinfofunc():
    
    contacts = 'contacts.csv'

    with open(contacts, 'r', newline = '') as csvfile:

        n = input('Enter name of the contact you want to edit : ')
        clear()
        # if n == 'name' or 'family_name' or 'phone_number' or 'email' or 'address':
            
        #     print('You can\'t edit header')
        # else:
        all_contacts = csv.reader(csvfile)
        lst =[]

        for row in all_contacts:
            lst.append(row)                   #searches in contacts and find all information about contact!
            
            for field in row:
                if field == n:
                    i = all_contacts.line_num
        
        o = input('''for editting name enter 1!         family name 2!
           phone number 3!               email 4!
                address 5!\n''')
        clear()
    with open(contacts, 'w', newline = '') as csvfile:

        if o == '1':
            lst[i-1][0] = input('Enter new name : ')
            clear()
        
        elif o == '2':
            lst[i-1][1] = input('Enter new family name : ')
            clear()
        
        elif o == '3':
            lst[i-1][2] = input('Enter new phone number : ')
            clear()

        elif o == '4':
            lst[i-1][3] = input('Enter new email : ')
            clear()

        elif o == '5':
            lst[i-1][4] = input('Enter new address : ')
            clear()

        writer = csv.writer(csvfile, delimiter = ',')

        writer.writerows(lst)
        print('Done!')
        sleep(1)
        clear()
        csvfile.close()

#---------------------------------sortfunc----------------------------------
# def sortfunc():
#     contacts = 'contacts.csv'
#     with open(contacts, 'r', newline = '') as csvfile:

#         reader = csvfile.readlines()
#         reader1 = reader[1:]
        
#         for k in range(len(reader1)):

#             for j in range(len(reader1)-1):
        
#                 if reader1[j] > reader1[j+1]:

#                     reader1[j] , reader1[j+1] = reader1[j+1] , reader1[j]

#     csvfile.close()

#     with open(contacts, 'w', newline = '') as csvfile:

#         writer = csv.writer(csvfile, delimiter = ',')
#         header = ['name' , 'family_name' , 'phone_number' , 'email' , 'address']
#         writer.writerow(header)
        
#         reader1=','.join(reader1)
#         writer.writerow(reader1)

#     csvfile.close()

#---------------------------------main--------------------------------------
x = os.path.exists('contacts.csv')

if x == False:
    header = ['name' , 'family_name' , 'phone_number' , 'email' , 'address']

    contacts = 'contacts.csv'
    
    with open (contacts, 'a' , newline = '') as csvfile:
        writer = csv.writer(csvfile, delimiter = ',')
        writer.writerow(header)

    csvfile.close()

while True:
    
    order = input('''    What do you want to do?
    Wanna creat new contact? Please enter ----------------- 1!
    Or you can see all of your contacts with details; enter 2!
    Searching for a contact? Enter ------------------------ 3!
    Wanna delete one of them?! Enter ---------------------- 4; I can help you!
    Finally for changing information Enter ---------------- 5!
    Shift-delete ------------------------------------------ 6!
    Sort -------------------------------------------------- 7!
    Close -----------------------------------------------exit!\n''')

    if order == '1':
        clear()
        inputfunc()

    elif order == '2':
        clear()
        listfunc()

    elif order == '3':
        clear()
        searchfunc()

    elif order == '4':
        clear()
        deletefunc()

    elif order == '5':
        clear()
        changeinfofunc()
    
    elif order == '6':
        clear()
        s = input('Are you sure?!   No : 0  Yes : 1\n')
        clear()
        if s == '1':
            if os.path.exists('contacts.csv'):
                os.remove('contacts.csv')
                clear()
                print('Deleted!')
                sleep(1.2)
                clear()
            else:
                print("The file does not exist!")
                sleep(2)
                clear()
    # elif order == '7':
    #     sortfunc()

    elif order.lower() == 'exit':
        clear()
        print('OK!')
        sleep(1)
        clear()
        break

    else:
        clear()
        print('Wrong order!')
        sleep(1.2)
        clear()