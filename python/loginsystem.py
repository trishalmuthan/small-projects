from tkinter import *
root = Tk(className="Login")


def new_user():
    global new_root
    new_root = Tk(className="Sign Up!")

    new_username = Entry(new_root, width=40)
    new_username.pack()
    new_username.insert(0, "Insert Username")

    new_password = Entry(new_root, width=40)
    new_password.pack()
    new_password.insert(0, "Insert Password")

    done_button = Button(new_root, text="Done",
                         command=lambda: add_user(new_username.get(), new_password.get()))
    done_button.pack()
    new_root.mainloop()


def add_user(username, password):
    file = open("../loginInfo.txt", "a")
    file.write(username + "\n")
    file.write(password + "\n")
    file.close()
    texttwo = Label(new_root,
                    text="Sign Up Completed! You may close this tab unless you have another account to sign in!")
    texttwo.pack()


def sign_user():
    file = open("../loginInfo.txt", "r")

    while True:
        line1 = file.readline()
        line2 = file.readline()
        username = get_user.get() + "\n"
        password = get_pass.get() + "\n"
        if not line2:
            break
        if line1 == username:
            if line2 == password:
                get_user.destroy()
                get_pass.destroy()
                sign_in.destroy()
                sign_up.destroy()
                text = Label(root, text="Logged In! You may close this tab!")
                text.pack()
                return
    get_user.destroy()
    get_pass.destroy()
    sign_in.destroy()
    sign_up.destroy()
    text = Label(root, text="Invalid Username or Password!")
    text.pack()


global get_user
get_user = Entry(root, width=40)
get_user.pack()
get_user.insert(0, "Enter Username Here!")

global get_pass
get_pass = Entry(root, width=40)
get_pass.pack()
get_pass.insert(0, "Enter Password Here!")

global sign_in
sign_in = Button(root, text="Sign in!", command=lambda: sign_user())
sign_in.pack()

global sign_up
sign_up = Button(root, text="Sign up!", command=new_user)
sign_up.pack()

root.mainloop()
