import tkinter as tk
from tkinter import *
#import enigma
import enigma_machine as enigma

# Default rotor positions
position1 = 1
position2 = 1
position3 = 1
mode = "encrypt"

# Initialize the enigma machine
def initialize_enigma():
    print("init: %d %d %d"%(position1,position2,position3))
    enigma.initialize(enigma.rotor_I, position1, enigma.rotor_II, position2, enigma.rotor_III, position3)

initialize_enigma()
root = tk.Tk()
root.title("Enigma Machine")
root.configure(background = 'Dark Grey')
root.geometry("1010x400+100+100")

lblTitle = tk.Label(root, width=39, bg='Dark Grey', font=('arial', 40, 'bold'), text="\tEnigma Encryption Machine\t")

lblTitle.grid(row=0, column=0)

MainFrame = tk.Frame(root, bg='Black', bd=10, width=1250, height=490, relief=RIDGE)
MainFrame.grid(row=1, column=0, padx=30)

keys = [
    ['Q','W','E','R','T','Y','U','I','O'],
    ['A','S','D','F','G','H','J','K','L'],
    [' ','Z','X','C','V','B','N','M','P'],
]

def change_position(rotor_number):
    global position1, position2, position3
    global position1display, position2display, position3display
    global dis1var, dis2var

    if rotor_number == 1:
        try:
            position1 = int(position1display.get())
            if position1 > 26 or position1 < 1:
                print("Illegal rotor position: " + position1display.get())
                dis1var.set("Illegal rotor position")
                dis2var.set("")
            else:
                print("changing rotor to position: " + str(position1))
                dis1var.set("")
                dis2var.set("")
                initialize_enigma()

        except:
            print("Illegal rotor position: " + position1display.get())
            dis1var.set("Illegal rotor position")
            dis2var.set("")
            
    elif rotor_number == 2:
        try:
            position2 = int(position2display.get())
            if position2 > 26 or position2 < 1:
                print("Illegal rotor position: " + position2display.get())
                disvar.set("Illegal rotor position")
                dis2var.set("")
            else:
                print("changing rotor 1 to position: " + str(position2))
                dis1var.set("")
                dis2var.set("")
                initialize_enigma()

        except:
            print("Illegal rotor position: " + position2display.get())
            dis1var.set("Illegal rotor position")
            dis2var.set("")
    
    elif rotor_number == 3:
        try:
            position3 = int(position3display.get())
            if position3 > 26 or position3 < 1:
                print("Illegal rotor position: " + position3display.get())
                dis1var.set("Illegal rotor position")
                dis2var.set("")
            else:
                print("changing rotor 3 to position: " + str(position3))
                dis1var.set("")
                dis2var.set("")
                initialize_enigma()

        except:
            print("Illegal rotor position: " + position3display.get())
            dis1var.set("Illegal rotor position")
            dis2var.set("")
    else:
        print("Unknown rotor number: " + rotor_number)

    
pos1var = tk.StringVar()
pos1var.set("1")
pos1var.trace("w", lambda name, index, mode, var=pos1var: change_position(1))
position1display = tk.Entry(MainFrame, font=('courier',28), bd=0, width=3, textvariable=pos1var)
position1display.grid(row = 0, column=2, columnspan=2, pady=10)

pos2var = tk.StringVar()
pos2var.set("1")
pos2var.trace("w", lambda name, index, mode, var=pos2var: change_position(2))
position2display = tk.Entry(MainFrame, font=('courier',28), bd=0, width=3, textvariable=pos2var)
position2display.grid(row = 0, column=3, columnspan=2, pady=10)

pos3var = tk.StringVar()
pos3var.set("1")
pos3var.trace("w", lambda name, index, mode, var=pos3var: change_position(3))
position3display = tk.Entry(MainFrame, font=('courier',28), bd=0, width=3, textvariable=pos3var)
position3display.grid(row = 0, column=4, columnspan=2, pady=10)
#position2display = tk.Entry(MainFrame, font=('courier',28), bd=0, width=54)
#position2display.grid(row = 0, column=0, columnspan=2, pady=10)

def toggle():
    global mode
    global dis1var
    global dis2var
    global position1
    global position2
    global position3
    global lblTitle
    if encrypt_decrypt_toggle.config('relief')[-1] == 'sunken':
        encrypt_decrypt_toggle.config(relief="raised")
        print("raising")
        encrypt_decrypt_toggle["text"]="Encrypt"
        mode = "encrypt"
        lblTitle.config(text = "Enigma Encryption Machine")
    else:
        encrypt_decrypt_toggle.config(relief="sunken")
        print("sinking")
        encrypt_decrypt_toggle["text"]="Decrypt"
        mode = "decrypt"   
        lblTitle.config(text = "Enigma Decryption Machine")
    enigma.initialize(enigma.rotor_I, position1, enigma.rotor_II, position2, enigma.rotor_III, position3)
    dis2var.set("")
    dis1var.set("")

encrypt_decrypt_toggle = tk.Button(MainFrame, font=('courier', 14, 'bold'), width=8, height=3, text="Encrypt", relief="raised", command=toggle)
encrypt_decrypt_toggle.grid(row=0, column=7)

dis1var = tk.StringVar()
display1 = tk.Entry(MainFrame, font=('courier',28), bd=0, width=54, textvariable=dis1var)
display1.grid(row=len(keys) + 1, column=0, columnspan=len(keys[0]), pady=10)

dis2var = tk.StringVar()
display2 = tk.Entry(MainFrame, font=('courier',28), bd=0, width=54, textvariable=dis2var)
display2.grid(row=len(keys) + 2, column=0, columnspan=len(keys[0]), pady=10)

def button_click(key):
    global mode
    print(key)
    current = display1.get()
    display1.delete(0, tk.END)
    display1.insert(0, str(current) + str(key))
    current = display2.get()
    display2.delete(0, tk.END)
    display2.insert(0, str(current) + enigma.encrypt(key, mode))

for i, key_row in enumerate(keys):
    for j, key in enumerate(key_row):
        tk.Button(MainFrame, font=('courier', 14, 'bold'), text=key, width=6, height=2, command = lambda key=key:
                button_click(key)).grid(row=i + 1, column=j)

root.mainloop()

