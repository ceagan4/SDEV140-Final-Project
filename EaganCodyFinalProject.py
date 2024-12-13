import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def add():
    #accepting input from the user
    username = entryName.get()
    #accepting password input from the user
    password = entryPassword.get()
    if username and password:
        with open('username_and_passwords.txt', 'a') as f:
            f.write(f'{username} {password}\n')
        messagebox.showinfo('Success', 'You have successfully added a username and password.')
    else:
        messagebox.showerror('Error', 'Please enter both the fields.')

def get():
    #accepting input from the user
    username = entryName.get()

    #creating a dictionary to store the data in the form of key-value pairs
    passwords = {}
    try:
        #opening the text file
        with open('username_and_passwords.txt', 'r') as f:
            for k in f:
                i = k.split(' ')
                #creating the key-value pair of username and password.
                passwords[i[0]] = i[1]
    except:
        #displaying the error message
        print('ERROR. Please enter correct username.')

    if passwords:
        mess = 'Your passwords:\n'
        for i in passwords:
            if i == username:
                mess += f'Password for {username} is {passwords[i]}\n'
                break
        else:
            mess += 'Username does not exist in the list.'
        messagebox.showinfo('Passwords', mess)
    else:
        messagebox.showinfo('Passwords', 'EMPTY LIST')


def getlist():
    #creating a dictionary
    passwords = {}

    #adding a try block, this will catch errors such as an empty file or others
    try:
        with open('username_and_passwords.txt', 'r') as f:
            for k in f:
                i = k.split(' ')
                passwords[i[0]] = i[1]
    except:
        print('No passwords found')

    if passwords:
        mess = 'List of information:\n'
        for name, password in passwords.items():
            #generating a proper message
            mess += f'Password for {name} is {password}\n'
        #showing the message
        messagebox.showinfo('Passwords', mess)
    else:
        messagebox.showinfo('Passwords', 'Empty List')


def delete():
    username = entryName.get()

    #creating a temporary list to store the data
    temp_passwords = []

    #reading data from the file and excluding the specified username
    try:
        with open('username_and_passwords.txt', 'r') as f:
            for k in f:
                i = k.split(' ')
                if i[0] != username:
                    temp_passwords.append(f"{i[0]} {i[1]}")

        #writing the modified data back to the file
        with open('username_and_passwords.txt', 'w') as f:
            for line in temp_passwords:
                f.write(line)

        messagebox.showinfo(
            'Success', f'User {username} deleted successfully')
    except Exception as e:
        messagebox.showerror('Error', f'Error deleting user {username}: {e}')


if __name__ == '__main__':
    app = tk.Tk()
    app.title("Username and Password Manager")
    app.geometry('625x400')

    #Load Image 1
    image1 = Image.open('image1.jpg').resize((275,188))
    image1 = ImageTk.PhotoImage(image1)

    #Image Label for Image1
    imageLabel = tk.Label(app, image = image1)
    imageLabel.grid(row = 4, column = 1, pady = 10)

    #Load Image 2
    image2 = Image.open('image2.jpg').resize((275,188))
    image2 = ImageTk.PhotoImage(image2)

    #Image Label for Image2
    imageLabel = tk.Label(app, image = image2)
    imageLabel.grid(row = 4, column = 2)

    #Username block
    labelName = tk.Label(app, text = 'USERNAME:')
    labelName.grid(row = 0, column = 1, padx = 15, pady = 15)
    entryName = tk.Entry(app)
    entryName.grid(row = 0, column = 2, padx = 15, pady = 15)

    #Password block
    labelPassword = tk.Label(app, text = 'PASSWORD:')
    labelPassword.grid(row = 1, column = 1, padx = 10, pady = 5)
    entryPassword = tk.Entry(app)
    entryPassword.grid(row = 1, column = 2, padx = 10, pady = 5)

    #Add button
    buttonAdd = tk.Button(app, text = 'Add', command = add)
    buttonAdd.grid(row = 2, column = 1, padx = 15, pady = 8, sticky = 'we')

    #Get button
    buttonGet = tk.Button(app, text = 'Get', command = get)
    buttonGet.grid(row = 2, column = 2, padx = 15, pady = 8, sticky = 'we')

    #List button
    buttonList = tk.Button(app, text = 'List', command = getlist)
    buttonList.grid(row = 3, column = 1, padx = 15, pady = 8, sticky = 'we')

    #Delete button
    buttonDelete = tk.Button(app, text = 'Delete', command = delete)
    buttonDelete.grid(row = 3, column = 2, padx = 15, pady = 8, sticky = 'we')

    #Exit Image/Button
    exitImage = Image.open('exit.jpg').resize((50,50))
    exitImage = ImageTk.PhotoImage(exitImage)
    exitButton = tk.Button(app, image = exitImage, command = app.destroy)
    exitButton.grid(row = 0, column = 4)

    app.mainloop()