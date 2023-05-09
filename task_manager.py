#=====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import date

#====Login Section====

username = input("Enter username: ")
password = input("Enter password: ")

#====opening file====
with open('user.txt','r') as user_file:
    user_names = []
    pass_words = []

    # reading lines of the file and seperating inforamtion and stroing them in appropriate variables
    for line in user_file:
        # removing \n commands
        temp = line.strip()
        # spliting the line into differente information 
        temp = temp.split(", ")
        # adding information to a appropriate list. 
        # first item on list which is the username goes into the username list 
        user_names.append(temp[0])
        pass_words.append(temp[1])
    
    # setting a boolean to true
    check = True
    # while the check has to be done the loop continues
    while check:
        # checking if the username is in the txt file(username list)
        if username in user_names:
            # checking if the password is in the username files
            if password in pass_words:
                # boolean gets set to false. check does not need to be done to loop wont continue
                check = False
            else:
                # re-asks for password
                password= input("\nIncorrect password entered please try again: ")
        else:
            # re-asks for username and password
            username = input("\nIncorrect username entered.\nEnter username:  ")
            password = input("Enter password: ")

#====menu=====
while True:
    # presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    if username == "admin":
        menu = input("\nSelect one of the following Options below:\nr - Registering a user\na - Adding a task\nva - View all tasks\nvm - view my task\ns - View statistics\ne - Exit\n: ").lower()
    else :
         menu = input("\nSelect one of the following Options below:\nr - Registering a user\na - Adding a task\nva - View all tasks\nvm - view my task\ne - Exit\n: ").lower()
    

    # checking the option menu
    if menu == 'r':
        
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''
        # checking if admin is loggedf in
        if username == "admin":
            # asking for informatio not update users.txt
            new_username=input("\nEnter new username: ")
            new_password = input("Enter new password: ")
            confirm_password = input("confirm password: ")

            # making sure that confiramtion password enterd match new password enterd
            while new_password != confirm_password:
                new_password = input("\nInvalid confirmation password\nEnter password: ")
                confirm_password = input("Confirm password: ")          
            
            # open txt file and insert information in correct format
            with open('user.txt','a') as user_file:
                user_file.write(f"\n{new_username}, {new_password}")
        
        else:
            print("\nYou cannot perform that option!")



    elif menu == 'a':
        
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''
        # asking for information
        username_task = input("\nEnter username: ")
        title = input("Enter title: ")
        description = input("Enter task description: ")
        due_date = input("Enter task due date: ")
        # method to get current date 
        today_date = date.today()
        # stroring in correct format
        month = today_date.strftime("%B")
        month = month[0:3]
        year = today_date.strftime("%Y")
        day = today_date.strftime("%d")
        today = day+" "+month+" " +year 

        # open txt file tasks and write inforamtion in correct format
        with open('tasks.txt','a') as task_file:
            task_file.write(f"\n{username_task}, {title}, {description}, {today}, {due_date}, No")#\n for new line
        


    elif menu == 'va':
        # open txt tasks to only read from it
        with open('tasks.txt','r') as task_file:
         for line in task_file:
            # remove white spaces and new line commands
            temp = line.strip()
            #split the string for seperate information
            temp = temp.split(",")
            print("------------------------------------------------------")
            #display in correct format
            print(f"Task:\t\t\t{temp[1]}\nAssigned to:\t\t {temp[0]}\nDate assigned:\t\t{temp[3]}\nDue date:\t\t{temp[4]}\nTask complete?\t\t{temp[5]}\nTask description:\t{temp[2]}")
            print("------------------------------------------------------")
        
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''                            
        
    elif menu == 'vm':
       
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''
        with open('tasks.txt','r') as task_file:
            for line in task_file:
                # remove white spaces and new line commands
                temp= line.strip()
                #split the string for seperate information
                temp = temp.split(",")
                #check if username on task is same as username of logged in person
                if temp[0] == username:
                    print("------------------------------------------------------")
                    #display in correct format
                    print(f"Task:\t\t\t{temp[1]}\nAssigned to:\t\t {temp[0]}\nDate assigned:\t\t{temp[3]}\nDue date:\t\t{temp[4]}\nTask complete?\t\t{temp[5]}\nTask description:\t{temp[2]}")
                    print("------------------------------------------------------") 
                

                  
    elif menu == "s":
        num_tasks = 0
        num_users = 0
        # opens txt
        with open('tasks.txt','r') as task_file:
            # repeats loops for number of lines in txt file
            for line in task_file:
                # counts how much times loop has iterated
                num_tasks +=1
        with open('user.txt','r') as user_file:
            for line in user_file:
                num_users += 1
        print(f"\nTotal number of users :{num_users}\nTotal number of tasks:{num_tasks}")
               

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")