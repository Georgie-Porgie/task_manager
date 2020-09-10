import sys
import re
import datetime
import calendar

#Login
#Login checks user.txt for registered username and passwords
#Grants access to this on the list.



#Register a new username and password and writes it to user.txt.
def reg_user():
    user_file = open("user.txt", "a+")
    if username == "admin":
        print("You have access")
        new_user1 = input("Please enter a new username: \n")
        new_pass1 = input("Please enter a new password: \n")
        user_pass1 = new_user1 , new_pass1
    for line in user_file:
            split_line = line.split(", ")
            user_check = split_line[0].strip()
            if username != user_check:
                print("Please try again, that username is already taken.")
    #Request confirmation of username and password
    new_user2 = input("Please confirm your username: \n")
    new_pass2 = input("Please confirm your password: \n")
    user_pass2 = new_user2 , new_pass2
    print("New user succesfully registered.")
    if user_pass1 == user_pass2:
            #Writes username and password to text file in format requewsted.
            user_file.write(f'\n{user_pass2[0]}, {user_pass2[1]}')
    elif username != "admin":
        print("You appear to have lost your way")
    user_file.close()
    return 0



#Option to add a new task
def add_task():

    task_file = open("tasks.txt", "a+")
    user = input("Enter the user this belongs to: \n")
    task_name = input("Enter the name of the task: \n")
    task_todo = input("Enter the task that needs to be performed: \n")
    start_date = input("Enter the start date: \n")
    due_date = input("Enter the end date: \n")
    is_completed = input("Is the task complete? \n")
    
    #Writes all input to task file
    task_file.write(f"\n{user}, {task_name}, {task_todo}, {start_date}, {due_date}, {is_completed}")
    task_file.seek(0)
    task_file.close()
    return 0

#View all tasks option
#This displays all the tasks in the file.
def view_all():
    task_file = open("tasks.txt","r")
    data = task_file.readlines()
    for line in data:
        line = line.split(", ")

        print(f'''
        \nUser:       {line[0]} 
        \nName:       {line[1]}
        \nTask:       {line[2]}
        \nStart date: {line[3]}
        \nEnd date:   {line[4]}
        \nCompleted?  {line[5]}      
    ''')
    task_file.close()
    return 0 

#This option views all tasks for signed in user.
def view_mine():
    #This is the list for the Task Numbers
    num_task_list = []  
    f = open('tasks.txt', 'r+')
    row = f.readlines()
    num_task = 0
    for i in row:
        task = i.replace(" ", "")
        task = i.replace("\n","")
        task = i.split(",")
        num_task +=1
        num_task_list.append(num_task)
        if username == task[0]:
            sentence = (f'''
                            Task Number     : {num_task}
                            Task assigned to: {task[0]}
                            Task title      : {task[1]}
                            Task descrition : {task[2]}
                            Due Date        : {task[3]}
                            Date Assigned   : {task[4]}
                            Completed       : {task[5]}\n''')
            print(sentence)
    
    task_num = int(input("Select the task number you would like to edit or -1 to return to the main menu: \n"))

    if task_num != -1:

        task_file = open ("tasks.txt", "r")
        data = task_file.readlines()
        item = data[task_num - 1].split(',')
    
    comp = input("Mark the task as complete? (Y/N): \n")
    select = item[5].upper()

    if select == "Y" or "y":
        print("This cannot be edited.")
        return 0

    if select != "Y" or "y":
        user = input("Edit user assignment: ")
        due_date = input("Edit assignment due date: ")
        items = data[task_num -1].split(", ")
        items[0] = user
        items[4] = due_date
        data[task_num - 1] = str(items)[1:-1].replace(", ")
        data[task_num - 1].strip("\n")
        print("Edit complete.")

    if task_num == len(data) and "Y" or "y":
        task_file = open("tasks.txt", "w")
        for line in data:
            line.strip("\n")
            task_file.write(f"{line}\n")
        return 0

    if task_num != len(data) and "Y" or "y":
        task_file = open("tasks.txt", "w")
        for line in data:
            line.strip("\n")
            task_file.write(f"{line}\n")
        return 0

    if select == "Y" or "y":
        items = data[task_num - 1].split(", ")
        items[5] ="Yes" or "yes"
        data[task_num - 1] = str(items)[1: -1].replace(", ")
        data [task_num -1].strip("\n")
        print("Edit complete.")

    if task_num == len(data) and select == "Y" or "y":
        task_file = open("tasks.txt", "w")
        for line in data:
            line.strip("\n")
            task_file.write(f"{line}\n")

        return 0
    
    if task_num == -1:
        task_file.close()
     
def generate_report():

    x = 0
    y = 0
    z = 0
    i = 0
    a = 0
    b = 0
    c = 0
    
    task_file = open("tasks.txt", "r+")
    tasks = task_file.readlines()
    num_tasks = len(tasks)

    for lines in tasks:
        
        items = lines.upper().split(',')
        if items[5] == " YES\n" or items[5] == " YES":
            i += 1 #completed tasks

        if items[5] == " NO\n" or items[5] == " NO":
            x += 1 #uncompleted tasks

        date = datetime.datetime.strptime(items[4], ' %m/%d/%y ')
        date_now = datetime.datetime.now()
        if date_now >  date and (items[5] == " NO\n" or items[5] == " NO"):
            y += 1 #over due tasks
        
        if username == items[0]:
            z += 1 #tasks assinged to user

        if username == items[0] and (items[5] == " YES" or items[5] == " YES\n"):
            a += 1 #tasks assigned to user and completed

        if username == items[0] and (items[5] == " NO" or items[5] == " NO\n"):
            b += 1 #tasks assgned to user and incomplete

        if username == items[0] and (items[5] == " NO" or items[5] == " NO\n") and date_now >  date:
            c += 1 #tasks assigned to user and incomplete and overdue

    #Calculates the percentages for the output to File
    percentage_incomplete = float((x/len(tasks))*100)
    percentage_overdue = float((y/len(tasks))*100)
    percentage_assigned = float((z/len(tasks))*100)
    percentage_assigned_complete = float((a/len(tasks))*100)
    percentage_assigned_incomplete = float((b/len(tasks))*100)
    percentage_assigned_incomplete_overdue = float((c/len(tasks))*100)

    task_file.close()

    #Writes updated task overview to file
    task_overview = open("task_overview.txt", "w+")
    task_overview.write(f"""
    Total number of tasks                           : {num_tasks}
    Total number of incomplete tasks                : {x}
    Total number of tasks incomplete and overdue    : {y}
    Percentage of tasks incomplete                  : {percentage_incomplete}
    Percentage of tasks incompleted and overdue     : {percentage_overdue}
    """)

    task_overview.close()

    with open('user.txt', 'r') as f:
        user = f.readlines()
        users = len(user)

    #Writes updated user overview to file
    user_overview = open('user_overview.txt', 'w+')
    user_overview.write(f"""
    Total number of users                       : {users}
    Total number of tasks                       : {num_tasks}
    Tatal tasks assgined to you                 : {z}
    Percentage of tasks assigned to you         : {percentage_assined}
    Percentage of tasks you completed           : {percentage_assined_complete}
    Percentage of tasks incomplete              : {percentage_assined_incomplete}
    Percentage of tasks incomplete and overdue  : {percentage_assined_incomplete_overdue}
                        """)
    user_overview.close()

    print("Reports successfully generated")
    return 0

#Function to display stats
def display_stats():
    user_file = open("user_overview.txt", "r")

    print("======User Overview======")
    for line in user_file:
        print(line)

    print("======Task Overview======")
    disp_task = open("task_overview.txt", "r")
    for line in disp_task:
        print(line)
    print

#Runs check to see if user is admin then prints out the admin menu    
user_file = open("user.txt", "r")
choice = 0
#User input
username = input("Please enter your username: ")
password = input("Please enter your password: ")
result = 0
if username and password:
    with open("user.txt") as f:
        for line in f:
            user, _ , pwd = line.strip().partition(", ")
            result = ((user == username) + (pwd == password)) or result
            if result == 2:
                break
if result == 2:
    print("\nWelcome!\n")
elif result:
    print("\nIncorrect username or password")

    choice = input("""
    =======================User Menu==========================
    ==========Enter the letter to select your choice==========
    A - Add task
    VA - View all tasks
    VM - View my tasks
    E - Exit    
    ==========================================================
    """)

#Admin menu options
if username == "admin" and password == "adm1n":
    choice = input('''
        =====================Admin Menu============================
        ==========Enter the letter to select your choice===========
        R - Register user 
        A - Add Task 
        VA - View all tasks
        VM - View my tasks
        GR - Generate Reports
        DS - Display Stats
        E - Exit
        ===========================================================
        ''')
    #Loops through the user choices
    if choice == "R" or choice == "r":
        reg_user()

    elif choice == "A"  or choice == "a":
        add_task()

    elif choice == "VA" or choice == "va":
        view_all()

    elif choice == "VM" or choice == "vm":
        view_mine()

    elif choice == "GR" or choice == "gr":
        generate_report()

    elif choice == "DS" or choice == "ds":
        display_stats()

    elif choice == "E" or choice == "e":
        login = True
        print("Have a nice day!")

    elif choice != "E" or choice == "e" and choice != "R" or choice == "r" and choice != "A" or choice == "a" and choice != "VA" or choice == "va" and choice != "VM"  or choice == "vm" and choice != "GR" or choice == "gr" and choice !="DS" or choice == "ds" and choice != 0:
        print ("Please make a valid choice.")

user_file.seek(0)