import tkinter as tk
import sys
from PIL import ImageTk, Image

def exitprogram():
    sys.exit(0)

def logmein():
    secret = 'SecretPassword'
    password = entry.get()
    if password == secret:
        loginwindow.destroy()
        window = tk.Tk()
        window.title("Your Title Here")
       #Configure rows
        window.rowconfigure(0, minsize=50, weight=2)
        window.columnconfigure([0], minsize=50, weight=1)
        
        img = ImageTk.PhotoImage(Image.open("IMAGE_URL_HERE"))
        panel = tk.Label(window, image = img)
        panel.grid(row=0, column=4, sticky="nsew")
        
        #Assign a button                                            #call the func
        btn_a = tk.Button(master=window, text="CustomTextOverHere", command=doSomething)
        btn_a.grid(row=0, column=0, sticky="nsew")
        window.mainloop()
    else:
        label_errorwindow = tk.Label(text="Wrong Password!")
        label_errorwindow.grid(row=0, column=0, sticky="nsew")

def doSomething():
    #do some thing here
 

#Login Window
loginwindow = tk.Tk()
loginwindow.columnconfigure([0], minsize=100, weight=1)
img = ImageTk.PhotoImage(Image.open("Your_IMAGE_URL"))
panel = tk.Label(loginwindow, image = img)
panel.grid(row=0, column=0, sticky="nsew")
loginwindow.title("Please Login")
loginwindow.size()
label = tk.Label(text="Please Enter Password: ")
label.grid(row=1, column=0, sticky="nsew")
entry = tk.Entry(show='*')
entry.grid(row=2, column=0, sticky="nsew")

#login button, call logmein func
login = tk.Button(master=loginwindow, text="Login", command=logmein)
login.grid(row=3, column=0, sticky="nsew")

#exit button, call exitprogram func
exitprog = tk.Button(master=loginwindow, text="Exit", command=exitprogram)
exitprog.grid(row=4, column=0, sticky="nsew")


loginwindow.mainloop()
